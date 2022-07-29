# coding:utf-8
# 引入fastapi
from dataclasses import replace
import uvicorn
from fastapi import FastAPI, Response
# 引入文件
from fastapi.middleware.cors import CORSMiddleware
# HTMLResponse
from fastapi.responses import HTMLResponse
import json
import os

# 创建FastAPI实例
app = FastAPI()

# cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 读取文件
def read_file(file_name):
    root_dir = './public/'
    with open(os.path.join(root_dir, file_name), 'r', encoding='utf-8') as f:
        return f.read()


@app.get("/")
def index():
    init_data = json.loads(read_file("data/page1.json"))
    html_data = read_file('index.html')
    replace_data = ""
    for i in init_data:
        replace_data += "<li>" + str(i["id"]) + "</li>"
    html_data = html_data.replace("{{page1}}", '<ul id="xxx">' + replace_data + '</ul>')
    # 返回 index.html
    return HTMLResponse(html_data)


# 返回 2.js
@app.get("/2.js")
def index2():
    # 返回 2.js
    return Response(content=read_file("2.js"), media_type="text/javascript;charset=UTF-8")


# 返回3.html
@app.get("/3.htm")
def index3():
    # 返回 3.html
    return HTMLResponse(read_file('3.html'))


# 返回4.xml
@app.get("/4.xml")
def index4():
    # 返回 4.xml
    return Response(content=read_file('4.xml'), media_type="application/xml;charset=UTF-8")


# 返回5.json
@app.get("/5.json")
def index5():
    # 返回 5.json
    return json.loads(read_file('5.json'))


# 返回style.css
@app.get("/style.css")
def index6():
    # 返回 style.css
    return Response(content=read_file('style.css'), media_type="text/css;charset=UTF-8")


# 返回main.js
@app.get("/main.js")
def index7():
    # 返回 main.js
    return Response(content=read_file('main.js'), media_type="text/javascript;charset=UTF-8")


# 返回data/page1.json
@app.get("/page1")
def index8():
    # 返回 data/page1.json
    return json.loads(read_file('data/page1.json'))


# 返回data/page2.json
@app.get("/page2")
def index9():
    # 返回 data/page2.json
    return json.loads(read_file('data/page2.json'))


# 返回data/page3.json
@app.get("/page3")
def index10():
    # 返回 data/page3.json
    return json.loads(read_file('data/page3.json'))

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)