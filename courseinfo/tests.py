from django.test import TestCase, Client
from django.urls import reverse


class CourseInfoTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_instructor_list_view(self):
        response = self.client.get(reverse('courseinfo_instructor_list_urlpattern'))
        self.assertEqual(response.status_code, 200)

    def test_student_list_view(self):
        response = self.client.get(reverse('courseinfo_student_list_urlpattern'))
        self.assertEqual(response.status_code, 200)
