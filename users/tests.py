from django.test import TestCase, Client
from reg.models import Course, Student
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Max
from django.contrib.auth.hashers import make_password

# Create your tests here.

class UserTestCase(TestCase):
    def setUp(self):
        pwd = make_password('password')
        testuser = User.objects.create(username='testuser', password=pwd , email='testuser@email.com')
        teststudent = Student.objects.create(Student_id='testuser', subjects='null' , credit='20', maxCredit='20')

    def test_user_not_auth(self):
        c = Client()
        response = c.get(reverse('users:index'))
        self.assertEqual(response.status_code, 302)

    def test_user_index(self):
        c = Client()
        c.force_login(User.objects.first())
        response = c.get(reverse('users:index'))
        self.assertEqual(response.status_code, 200)

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