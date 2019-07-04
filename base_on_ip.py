#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/30 11:09
# @Author  : Tisson_Lab
# @File    : base_on_ip.py
# @Software: PyCharm
"""
解析ip类
"""

class Ip_to_ip(object):
    def __init__(self):
        self.ip_to_ip_count = {}


    def ip_to_ip(self, p):
        """
        基于IP统计各ip和端口之间的访问次数
        :param p:
        :return:
        """
        try:
            sport = p.sport
        except AttributeError:
            sport = 1

        try:
            dport = p.dport
        except AttributeError:
            dport = 1

        src = p["IP"].src
        dst = p["IP"].dst
        key_ip = (src, sport, dst, dport)
        if key_ip in self.ip_to_ip_count:
            self.ip_to_ip_count[key_ip][0] += 1
            self.ip_to_ip_count[key_ip][1] += p["IP"].len
        else:
            self.ip_to_ip_count[key_ip] = [1, p["IP"].len]
