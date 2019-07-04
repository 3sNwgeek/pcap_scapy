#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/30 9:10
# @Author  : Tisson_Lab
# @File    : get_sth_by_re.py
# @Software: PyCharm


import re

def get_findall_urls(text):
    """
    :param text: 文本
    :return: 返回url列表
    """
    urls = re.findall(r"http[s]?://[0-9a-zA-Z\.\/\:\_\?&\-\~\!\*\;\=\+\$\,\#\(\)@\[\]]+", text)
    return urls


def get_findall_emails(text):
    """
    :param text: 文 本
    :return: 返回电子邮件列表
    """
    emails = re.findall(r"[a-zA-Z0-9\.\-+_]+@[a-zA-Z0-9\.\-+_]+\.[a-z]+", text)
    return emails


if __name__ == '__main__':
    print(get_findall_urls("http://118.194.196.232:8090/webmail/login9.php"))
    print(get_findall_emails("123456789@qq.com"))
