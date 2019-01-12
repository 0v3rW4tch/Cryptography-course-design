# -*- coding: utf-8 -*-
# Author:0verWatch

def get_key():
    key = 0
    print("输入秘钥数字")
    key = int(input()) % 26
    return key

def get_message():
    print("你的信息")
    message = input()
    return message

def Encryption(message, key):
    encryption = ""
    for i in message:
        if i.isalpha():
            temp = ord(i) + key
            if i.isupper():
                if temp > ord('Z'):
                    temp = temp - 26
                elif temp < ord('A'):
                    temp = temp + 26
            if i.islower():
                if temp > ord('z'):
                    temp = temp - 26
                elif temp < ord('a'):
                    temp = temp + 26
            encryption += chr(temp)
        else:
            encryption += i
    return encryption

def Decryption(message,key):
    key = -key
    decryption = ""
    for i in message:
        if i.isalpha():
            temp = ord(i)+ key
            if i.isupper():
                if temp > ord('Z'):
                    temp -= 26
                elif temp < ord('A'):
                    temp += 26
            if i.islower():
                if temp > ord('z'):
                    temp -= 26
                if temp < ord('a'):
                    temp += 26
            decryption += chr(temp)
        else:
            decryption += i
    return decryption


def Getmode():
    while True:
        print("请选择加密或解密模式，也可以选择暴力破解")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Brute")
        choice = input("Your choice")
        if choice == '1':
            message = get_message()
            key = get_key()
            print(Encryption(message,key))
        if choice == '2':
            message = get_message()
            key = get_key()
            print(Decryption(message,key))
        if choice == '3':
            message = get_message()
            for j in range(0,25):
                print(Decryption(message, j))



if __name__ == '__main__':
    Getmode()
