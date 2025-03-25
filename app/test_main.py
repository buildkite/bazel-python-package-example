import unittest
import json
from main import greet

class TestMain(unittest.TestCase):
    def test_generate_pipeline(self):
        self.assertEqual(greet(), "The Python package says, 'Hi!'")
