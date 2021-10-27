from django.core import mail
from django.test import TestCase
from rest_framework.test import RequestsClient

class EndpointTest(TestCase):
    def test_github_request(self):
        client = RequestsClient()
        response = client.get('http://testserver/api/georgemjohnson11/auth_system/')
        assert response.status_code == 200

#https://docs.djangoproject.com/en/3.2/topics/testing/tools/#email-services
class EmailTest(TestCase):
    def test_send_email(self):
        mail.send_mail(
            'Subject here', 'Here is the message.',
            'from@example.com', ['to@example.com'],
            fail_silently=False,
        )
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Subject here')