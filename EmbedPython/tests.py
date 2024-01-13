import unittest

import EmbedPython


class MyTestCase(unittest.TestCase):
    def test_run(self):
        EmbedPython.python("-V")

    def test_pip(self):
        r = EmbedPython.ensurepip()
        print(r)


if __name__ == '__main__':
    unittest.main()
