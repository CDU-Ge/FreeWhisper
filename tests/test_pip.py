import unittest
import pip


class MyTestCase(unittest.TestCase):
    def test_install(self):
        pip.main(['install', 'python_mop', '-t', 'test_libs'])

    def test_uninstall(self):
        pip.main(['uninstall', 'python_mop', '-t', 'test_libs'])

if __name__ == '__main__':
    unittest.main()
