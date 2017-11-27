# -*- coding: UTF-8 -*-

import unittest
import roman  # 同じフォルダーにあるroman.pyを読み込む

class Test(unittest.TestCase):

    def test_to_number(self):
        self.assertEqual(1, roman.to_number('I'))
        self.assertEqual(3, roman.to_number('III'))
        self.assertEqual(4, roman.to_number('IV'))
        self.assertEqual(5, roman.to_number('V'))
        self.assertEqual(6, roman.to_number('VI'))
        self.assertEqual(9, roman.to_number('IX'))
        self.assertEqual(444, roman.to_number('CDXLIV'))
        self.assertEqual(3999, roman.to_number('MMMCMXCIX'))

    def test_to_number_exeption(self):
        with self.assertRaises(ValueError):
            roman.to_number('IIII')

        with self.assertRaises(ValueError):
            roman.to_number('VV')

        with self.assertRaises(ValueError):
            roman.to_number('A')

    def test_to_roman(self):
        self.assertEqual('I', roman.to_roman(1))
        self.assertEqual('III', roman.to_roman(3))
        self.assertEqual('IV', roman.to_roman(4))
        self.assertEqual('V', roman.to_roman(5))
        self.assertEqual('VIII', roman.to_roman(8))
        self.assertEqual('IX', roman.to_roman(9))
        self.assertEqual('X', roman.to_roman(10))
        self.assertEqual('L', roman.to_roman(50))
        self.assertEqual('CDXLIV', roman.to_roman(444))
        self.assertEqual('MMMCMXCIX', roman.to_roman(3999))

    def test_to_roman_exception(self):
        self.assertEqual('範囲外です', roman.to_roman(0))
        self.assertEqual('範囲外です', roman.to_roman(4000))


if __name__ == "__main__":
    # このファイルを指定して実行した場合は、以下の命令を実行する
    unittest.main()