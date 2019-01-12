# -*- coding: utf-8 -*-
# Author:0verWatch

import base64

def get_message():
    print("输入你的信息：")
    s = input()
    return s

def get_key():
    print("输入你的秘钥：")
    key = input()
    if key == '':
        key = 'none_public_key'
    return key

def init_box(key):
    """
    S盒 
    """
    s_box = list(range(256)) #我这里没管秘钥小于256的情况，小于256应该不断重复填充即可
    j = 0
    for i in range(256):
        j = (j + s_box[i] + ord(key[i % len(key)])) % 256
        s_box[i], s_box[j] = s_box[j], s_box[i]
    #print(type(s_box)) #for_test
    return s_box

def ex_encrypt(plain,box,mode):
    """
    利用PRGA生成秘钥流并与密文字节异或，加解密同一个算法
    """

    if mode == '2':
        while True:
            c_mode = input("输入你的解密模式:Base64 or ordinary\n")
            if c_mode == 'Base64':
                plain = base64.b64decode(plain)
                plain = bytes.decode(plain)
                break
            elif c_mode == 'ordinary':
                plain = plain
                break
            else:
                print("Something Wrong,请重新新输入")
                continue

    res = []
    i = j =0
    for s in plain:
        i = (i + 1) %256
        j = (j + box[i]) %256
        box[i], box[j] = box[j], box[i]
        t = (box[i] + box[j])% 256
        k = box[t]
        res.append(chr(ord(s)^k))

    cipher = "".join(res)
    #print(cipher)
    if  mode == '1':
        # 化成可视字符需要编码
        print("加密后的输出(没经过任何编码):")
        print(cipher)
        # base64的目的也是为了变成可见字符
        print("base64后的编码:")
        print(str(base64.b64encode(cipher.encode('utf-8')),'utf-8'))
    if mode == '2':
        print("解密后的密文：")
        print(cipher)


def get_mode():
    print("请选择加密或者解密")
    print("1. Encrypt")
    print("2. Decode")
    mode = input()
    if mode == '1':
        message = get_message()
        key = get_key()
        box = init_box(key)
        ex_encrypt(message,box,mode)
    elif mode == '2':
        message = get_message()
        key = get_key()
        box = init_box(key)
        ex_encrypt(message, box, mode)
    else:
        print("输入有误！")





if __name__ == '__main__':
    while True:
        get_mode()

