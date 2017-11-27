# -*- coding: UTF-8 -*-

'''
日本語を扱う場合は、ファイルのエンコードを指定する
'''

import re # 正規表現ライブラリ

num1s = ['', u'壱', u'弐', u'参', u'肆', u'伍', u'陸', u'漆', u'捌', u'玖']
num2s = ['', '', u'弐', u'参', u'肆', u'伍', u'陸', u'漆',u'捌', u'玖']
digits = ['', u'拾', u'佰', u'仟']

def to_daiji(number):
    '''数値を大字に変換する'''

    if (number < 0 or 9999 <number):
        raise ValueError(u'範囲外です')

    if (number == 0):
        return u'零'

    daiji = ''
    for digit in range(3, 0, -1):
        num = int(number / pow(10, digit))
        daiji += num2s[num]
        if (num != 0):
            daiji += digits[digit]
        number = number % pow(10, digit)

    daiji += num1s[number]
    return daiji

def to_number(daiji):
    '''大字を数値に変換する'''

    def _to_number(result, digit):
        '''位ごとの大字を数値に変換する'''

        index = len(digits) - digit

        if (not result.group(index)):
            return 0

        if (result.group(index) == digits[digit]):
            return pow(10, digit)

        val = result.group(index)[0:-1]
        num = num1s.index(val)

        return num * pow(10, digit)

    def _to_number_one(result):
        '''壱の位の大字を数値に変換する'''

        if (not result.group(len(digits))):
            return 0

        val = result.group(len(digits))
        num = num1s.index(val)

        return num

    pattern = u'^([弐参肆伍陸漆捌玖]?仟)?([弐参肆伍陸漆捌玖]?佰)?([弐参肆伍陸漆捌玖]?拾)?([壱弐参肆伍陸漆捌玖]?)$|^零$'
    result = re.match(pattern, daiji)

    if not result:
        raise ValueError(u'大字として正しくありません')

    if result.group(0) == u'零':
        return 0

    number = 0
    number += _to_number_one(result)
    for rank in range(1, len(digits)):
        number += _to_number(result, rank)
    return number

if __name__ == '__main__':
    print(to_daiji(0)) # 零
    print(to_daiji(1)) # 壱
    print(to_daiji(10)) # 拾
    print(to_daiji(11)) # 拾壱
    print(to_daiji(100)) # 佰
    print(to_daiji(1000)) # 仟
    print(to_daiji(9999)) # 玖仟玖佰玖拾玖