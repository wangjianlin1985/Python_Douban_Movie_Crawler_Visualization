import sqlite3

import pymysql

def get_loan_number():
    con = sqlite3.connect("movie.db")
    cursor = con.cursor()
    print("---读取数据---")
    sql = "select cname,year_release  from movie250"
    cursor.execute(sql)  # 用于执行返回多个结果集、多个更新计数或二者组合的语句。
    number = cursor.fetchall()  # 返回多个元组，即返回多个记录(rows),如果没有结果 则返回 ()
    temp_data = []
    loan_count = 0
    for loanNumber in number:
        loan_count += 1
        temp_data.append(loanNumber)
    data11 = dict(temp_data)
    # print(data11)
    cursor.close()
    con.close()
    print("读取完成,共有%d条数据……" % loan_count)
    return data11


def get_country_static():
    con = sqlite3.connect("movie.db")
    cursor = con.cursor()
    print("---读取数据---")
    sql = "select country,count(*) as num from movie250 group by country order by num desc"
    cursor.execute(sql)  # 用于执行返回多个结果集、多个更新计数或二者组合的语句。
    rs = cursor.fetchall()  # 返回多个元组，即返回多个记录(rows),如果没有结果 则返回 ()
    temp_data = []
    loan_count = 0
    for item in rs:
        temp_data.append(item)
    temp_data = temp_data[0:15]
    data11 = dict(temp_data)
    # print(data11)
    cursor.close()
    con.close()
    print("读取完成,共有%d条数据……" % loan_count)
    return data11
