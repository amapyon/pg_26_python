# -*- coding: UTF-8 -*-

import re # 正規表現ライブラリ

def to_number(roman):
    '''ローマ数字を数値に変換する'''

    pattern = '^M{0,3}(CM|D|CD)?C{0,3}(XC|L|XL)?X{0,3}(IX|V|IV)?I{0,3}?$'
    result = re.match(pattern, roman)
    if not result:
        raise ValueError('ローマ数字として正しくありません')

    roman_to_number = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }

    number = 0
    pre = 0
    for i in range(len(roman) - 1, -1, -1):
        ch = roman[i]
        num = roman_to_number[ch]
        if num >= pre:
            number += num
            pre = num
        else:
            number -= num

    return number


def to_roman(number):
    '''数値をローマ数字に変換する'''

    if number < 1 or 3999 < number:
        return '範囲外です'

    def _to_roman(number, one, five, ten):
        '''位ごとに数値をローマ数字に変換する'''

        if number == 0:
            return ''
        if number == 1:
            return one
        if number == 2:
            return one * 2
        if number == 3:
            return one * 3
        if number == 4:
            return one + five
        if number == 5:
            return five
        if number == 6:
            return five + one
        if number == 7:
            return five + one * 2
        if number == 8:
            return five + one * 3
        if number == 9:
            return one + ten



    m = int(number / 1000)
    number %= 1000
    c = int(number / 100)
    number %= 100
    x = int (number / 10)
    i = number % 10

    roman = _to_roman(m, 'M', '', '')
    roman += _to_roman(c, 'C', 'D', 'M')
    roman += _to_roman(x, 'X', 'L', 'C')
    roman += _to_roman(i, 'I', 'V', 'X')

    return roman

if __name__ == '__main__':
    # このファイルを指定して実行した場合は、以下の命令を実行する
    print(to_number('I')) # 1
    print(to_number('IV')) # 4
    print(to_number('CDXLIV')) # 444
#    print(to_number('B')) # ローマ数字として正しくありません

    print(to_roman(1)) # I
    print(to_roman(4)) # IV
    print(to_roman(5)) # V
    print(to_roman(9)) # IX
    print(to_roman(10)) # X
    print(to_roman(11)) # XI
    print(to_roman(444)) # CDXLIV
    print(to_roman(3999)) # MMMCMXCIX