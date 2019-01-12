# -*- coding: utf-8 -*-
# Author:0verWatch

from myRSA import *
from mymd5 import *

if __name__ == '__main__':
    print("------------------------发送人操作-------------------------")
    message = raw_input("输入发送的信息：")
    init_mess(message)
    h = hex_digest()
    mess_num4sign = mess2long(h)
    (n, e , d) = generate_key(len(str(mess_num4sign))*5)
    sign = pow(mess_num4sign, d, n)
    print(sign, message)
    print("---------------------------已发送---------------------------------")
    print("-----------------------验证一致性(接受者)---------------------------------")
    init_mess(message)
    h = hex_digest()
    print h
    sign_check = pow(sign, e, n)
    print(long2mess(sign_check))
    print("检验结果:")
    print(long2mess(sign_check) == h)




