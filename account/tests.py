# from django.test import TestCase
# from django.urls import reverse
# from account.models import Account
# from django.contrib.auth.models import User

# class AuthTest(TestCase):
#     def setUp(self):
#         self.register_url = reverse('account:register')
#         self.login_url = reverse('account:login')
#         # self.factory = RequestFactory()
#         self.user = {
#             'email': 'test@gmail.com',
#             'username': 'test',
#             'fullname':'test',
#             'phone_number': 7938292,
#             'address': 'test',
#             'password1': 'test123',
#             'password2': 'test123'
#         }
#         return super().setUp()

#     def testRegister(self):
#         response = self.client.post(self.register_url, self.user, format = "text/html")
#         self.assertEqual(response.status_code, 200)

#     def testLogin(self):
#         response = self.client.post(self.register_url, self.user, format = "text/html")
#         response = self.client.post(self.login_url, {'email':'test@gmail.com', 'password':'test123'})
#         self.assertEqual(response.status_code, 200)
