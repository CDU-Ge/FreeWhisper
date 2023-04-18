import unittest
import pip


class MyTestCase(unittest.TestCase):
    def test_something(self):
        pip.main(['install', 'pip', '-t', 'test_libs'])

if __name__ == '__main__':
    unittest.main()
