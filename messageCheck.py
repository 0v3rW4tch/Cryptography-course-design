# -*- coding: utf-8 -*-
# Author:0verWatch

from mymd5 import *


if __name__ == '__main__':
    print("---------发送人发送消息------------")
    message4check = raw_input("请输入你要发送的信息:")
    init_mess(message4check)
    out_put = hex_digest()
    print("发送消息+消息验证码")
    print(message4check,out_put)
    print("----------接收方接受信息并检测消息验证码------------")
    print("接收的信息"+message4check)
    init_mess(message4check)
    out_put_check = hex_digest()
    print(out_put == out_put_check)