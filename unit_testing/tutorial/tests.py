import unittest
from pyramid import testing

class tutorialViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
    
    def tearDown(self):
        testing.tearDown()
    
    def test_hello_world(self):
        from tutorial import hello_world

        request = testing.DummyRequest()
        response = hello_world(request)
        self.assertEqual(1, 1)
        self.assertEqual(response.status_code, 200)