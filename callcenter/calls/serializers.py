from .models import Call, Bill, TYPES
from rest_framework import serializers

import rest_framework.validators
from .validators.custom_validator import RequiredIf


class CallSerializer(serializers.Serializer):
    """
    Call Serializer class
    """
    call_id = serializers.CharField(required=False, max_length=32,
                                    min_length=32)
    destination = serializers.CharField(min_length=10,
                                        max_length=11,
                                        required=False
                                        )
    call_type = serializers.ChoiceField(choices=TYPES, required=True)
    source = serializers.CharField(min_length=10,
                                   max_length=11,
                                   required=False
                                   )

    def create(self, validated_data):
        return Call.objects.create(**validated_data)

    def validate(self, data):
        if data['call_type'] == TYPES[0][0]:
            call = Call.objects.filter(source=data['source'],
                                       destination=data['destination']).last()
            if call and call.call_type == TYPES[0][0]:
                raise serializers.ValidationError(
                    'Warning, this call has already been terminated.')
        else:
            call_finished = Call.objects.filter(call_id=data['call_id']).last()
            if call_finished and call_finished.call_type == TYPES[1][0]:
                raise serializers.ValidationError(
                    "Hey, This call has already been closed.")
            elif not call_finished:
                raise serializers.ValidationError(
                    "Hey, This call does not exist.")
        return data

    class Meta:
        model = Call
        fields = ('call_type', 'call_id', 'source', 'destination')
        validators = [RequiredIf(fields=('call_id',),
                                 condition=('call_type', 2)),
                      RequiredIf(fields=('source', 'destination'),
                                 condition=('call_type', 1))
                      ]


class BillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bill
        fields = ('destination', 'call_start_date', 'call_start_time',
                  'call_price')
