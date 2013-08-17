from django.contrib.auth.models import User
from django.test import TestCase

from tastypie.test import TestApiClient


class TestApiClientTestCase(TestCase):

    def test_patch(self):
        """
        test patching with the UserResource
        """
        username = 'johndoe'
        user = User.objects.get(username=username)
        uri = '/api/v1/users/%s/' % (user.pk)

        # we'll try to change the first name (which is currently unset)
        new_first_name = 'John'
        payload = {
            'first_name': new_first_name,
        }

        client = TestApiClient()

        # make sure we get a 202
        response = client.patch(uri, data=payload)
        self.assertEqual(response.status_code, 202)

        # make sure the first_name changed
        user = User.objects.get(username=username)
        self.assertEqual(user.first_name, new_first_name)
