# -*- coding: UTF-8 -*-

import unittest
import daiji # 同じフォルダーにあるdaiji.pyを読み込む

class Test(unittest.TestCase):

    def test_to_number(self):
        self.assertEqual(0, daiji.to_number(u'零'))
        self.assertEqual(1, daiji.to_number(u'壱'))
        self.assertEqual(10, daiji.to_number(u'拾'))
        self.assertEqual(20, daiji.to_number(u'弐拾'))
        self.assertEqual(39, daiji.to_number(u'参拾玖'))
        self.assertEqual(1000, daiji.to_number(u'仟'))
        self.assertEqual(4000, daiji.to_number(u'肆仟'))
        self.assertEqual(9465, daiji.to_number(u'玖仟肆佰陸拾伍'))

    def test_to_number_exception(self):
        with self.assertRaises(ValueError):
            daiji.to_number(u'佰仟')

        with self.assertRaises(ValueError):
            daiji.to_number(u'仟仟佰')

    def test_to_daiji(self):
        self.assertEqual(u'零', daiji.to_daiji(0))
        self.assertEqual(u'壱', daiji.to_daiji(1))
        self.assertEqual(u'拾', daiji.to_daiji(10))
        self.assertEqual(u'拾壱', daiji.to_daiji(11))
        self.assertEqual(u'弐拾参', daiji.to_daiji(23))
        self.assertEqual(u'佰', daiji.to_daiji(100))
        self.assertEqual(u'肆佰伍拾陸', daiji.to_daiji(456))
        self.assertEqual(u'仟', daiji.to_daiji(1000))
        self.assertEqual(u'仟壱', daiji.to_daiji(1001))
        self.assertEqual(u'漆仟捌佰玖拾', daiji.to_daiji(7890))
        self.assertEqual(u'玖仟玖佰玖拾玖', daiji.to_daiji(9999))

    def test_to_daiji_exception(self):
        with self.assertRaises(ValueError):
            daiji.to_daiji(-1)

        with self.assertRaises(ValueError):
            daiji.to_daiji(10000)

if __name__ == "__main__":
    unittest.main()