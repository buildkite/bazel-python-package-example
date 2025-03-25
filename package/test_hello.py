import unittest
import hello

class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello.say_hi(), "Hi!")

if __name__ == "__main__":
    unittest.main()