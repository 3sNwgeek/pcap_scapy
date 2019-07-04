#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 14:59
# @Author  : Tisson_Lab
# @File    : run_pcap.py
# @Software: PyCharm
import datetime
from scapy.all import *
import os
from output_to_excel import write_all_data
from base_on_agreement_type import *
from base_on_content import *
from base_on_ip import *
try:
    import scapy_http.http
except ImportError:
    from scapy.layers import http
date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")



DIR = "C:\\Users\\3s_NwGeek\\Desktop\\test"  # 存放数据的路径，需要自己配置





def main():
    output_filepath = DIR+'\\result\\' + date
    if not os.path.exists(output_filepath):
        os.makedirs(output_filepath)
    """
    检查DIR文件夹下的所有pcap文件并解析
    :return:
    """
    all_files = os.listdir(DIR)
    for file in all_files:
        if os.path.isfile(DIR + "/" + file):
            if file[file.rfind(".")+1:].startswith("pcap"):
                print(file, "Start Working.........")
                agreement = Agreement()
                ip_ = Ip_to_ip()
                content = Content()
                with PcapReader(DIR + "/" + file) as f:
                    count = 0
                    for p in f:
                        count += 1
                        try:
                            if p["Ether"].type == 34525:
                                continue
                            agreement.agreement_type(p)
                            if p.haslayer("IP"):
                                ip_.ip_to_ip(p)
                            content.content(p)
                        except:
                            continue

                # print(file, "Work Finished..........")
                # print("Start Writing........")
                # print(content.http_keywords_count)
                write_all_data(file, agreement.agreement_, ip_.ip_to_ip_count, content.emails_count, content.urls_count, content.http_keywords_count,output_filepath)
                print(file + " Is Ok !!!!!!!!!!!\n")
    print('result saved in '+output_filepath)

    # print(agreement_)
    # print(ip_to_ip_count)
    # print(emails_count)
    # print(urls_count)
    # print(http_keywords_count)


if __name__ == '__main__':
    main()
