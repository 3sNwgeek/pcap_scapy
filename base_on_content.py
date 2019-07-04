#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/30 11:11
# @Author  : Tisson_Lab
# @File    : base_on_content.py
# @Software: PyCharm

"""
解析url, 邮箱, 关键字的类
"""

from get_sth_by_re import get_findall_emails, get_findall_urls


class Content(object):
    def __init__(self):
        self.emails_count = {}
        self.urls_count = {}
        self.http_keywords = ["eval", "z0", "system", "select", "union", "ipconfig", "ifconfig", "whoami", "base64", "system(", "shell", 'int_set("display_errors","0")']  # 可修改关键字， 但是需要同步修改下面的http_keywords_count的内容
        self.http_keywords_count = {
        }

    def content(self, p):
        """
        基于内容添加邮箱和url
        :param p:
        :return:
        """
        try:
            text = p.load
        except AttributeError:
            return
        try:
            sport = p.sport
        except AttributeError:
            sport = 1
        src = p["IP"].src
        text = text.decode("utf-8", "ignore")
        emails = get_findall_emails(text)
        key = (src, sport)
        for email in emails:
            if key in self.emails_count:
                if email in self.emails_count[key]:
                    self.emails_count[key][email] += 1
                else:
                    self.emails_count[key][email] = 1
            else:
                self.emails_count[key] = {email: 1}
        urls = get_findall_urls(text)
        for url in urls:
            if url.count('.') < 2:
                continue
            if key in self.urls_count:
                if url in self.urls_count[key]:
                    self.urls_count[key][url] += 1
                else:
                    self.urls_count[key][url] = 1
            else:
                self.urls_count[key] = {url: 1}
        # 基于内容统计关键字次数
        if p.haslayer("HTTP"):
            for keyword in self.http_keywords:
                if keyword in text:
                    if key in self.http_keywords_count:
                        self.http_keywords_count[key][keyword] += 1
                    else:
                        self.http_keywords_count[key] = {
                            "eval": 0,
                            "z0": 0,
                            "system": 0,
                            "select": 0,
                            "union": 0,
                            "ipconfig": 0,
                            "ifconfig": 0,
                            "whoami": 0,
                            "base64": 0,
                            "system(": 0,
                            "shell": 0,
                            'int_set("display_errors","0")': 0
                        }
                        self.http_keywords_count[key][keyword] += 1

