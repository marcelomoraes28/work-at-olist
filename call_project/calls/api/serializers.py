from rest_framework import serializers

from .validators.custom_validator import RequiredIf
from .models import Call, Bill, TYPES
from .tasks import generate_bill


class BillSerializer(serializers.Serializer):

    call_id = serializers.IntegerField(required=True)
    timestamp = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S",
                                          required=True)

    def create(self, validated_data):
        try:
            bill_exist = Bill.objects.get(call_id=validated_data['call_id'])
            return bill_exist
        except Bill.DoesNotExist:
            created = Bill.objects.create(**validated_data)
            return created

    class Meta:
        model = Bill
        fields = ('destination', 'timestamp',
                  'call_id', 'call_price')


class CallSerializer(serializers.Serializer):
    """
    Call Serializer class
    """
    call_id = BillSerializer()
    destination = serializers.CharField(min_length=10,
                                        max_length=11,
                                        required=False
                                        )
    type = serializers.ChoiceField(choices=TYPES, required=True)
    source = serializers.CharField(min_length=10,
                                   max_length=11,
                                   required=False
                                   )
    timestamp = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S",
                                          required=True)

    def create(self, validated_data):
        created = Call.objects.create(**validated_data)
        if created.type == TYPES[1][0]:
            last = Call.objects.filter(call_id=created.call_id.call_id).last()
            created.source = last.source
            created.destination = last.destination
            created.save()
            generate_bill.delay(created.call_id.call_id)
        return created

    def validate(self, data):
        """
        Validate data before save
        :param data:
        :return:
        """
        call_exist = Call.objects.filter(call_id=data['call_id'].get('call_id'),
                                         type=TYPES[1][0]).first()
        if call_exist:
            raise serializers.ValidationError(
                'This call already exists and has already been closed.')
        if data['type'] == TYPES[0][0]:
            call = Call.objects.filter(source=data['source'],
                                       destination=data['destination']).first()
            if call and call.type == TYPES[0][0]:
                raise serializers.ValidationError(
                    'Warning, this call has already been terminated.')
        else:
            call_finished = Call.objects.filter(call_id=data['call_id'].get('call_id')).first()
            if call_finished and call_finished.type == TYPES[1][0]:
                raise serializers.ValidationError(
                    "Hey, This call has already been closed.")
            elif call_finished and call_finished.timestamp > data['timestamp']:
                raise serializers.ValidationError(
                    "The date can not be less than %s" % call_finished.timestamp)
            elif not call_finished:
                raise serializers.ValidationError(
                    "Hey, This call does not exist.")
        return data

    class Meta:
        model = Call
        fields = (
            'type', 'call_id', 'source', 'destination', 'timestamp')
        validators = [RequiredIf(fields=('call_id',),
                                 condition=('type', 2)),
                      RequiredIf(fields=('source', 'destination'),
                                 condition=('type', 1))
                      ]
