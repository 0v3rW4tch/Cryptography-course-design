# -*- coding: utf-8 -*-
# Author:0verWatch

from pyDes import des, CBC, PAD_PKCS5
import binascii
import hashlib
import rsa

# 秘钥
KEY = 'mHAxsLYz'


def des_encrypt(s):
    """
    DES 加密
    :param s: 原始字符串
    :return: 加密后字符串，16进制
    """
    secret_key = KEY
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    en = k.encrypt(s, padmode=PAD_PKCS5)
    return binascii.b2a_hex(en)


def des_descrypt(s):
    """
    DES 解密
    :param s: 加密后的字符串，16进制
    :return:  解密后的字符串
    """
    secret_key = KEY
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
    return de

import rsa

# rsa加密
def rsaEncrypt(str):
    # 生成公钥、私钥
    (pubkey, privkey) = rsa.newkeys(512)
    print(pubkey, privkey)
    # 明文编码格式
    content = str.encode('utf-8')
    # 公钥加密
    crypto = rsa.encrypt(content, pubkey)
    return (crypto, privkey)



# rsa解密
def rsaDecrypt(str, pk):
    # 私钥解密
    content = rsa.decrypt(str, pk)
    con = content.decode('utf-8')
    return con



if __name__ == '__main__':
    print("-----Alice发送信息------")
    message = input("输入发送的信息:\n")
    salt = input("请输入防碰撞的salt:\n")
    hash = hashlib.md5((salt+message).encode("utf-8"))
    DES_word = des_encrypt(salt+message)
    print("DES加密过后的信息(16进制输出):"+DES_word.decode())
    print(hash.hexdigest())
    str1, pk = rsaEncrypt(KEY)
    print('加密后对称密钥：')
    print(str1)
    tmp = hash.hexdigest()
    RSA_sign,pk2 = rsaEncrypt(hash.hexdigest())
    print('数字签名：')
    print(RSA_sign)
    #print(pk)
    print("-----Bob接受信息--------")
    print('解密后明文：')
    DES_word2 = des_descrypt(DES_word)
    print("DES解密过后的信息:" + DES_word2[len(salt):].decode())
    hash2 = hashlib.md5(DES_word2)
    res = hash.hexdigest()== hash2.hexdigest()
    print("判断Hash是否正确:"+ str(res) )
    RSA_check = rsaDecrypt(RSA_sign, pk2)
    print("检查是否签名是否正确"+str(RSA_check == tmp))




