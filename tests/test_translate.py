import unittest


class MyTestCase(unittest.TestCase):
    def test_ja2zh(self):
        from translate import Translator
        translate = Translator(to_lang='zh', from_lang='ja', provider='microsoft')
        result = translate.translate("あのれはいい")
        print(result)
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
