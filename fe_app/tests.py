from django.test import TestCase
from .models import Thread, Post, Comment

# Create your tests here.
#import unittest

class unitTestsClass(TestCase):

    def test_comment(self):
        self.assertNotEqual(Comment.text, None)
        #self.assertNotEqual("a", "a")

    def test_post(self):
        self.assertNotEqual(Post.text, None)

    def test_thread(self):
        self.assertNotEqual(Thread.text, None)

if __name__ == '__main__':
    unittest.main()