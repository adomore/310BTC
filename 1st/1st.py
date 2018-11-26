import sys
sys.path.append('../common')

from common import words as ws

data = '511 B20 332 328 410 530 ' \
       '22B 0FE 52E D0F 7A1 65B ' \
       '52C 7E7 511 2F6 56F C4B'

date = '20181002'


def sub(o, d):
    o = int('0x' + o, 16)
    d = int(d)
    if o < d:
        o = o + 16
    return (hex(o - d) + '')[2].upper()


skip = 0

for i in range(len(data)):
    c = data[i]
    if c != ' ':
        n = date[(i - skip) % 8]
        n = sub(c, n)
        data = data[:i] + n + data[(i+1):]
    else:
        skip = skip + 1

data = data.split(' ')

data = data[6:]

keys = ''

for index in data:
    keys = keys + ws.get_word(int('0x' + index, 16)) + ' '

print(keys)
