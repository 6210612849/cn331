from django.test import TestCase, Client
from reg.models import Course, Student
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Max

# Create your tests here.


class RegTestCase(TestCase):
    def test_main_view(self):
        c = Client()
        response = c.get(reverse("first:index"))
        self.assertEqual(response.status_code, 200)

    def test_contact_fix_view(self):
        c = Client()
        response = c.get(reverse("first:contact"))
        self.assertEqual(response.status_code, 200)
