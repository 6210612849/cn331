from django.test import TestCase, Client
from reg.models import Course, Student
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Max
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
# Create your tests here.


class RegTestCase(TestCase):
    def setUp(self):
        test_subject = Course.objects.create(
            course_id="1", course_name="test lab", seat=0, maxSeat=1, credit=3)
        pwd_test = make_password('12345')
        test_user = User.objects.create(
            username="user5", password=pwd_test, email="usermail")

        test_student = Student.objects.create(student_id=test_user)

    def test_index_failed_view(self):
        c = Client()
        response = c.get(reverse("users:index"))
        self.assertEqual(response.status_code, 302)

    def test_index_success_view(self):
        c = Client()
        c.force_login(User.objects.first())
        response = c.get(reverse("users:index"))

        self.assertEqual(response.status_code, 200)

    def test_login_not_view(self):
        c = Client()
        response = c.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/login.html")

    def test_login_success_view(self):
        c = Client()

        response = c.post(reverse('users:login'), {
                          "username": "user5", "password": "12345"}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/index.html')

    def test_login_wrong_view(self):
        c = Client()

        response = c.post(reverse('users:login'), {
                          "username": "user5", "password": "1234"}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_logout_view(self):
        c = Client()
        c.force_login(User.objects.first())
        response = c.get(reverse('users:logout'), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_reg_success_view(self):
        c = Client()
        c.force_login(User.objects.first())
        student = Student.objects.get(
            student_id=User.objects.get(username="user5"))
        subject = Course.objects.first()
        student.subjects.add(subject)
        response = c.get(reverse('users:reg'))
        self.assertEqual(response.status_code, 200)
