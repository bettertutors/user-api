from unittest import TestCase, main as unittest_main

from webtest import TestApp

from user_api import user_app


class TestRestApi(TestCase):
    app = TestApp(user_app)

    users = (
        {'email': u'foo@bar.com', 'institute': u'UNSW', 'role': u'tutor'},
        {'email': u'foobar@car.com', 'institute': u'Sydney', 'role': u'tutor'}
    )

    def test_signup(self):
        for user in self.users:
            print self.app.post('/api/user/signup', user).json


if __name__ == '__main__':
    unittest_main()
