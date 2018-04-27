from .models import Call, Bill, TYPES
from rest_framework import serializers


class CallSerializer(serializers.Serializer):
    """
    Call Serializer class
    """
    source = serializers.CharField(required=False, min_length=10,
                                   max_length=11)
    destination = serializers.CharField(required=False, min_length=10,
                                        max_length=11)
    type = serializers.ChoiceField(choices=TYPES, default=1)

    call_id = serializers.CharField(required=False, max_length=32)

    def create(self, validated_data):
        return Call.objects.create(**validated_data)

    def validate(self, data):
        if data['type'] == TYPES[0][0]:
            call = Call.objects.filter(source=data['source'],
                                       destination=data['destination']).last()
            if call and call.call_type == TYPES[0][0]:
                raise serializers.ValidationError(
                    'Warning, this call has already been terminated.')
        else:
            call_finished = Call.objects.filter(source=data['source'],
                                                destination=data['destination'])\
                .last()
            if call_finished.call_id != data['call_id']:
                raise serializers.ValidationError(
                    "Call_id doesn't match.")

    class Meta:
        model = Call
        fields = ('type', 'call_id', 'source', 'destination')


class BillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bill
        fields = ('destination', 'call_start_date', 'call_start_time',
                  'call_price')
