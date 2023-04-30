from flask import Flask,render_template
import sqlite3
import json

from data import get_loan_number,get_country_static

app = Flask(__name__)

# #时间分布 定义视图处理函数加载到App中（路由+视图函数）
@app.route('/time') # 访问路由
def time(): # 绑定的视图函数
    temp_data = get_loan_number()
    return render_template('time.html',map_data=temp_data)

#国家分布
@app.route('/world') # 访问路由
def world(): # 绑定的视图函数
    temp_data = get_country_static()
    return render_template('world.html',map_data=temp_data)



@app.route('/')
def index():
    return render_template("index.html")

#进入首页
@app.route('/index')
def home():
    #return render_template("index.html")
    return index()

#电影记录查询
@app.route('/movie')
def movie():
    datalist  = []
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select * from movie250"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()
    # print(datalist)
    return render_template("movie.html",movies = datalist)


#评分
@app.route('/score')
def score():
    score = []  # 评分
    num = []    # 每个评分所统计出的电影数量
    score2 = []  # 评分
    num2 = []  # 每个评分所统计出的电影数量
    res={}
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select score,count(score) from movie250 group by score"
    data = cur.execute(sql)
    for item in data:
        score.append(str(item[0]))
        num.append(item[1])
    for k, v in zip(score, num):
        res.update({k: v, },)

    sql2="select year_release,count(year_release) from movie250 group by year_release"
    data2 = cur.execute(sql2)
    for item2 in data2:
        score2.append(str(item2[0]))
        num2.append(item2[1])

    #print(num2)
    cur.close()
    con.close()
    return render_template("score.html",score=score,num=num,res=res,num2=num2,score2=score2)
    # return render_template("testshanxing.html",score=score,num=num,res=res,num2=num2,score2=score2)

#词云
@app.route('/word')
def word():
    return render_template("cloud.html")


@app.route('/team')
def team():
    return render_template("team.html")

@app.route('/aboutMe')
def aboutMe():
    return render_template("aboutMe.html")

def combine(keys,values):
    res=[]
    if len(keys)!=len(values):
        return None
    for ind,key in enumerate(keys):
        dict_temp={}

        dict_temp[key]=values[ind]
        res.append(dict_temp)
    return res

def mycombine(key,value):
    data = {}
    # keys与values分别为该数据的键数组，值的数组。这里循环为字典添加对应键值
    for k, v in zip(key, value):
        data.update({k: v, }, )
    # 最后将数据打包成json格式以字典的方式传送到前端
    # return render(request, 'index.html', {'data': json.dumps(data)})
    return data

if __name__ == '__main__':
    app.run()
