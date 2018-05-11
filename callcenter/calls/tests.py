from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from calls.models import Call, TYPES


class CallTests(APITestCase):

    def __init__(self, *args, **kwargs):
        super(CallTests, self).__init__(*args, **kwargs)
        self.call_id = None

    def test_starting_a_call(self):
        """
        Ensure we can create a new call object.
        """
        url = reverse('calls')
        data = {'source': '41997471140',
                'destination': '41997471112',
                'call_id': 1,
                'timestamp': '2018-05-10 11:00:00',
                'call_type': TYPES[0][0],
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Call.objects.count(), 1)
        self.assertEqual(Call.objects.get().call_id, response.data['call_id'])
        self.call_id = response.data['call_id']
        self.finish_a_call()

    def finish_a_call(self):
        """
        Ensure we can create a new call object
        """
        url = reverse('calls')
        data = {'call_id': self.call_id,
                'call_type': TYPES[1][0],
                'timestamp': '2018-05-10 11:23:00',
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Call.objects.count(), 2)
        self.assertEqual(Call.objects.last().call_id, response.data['call_id'])

    def test_missing_arguments_type_one(self):
        """
        Ensure to validate arguments
        """
        url = reverse('calls')
        data = {'call_type': TYPES[0][0]}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['call_id'][0], "This field is required.")
        self.assertEqual(response.data['timestamp'][0], "This field is required.")

    def test_missing_arguments_type_two(self):
        """
        Ensure to validate arguments
        """
        url = reverse('calls')
        data = {'call_type': TYPES[1][0]}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['call_id'][0], "This field is required.")
