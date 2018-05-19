from rest_framework import serializers

from call_project.calls.models import Bill


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
