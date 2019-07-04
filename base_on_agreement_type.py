#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/30 11:06
# @Author  : Tisson_Lab
# @File    : base_on_self.agreement_type.py
# @Software: PyCharm
# 基于协议类型
"""
解析协议类型的类
"""


class Agreement(object):
    def __init__(self):
        self.agreement_ = {
            "HTTP": {},
            "TCP": {},
            "POP": {},
            "SMB": {},
            "SSH": {},
            "FTP": {},
            "DNS": {},
            "SMTP": {},
            "ICMP": {},
        }
        self.type_ = {
            "smb": (139, 138),
            "ftp": 21,
            "ssh": 22,
            "smtp": 25,
            "pop": 110
        }
    
    def agreement_type(self, p):
        """
        统计各协议类型的请求数量
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
        if p.haslayer("HTTP"):
            if sport in self.agreement_["HTTP"]:
                self.agreement_["HTTP"][sport][0] += 1
                self.agreement_["HTTP"][sport][1] += p.len
            else:
                self.agreement_["HTTP"][sport] = [1, p.len]

        if p.haslayer("TCP"):
            if sport in self.agreement_["TCP"]:
                self.agreement_["TCP"][sport][0] += 1
                self.agreement_["TCP"][sport][1] += p.len
            else:
                self.agreement_["TCP"][sport] = [1, p.len]
        if p.haslayer("ICMP"):
            if sport in self.agreement_["ICMP"]:
                self.agreement_["ICMP"][sport][0] += 1
                self.agreement_["ICMP"][sport][1] += p.len
            else:
                self.agreement_["ICMP"][sport] = [1, p.len]
        if sport == 110 or dport == 110:
            if sport in self.agreement_["POP"]:
                self.agreement_["POP"][sport][0] += 1
                self.agreement_["POP"][sport][1] += p.len
            else:
                self.agreement_["POP"][sport] = [1, p.len]
        if sport == 139 or dport == 139 or sport == 138:
            if sport in self.agreement_["SMB"]:
                self.agreement_["SMB"][sport][0] += 1
                self.agreement_["SMB"][sport][1] += p.len
            else:
                self.agreement_["SMB"][sport] = [1, p.len]
        if sport == 22 or dport == 22:
            if sport in self.agreement_["SSH"]:
                self.agreement_["SSH"][sport][0] += 1
                self.agreement_["SSH"][sport][1] += p.len
            else:
                self.agreement_["SSH"][sport] = [1, p.len]
        if p.sport == 21 or dport == 21:
            if sport in self.agreement_["FTP"]:
                self.agreement_["FTP"][sport][0] += 1
                self.agreement_["FTP"][sport][1] += p.len
            else:
                self.agreement_["FTP"][sport] = [1, p.len]
        if p.haslayer("DNS"):
            if sport in self.agreement_["DNS"]:
                self.agreement_["DNS"][sport][0] += 1
                self.agreement_["DNS"][sport][1] += p.len
            else:
                self.agreement_["DNS"][sport] = [1, p.len]
        if sport == 25 or dport == 25:
            if sport in self.agreement_["SMTP"]:
                self.agreement_["SMTP"][sport][0] += 1
                self.agreement_["SMTP"][sport][1] += p.len
            else:
                self.agreement_["SMTP"][sport] = [1, p.len]
