# -*- coding: utf-8 -*-
# Author:0verWatch

import struct
import math
import binascii

lrot = lambda x,n: (x << n)|(x >> 32- n)  #循环左移的骚操作

#初始向量
A, B, C, D = (0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476)
# A, B, C, D = (0x01234567, 0x89ABCDEF, 0xFEDCBA98, 0x76543210)

#循环左移的位移位数
r = [   7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
        5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20,
         4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
         6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, asda6, 10, 15, 21
        ]

#使用正弦函数产生的位随机数，也就是书本上的T[i]
k =  [int(math.floor(abs(math.sin(i + 1)) * (2 ** 32))) for i in range(64)]


def init_mess(message):
    global A
    global B
    global C
    global D
    A, B, C, D = (0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476)
    # A, B, C, D = (0x01234567, 0x89ABCDEF, 0xFEDCBA98, 0x76543210)
    length = struct.pack('<Q', len(message)*8)  #原消息长度64位比特的添加格式，太骚额这种写法
    while len(message) > 64:
        solve(message[:64])
        message = message[64:]
    #长度不足64位消息自行填充
    message += '\x80'
    message += '\x00' * (56 - len(message) % 64)
    #print type(length)
    message += length
    # print binascii.b2a_hex(message)
    solve(message[:64])


def solve(chunk):
    global A
    global B
    global C
    global D
    w = list(struct.unpack('<' + 'I' * 16, chunk))  #分成16个组，I代表1组32位,tql,学到了
    a, b, c, d = A, B, C, D

    for i in range(64):  #64轮运算
        if i < 16:  #每一轮运算只用到了b,c,d三个
            f = ( b & c)|((~b) & d)
            flag  = i      #用于标识处于第几组信息
        elif i < 32:
            f = (b & d)|(c & (~d))
            flag = (5 * i +1) %16
        elif i < 48:
            f = (b ^ c ^ d)
            flag  = (3 * i + 5)% 16
        else:
            f = c ^(b |(~d))
            flag  = (7 * i ) % 16
        tmp = b + lrot((a + f + k[i] + w[flag])& 0xffffffff,r[i]) #&0xffffffff为了类型转换
        a, b, c, d = d, tmp & 0xffffffff, b, c
        #print(hex(a).replace("0x","").replace("L",""), hex(b).replace("0x","").replace("L","") , hex(c).replace("0x","").replace("L",""), hex(d).replace("0x","").replace("L",""))
    A = (A + a) & 0xffffffff
    B = (B + b) & 0xffffffff
    C = (C + c) & 0xffffffff
    D = (D + d) & 0xffffffff



def digest():
    global A
    global B
    global C
    global D
    return struct.pack('<IIII',A,B,C,D)

def hex_digest():
    return binascii.hexlify(digest()).decode()


if __name__ == '__main__':
    while True:
        mess = raw_input("请输入你的信息:")
        init_mess(mess)
        out_put = hex_digest()
        print out_put





