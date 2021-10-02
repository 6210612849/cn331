from django.test import TestCase, Client
from .models import Course, Student
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Max

# Create your tests here.


class RegTestCase(TestCase):
    def setUp(self):
        test_subject = Course.objects.create(
            course_id="1", course_name="test lab", seat=0, maxSeat=1, credit=3)

    def test_course_seat_available(self):
        course = Course.objects.first()
        self.assertTrue(course.is_seat_available())

    def test_course_view(self):
        c = Client()
        response = c.get(reverse("reg:index"))
        self.assertEqual(response.status_code, 302)

    def test_course_login_view(self):
        c = Client()
        user = User.objects.create(
            username="user", password="1234", email="usermail")
        c.force_login(user)
        response = c.get(reverse("reg:index"))
        self.assertEqual(response.status_code, 200)
