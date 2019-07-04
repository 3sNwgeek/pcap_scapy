#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/30 14:55
# @Author  : Tisson_Lab
# @File    : output_to_excel.py
# @Software: PyCharm

"""
把结果写入excel
"""
# import datetime
import os
import xlwt


from base_on_content import Content


def write_raw(worksheet, start_col, raw_num, raw_data):
    for i, j in enumerate(raw_data, start_col):
        worksheet.write(raw_num, i, j)
    return raw_num + 1


def create_style():
    alignment = xlwt.Alignment()
    alignment.vert = xlwt.Alignment.VERT_CENTER
    style = xlwt.XFStyle()
    style.alignment = alignment
    return style


def sort_key(x):
    return x[0][0]


# def agreement_(workbook, agreement_data, n="1"):
#     """
#     解析协议类型
#     :param workbook:
#     :param agreement_data:
#     :param n:
#     :return:
#     """
#     worksheet = workbook.add_sheet('协议'+n)
#     style = create_style()
#     header = ["协议分组", "端口", "数量", "字节(b)"]
#     raw_num = 0
#     write_raw(worksheet, 0, raw_num, header)
#     if not agreement_data:
#         return
#     raw_num += 1
#     agreement_data = agreement_data.items()
#     for i, agreement in enumerate(agreement_data):
#         key = agreement[0]
#         data = agreement[1]
#         if not data:
#             raw_data = [key, "合计", 0, 0]
#             write_raw(worksheet, 0, raw_num, raw_data)
#             raw_num += 1
#         else:
#             if raw_num + len(data) > 50000:
#                 agreement_(workbook, agreement_data[i:], str(int(n)+1))
#                 break
#             data = sorted(data.items())
#             worksheet.write_merge(raw_num, raw_num + len(data) - 1, 0, 0, key, style=style)
#             num_count = 0
#             bytes_count = 0
#             for sport_data in data:
#                 num = sport_data[1][0]
#                 bytes_ = sport_data[1][1]
#                 raw_data = [sport_data[0], num, bytes_]
#                 write_raw(worksheet, 1, raw_num, raw_data)
#                 raw_num += 1
#                 num_count += num
#                 bytes_count += bytes_
#             else:
#                 raw_data = [key, "合计", num_count, bytes_count]
#                 write_raw(worksheet, 0, raw_num, raw_data)
#                 raw_num += 1

def agreement_(workbook, agreement_data, n=1):
    """
    解析协议类型
    :param workbook:
    :param agreement_data:
    :param n:
    :return:
    """
    worksheet = workbook.add_sheet('协议统计'+str(n))
    style = create_style()
    header = ["协议分组", "端口", "数量", "字节(b)"]
    raw_num = 0
    write_raw(worksheet, 0, raw_num, header)
    if not agreement_data:
        return
    raw_num += 1
    if isinstance(agreement_data, dict):
        agreement_data = agreement_data.items()
    for i, agreement in enumerate(agreement_data):
        key = agreement[0]
        data = agreement[1]
        if not data:
            raw_data = [key, "总计", 0, 0]
            write_raw(worksheet, 0, raw_num, raw_data)
            raw_num += 1
        else:
            data = sorted(data.items())
            worksheet.write_merge(raw_num, raw_num + len(data) - 1, 0, 0, key, style=style)
            num_count = 0
            bytes_count = 0
            for sport_data in data:
                num = sport_data[1][0]
                bytes_ = sport_data[1][1]
                raw_data = [sport_data[0], num, bytes_]
                write_raw(worksheet, 1, raw_num, raw_data)
                raw_num += 1
                num_count += num
                bytes_count += bytes_
            else:
                raw_data = [key, "合计", num_count, bytes_count]
                write_raw(worksheet, 0, raw_num, raw_data)
                raw_num += 1
            if raw_num > 50000:
                agreement_(workbook, list(agreement_data)[i:], n + 1)
                break

def ip_no_port(workbook, ip_to_ip_count):
    worksheet = workbook.add_sheet('端点对话统计汇总')
    header = ["源IP", "目的IP", "包数", "字节(b)"]
    raw_num = 0
    write_raw(worksheet, 0, raw_num, header)
    if not ip_to_ip_count:
        return
    raw_num += 1
    data = sorted(ip_to_ip_count.items(), key=sort_key)
    new_data = {}
    for ip_data in data:
        ip = ip_data[0][0]
        d_ip = ip_data[0][2]
        key = (ip, d_ip)
        if key not in new_data:
            new_data[key] = ip_data[1]
        else:
            new_data[key][0] += ip_data[1][0]
            new_data[key][1] += ip_data[1][1]
    for new_ip in new_data.items():
        raw_data = list(new_ip[0])
        raw_data.extend(new_ip[1])
        write_raw(worksheet, 0, raw_num, raw_data)
        raw_num += 1


# def ip_(workbook, ip_to_ip_count):
#     worksheet = workbook.add_sheet('对话具体情况')
#     style = create_style()
#     header = ["源IP", "源端口", "目的IP", "目的端口", "包数", "字节(b)"]
#     raw_num = 0
#     write_raw(worksheet, 0, raw_num, header)
#     if not ip_to_ip_count:
#         return
#     raw_num += 1
#     data = sorted(ip_to_ip_count.items(), key=sort_key)
#     key = data[0][0][0]
#     count = 0
#     num_count = 0
#     bytes_count = 0
#     for ip_data in data:
#         ip = ip_data[0][0]
#         if ip != key:
#             worksheet.write_merge(raw_num - count, raw_num - 1, 0, 0, key, style=style)
#             count = 0
#             raw_data = [key, "合计", "", "", num_count, bytes_count]
#             write_raw(worksheet, 0, raw_num, raw_data)
#             raw_num += 1
#             num_count = 0
#             bytes_count = 0
#             key = ip
#         raw_data = list(ip_data[0][1:])
#         raw_data.extend(ip_data[1])
#         write_raw(worksheet, 1, raw_num, raw_data)
#         raw_num += 1
#         count += 1
#         num_count += ip_data[1][0]
#         bytes_count += ip_data[1][1]
#     else:
#         worksheet.write_merge(raw_num - count, raw_num - 1, 0, 0, data[-1][0][0], style=style)
#         raw_data = [key, "合计", "", "", num_count, bytes_count]
#         write_raw(worksheet, 0, raw_num, raw_data)


def ip_(workbook, ip_to_ip_count, n=1):
    worksheet = workbook.add_sheet('端点对话具体情况' + str(n))
    style = create_style()
    header = ["源IP", "源端口", "目的IP", "目的端口", "包数", "字节(b)"]
    raw_num = 0
    write_raw(worksheet, 0, raw_num, header)
    if not ip_to_ip_count:
        return
    raw_num += 1
    if isinstance(ip_to_ip_count, dict):
        data = sorted(ip_to_ip_count.items(), key=sort_key)
    else:
        data = ip_to_ip_count
    key = data[0][0][0]
    count = 0
    num_count = 0
    bytes_count = 0
    for i, ip_data in enumerate(data):
        ip = ip_data[0][0]
        if ip != key:
            worksheet.write_merge(raw_num - count, raw_num - 1, 0, 0, key, style=style)
            count = 0
            raw_data = [key, "合计", "", "", num_count, bytes_count]
            write_raw(worksheet, 0, raw_num, raw_data)
            raw_num += 1
            num_count = 0
            bytes_count = 0
            key = ip
            if raw_num > 50000:
                ip_(workbook, list(data)[i:], n + 1)
                break
        raw_data = list(ip_data[0][1:])
        raw_data.extend(ip_data[1])
        write_raw(worksheet, 1, raw_num, raw_data)
        raw_num += 1
        count += 1
        num_count += ip_data[1][0]
        bytes_count += ip_data[1][1]
    else:
        worksheet.write_merge(raw_num - count, raw_num - 1, 0, 0, data[-1][0][0], style=style)
        raw_data = [key, "合计", "", "", num_count, bytes_count]
        write_raw(worksheet, 0, raw_num, raw_data)

def emails_(workbook, emails_count):

    worksheet = workbook.add_sheet('钓鱼邮箱检测分析')
    style = create_style()
    header = ["IP", "端口", "email", "数量"]
    email_total = {}
    raw_num = 0
    count = 0
    num_count = 0
    write_raw(worksheet, 0, raw_num, header)
    raw_num += 1
    if not emails_count:
        return
    all_email = sorted(emails_count.items(), key=sort_key)
    key = all_email[0][0][0]
    for email in all_email:
        ip = email[0][0]
        if ip != key:
            total = email_total.items()
            for raw_data in total:
                write_raw(worksheet, 2, raw_num, raw_data)
                raw_num += 1
                count += 1
            else:
                worksheet.write_merge(raw_num - count, raw_num - len(total) - 1, 0, 0, key, style=style)
                worksheet.write_merge(raw_num - len(total), raw_num - 1, 0, 0, key, style=style)
                worksheet.write_merge(raw_num - len(total), raw_num - 1, 1, 1, "合计", style=style)
                email_total = {}
                key = ip
                count = 0
                num_count = 0
        port = email[0][1]
        data = email[1].items()
        worksheet.write_merge(raw_num, raw_num + len(data) - 1, 1, 1, port, style=style)
        for email_data in data:
            email_ = email_data[0]
            num = email_data[1]
            if email_ in email_total:
                email_total[email_] += num
            else:
                email_total[email_] = num
            raw_data = [email_, num]
            write_raw(worksheet, 2, raw_num, raw_data)
            raw_num += 1
            count += 1
            num_count += num
    else:
        total = email_total.items()
        for raw_data in total:
            write_raw(worksheet, 2, raw_num, raw_data)
            raw_num += 1
            count += 1
        else:
            worksheet.write_merge(raw_num - count, raw_num - len(total) - 1, 0, 0, key, style=style)
            worksheet.write_merge(raw_num - len(total), raw_num - 1, 0, 0, key, style=style)
            worksheet.write_merge(raw_num - len(total), raw_num - 1, 1, 1, "合计", style=style)


def urls_(workbook, urls_count):
    worksheet = workbook.add_sheet('url检测')
    style = create_style()
    header = ["IP", "端口", "url", "数量"]
    url_total = {}
    raw_num = 0
    count = 0
    num_count = 0
    write_raw(worksheet, 0, raw_num, header)
    raw_num += 1
    if not urls_count:
        return
    all_url = sorted(urls_count.items(), key=sort_key)
    key = all_url[0][0][0]
    for url in all_url:
        ip = url[0][0]
        if ip != key:
            total = url_total.items()
            for raw_data in total:
                write_raw(worksheet, 2, raw_num, raw_data)
                raw_num += 1
                count += 1
            else:
                worksheet.write_merge(raw_num - count, raw_num - len(total) - 1, 0, 0, key, style=style)
                worksheet.write_merge(raw_num - len(total), raw_num - 1, 0, 0, key, style=style)
                worksheet.write_merge(raw_num - len(total), raw_num - 1, 1, 1, "合计", style=style)
                url_total = {}
                key = ip
                count = 0
                num_count = 0
        port = url[0][1]
        data = url[1].items()
        worksheet.write_merge(raw_num, raw_num + len(data) - 1, 1, 1, port, style=style)
        for url_data in data:
            url_ = url_data[0]
            yuming = url_data[0].split('/')[2]
            num = url_data[1]
            if yuming in url_total:
                url_total[yuming] += num
            else:
                url_total[yuming] = num
            raw_data = [url_, num]
            write_raw(worksheet, 2, raw_num, raw_data)
            raw_num += 1
            count += 1
            num_count += num
    else:
        total = url_total.items()
        for raw_data in total:
            write_raw(worksheet, 2, raw_num, raw_data)
            raw_num += 1
            count += 1
        else:
            worksheet.write_merge(raw_num - count, raw_num - len(total) - 1, 0, 0, key, style=style)
            worksheet.write_merge(raw_num - len(total), raw_num - 1, 0, 0, key, style=style)
            worksheet.write_merge(raw_num - len(total), raw_num - 1, 1, 1, "合计", style=style)


def http_keywords(workbook, http_keywords_count):
    worksheet = workbook.add_sheet('攻击特征值检测')
    style = create_style()
    c = Content()
    header = ["IP", "端口"]
    header.extend(c.http_keywords)
    raw_num = 0
    count = 0
    key_words_count = {
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
    write_raw(worksheet, 0, raw_num, header)
    if not http_keywords_count:
        return
    raw_num += 1
    all_data = sorted(http_keywords_count.items(), key=sort_key)
    key = all_data[0][0][0]
    for data in all_data:
        ip = data[0][0]
        key_words = data[1]
        if ip != key:
            worksheet.write_merge(raw_num - count, raw_num - 1, 0, 0, key, style=style)
            key = ip
            count = 0
            raw_data = ["合计"]
            raw_data.extend(key_words_count.values())
            write_raw(worksheet, 1, raw_num, raw_data)
            raw_num += 1
            key_words_count = {
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
        port = data[0][1]
        raw_data = [port]
        for key_word, value in key_words.items():
            raw_data.append(value)
            key_words_count[key_word] += value
        write_raw(worksheet, 1, raw_num, raw_data)
        raw_num += 1
        count += 1
    else:
        worksheet.write_merge(raw_num - count, raw_num - 1, 0, 0, all_data[-1][0][0], style=style)
        raw_data = ["合计"]
        raw_data.extend(key_words_count.values())
        write_raw(worksheet, 1, raw_num, raw_data)
        raw_num += 1


def write_all_data(file, agreement_data, ip_to_ip_count, emails_count, urls_count, http_keywords_count,output_filepath):
    workbook = xlwt.Workbook(encoding='utf-8')
    agreement_(workbook, agreement_data)
    ip_no_port(workbook, ip_to_ip_count)
    ip_(workbook, ip_to_ip_count)
    emails_(workbook, emails_count)
    urls_(workbook, urls_count)
    http_keywords(workbook, http_keywords_count)
    # date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # if not os.path.exists(DIR+'/result/' + date):
    #     os.makedirs(DIR+'/result/' + date)
    workbook.save(output_filepath + '/' + file[:file.rfind(".")] + '.xls')

