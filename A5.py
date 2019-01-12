# -*- coding: utf-8 -*-
# Author:0verWatch

X = ''
Y = ''
Z = ''

import base64
import re


def str2bin(str_mess):
    res = ""
    for i in str_mess:
        tmp = bin(ord(i))[2:].zfill(8)
        res += tmp
    return res



def bin2str(bin_mess):
    res = ""
    tmp = re.findall(r'.{8}',bin_mess)
    for i in tmp:
        res += chr(int(i,2))
    return res


def LFSRinit(): #用64bit密钥初始3个移位寄存器,分别是19,22,23位
    global X
    global Y
    global Z
    key = input("请输入8位秘钥\n")
    while len(key) != 8:   #限定只能是8位，然后生成64位的二进制流
        key = input("请输入8位秘钥\n")
    key_bin_str = ""
    for i in key:
        tmp = bin(ord(i))[2:].zfill(8)
        key_bin_str += tmp
    X = key_bin_str[0:19]
    Y = key_bin_str[19:41]
    Z = key_bin_str[41:]
    # print("X"+X)
    # print("Y"+Y)
    # print("Z"+Z)



def xor(bin_str,bin_key): #输入的字符串的二进制流
    res = ""
    for i in range(len(bin_str)):
        if bin_str[i] == bin_key[i]:
            res += '0'
        else:
            res += '1'
    return res


def create_key():
    global X
    global Y
    global Z
    LFSRinit()
    res = ""
    for i in range(114):   # A5 / 1用于为每个突发产生114比特的密钥流序列
        # a = X[-1]
        # b = Y[-1]
        # c = Z[-1]
        g  = int(X[-1]) ^ int(Y[-1]) ^ int(Z[-1])
        res += str(g)  #用最后一位异或产生秘钥流
        x =  str(int(X[13]) ^  int(X[16]) ^ int(X[17]) ^ int(X[18]) ^ 1)               #候选位的值
        y =  str(int(Y[20]) ^ int(Y[21]) ^ 1)
        z = str(int(Z[7]) ^ int(Z[20]) ^ int(Z[21]) ^ int(Z[22]) ^ 1)
        #选择的钟控位
        c_x = int(X[8])
        c_y = int(Y[10])
        c_z = int(Z[10])
        if (c_x + c_y + c_z) >= 2:#多数的占优
            choice = '1'
        else:
            choice = '0'
        if str(c_x) == choice:
            X = x + X[:-1] #隐式位移，这里是不包含最后一位的
        if str(c_y) == choice:
            Y = y + Y[:-1]
        if str(c_z) == choice:
            Z = z + Z[:-1]
        # print("X"+X)
        # print("Y"+Y)
        # print("Z"+Z)
    # print(res)
    return res

def a5_encode(mess):
    bin_mess = str2bin(mess)
    bin_key = create_key()
    bin_cipher = ""
    #print(len(bin_mess))
    if len(bin_mess) % 114 == 0:
        for i in range(0, len(bin_mess), 114):
            bin_cipher += xor(bin_mess, bin_key)
    elif len(bin_mess) > 114:
        j = 0
        for i in range(len(bin_mess)):
            bin_cipher += str(int(bin_mess[i]) ^ int(bin_key[i]))
            j += 1
            if j == 114:
                j = 0
    else:
        for i in range(len(bin_mess)):
            bin_cipher += str(int(bin_mess[i]) ^ int(bin_key[i]))
    print("二进制密文" + bin_cipher)
    print("十六进制密文"+hex(int(bin_cipher,2)))
    str_cipher = bin2str(bin_cipher)
    print(base64.b64encode(str_cipher.encode('utf-8')))





def a5_decode(bin_mess):
    bin_key = create_key()
    bin_cipher = ""
    # print(len(bin_mess))
    if len(bin_mess) % 114 == 0:
        for i in range(0, len(bin_mess), 114):
            bin_cipher += xor(bin_mess, bin_key)
    elif len(bin_mess) > 114:
        j = 0
        for i in range(len(bin_mess)):
            bin_cipher += str(int(bin_mess[i]) ^ int(bin_key[i]))
            j += 1
            if j == 114:
                j = 0
    else:
        for i in range(len(bin_mess)):
            bin_cipher += str(int(bin_mess[i]) ^ int(bin_key[i]))
    str_cipher = bin2str(bin_cipher)
    print("解密后的结果:"+str_cipher)



def get_info():
    choice = input("1.加密\n2.解密\n")
    if choice == '1':
        message = input("输入你的信息\n")
        a5_encode(message)
    elif choice == '2':
        bin_message = input("输入你的信息\n")
        a5_decode(bin_message)
    else:
        print("请重新输入")

if __name__ == '__main__':
    while True:
        get_info()
