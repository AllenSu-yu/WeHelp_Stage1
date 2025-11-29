from unittest import result
from fastapi import FastAPI, Body, Request, Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, PlainTextResponse, HTMLResponse
from starlette.middleware.sessions import SessionMiddleware
from fastapi.templating import Jinja2Templates
import json, mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MySQL+123",
    database="website"
)
print("連線成功！")
cursor=con.cursor()


app=FastAPI()
app.add_middleware(SessionMiddleware, secret_key="dkjfaosdijf")
#設定模板目錄
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request
    })

@app.post("/signup")
async def signup(request: Request):
    body= await request.json()
    name=body["name"]
    email=body["email"]
    password=body["password"]
    cursor.execute("SELECT * FROM member WHERE email=%s", [email,])
    result=cursor.fetchone()
    if result==None:  
        cursor.execute("INSERT INTO member(name,email,password) VALUES(%s,%s,%s)", (name,email,password))
        con.commit()
        return {"ok":True}
    else:
        return {"ok":False}     



@app.post("/login")
async def login(request: Request):
    body= await request.json()
    email=body["email"]
    password=body["password"]

    cursor.execute("SELECT * FROM member WHERE email=%s AND password=%s", [email,password])
    result=cursor.fetchone()
    if result==None:
        request.session["member"]=None
        return {"ok":False}
    else:   
        member_id=result[0]
        member_name=result[1]
        member_email=result[2]
        member_password=result[3]
        request.session["member"]={
            "id":member_id,"name": member_name,"email":member_email, "password":member_password
        }
        return {"ok":True}


@app.get("/logout")
async def logout(request: Request):
        request.session["member"]=None
        return {"ok":False}

@app.get("/check_status")
async def check_status(request: Request):
        if "member" in request.session and request.session["member"]!=None:
            return {"ok":True}
        else:
            return {"ok":False}


@app.get("/member", response_class=HTMLResponse)
async def member(request:Request):
    member_data = request.session.get("member")
    member_name = member_data.get("name") if member_data else None
    member_id = member_data.get("id") if member_data else None
    cursor.execute("SELECT member.name, message.content, message.id,message.member_id FROM message join member ON message.member_id = member.id ORDER BY message.id")
    messages = cursor.fetchall()
    return templates.TemplateResponse("member.html",{
        "request":request,
        "name": member_name,
        "messages": messages,
        "login_id": member_id
    })


@app.get("/ohoh", response_class=HTMLResponse)
async def ohoh(request:Request, msg: str = Query(None)):
    return templates.TemplateResponse("fail_login.html",{
        "request":request,
        "error_message" : msg
    })

@app.post("/createMessage")
async def createMessage(request:Request):
    body = await request.json()    
    member_id=request.session["member"]["id"]
    content=body["content"]
    cursor.execute("INSERT INTO message(member_id,content) VALUES(%s,%s)", (member_id,content))
    con.commit()
    return {"ok":True}

@app.post("/deleteMessage")
async def deleteMessage(request:Request):
    body = await request.json()
    messageId=body["messageId"]
    cursor.execute("DELETE FROM message WHERE id=%s", (messageId,))
    con.commit()
    return {"ok":True}

@app.get("/api/member/{member_id}")
async def getMember(request:Request, member_id:int):
    cursor.execute("SELECT id, name, email FROM member WHERE id=%s", (member_id,))
    member_data = cursor.fetchone()
    if member_data is not None:
        inquirer_member_id = request.session["member"]["id"]
        if member_id != inquirer_member_id:
            cursor.execute("INSERT INTO queryhistory(inquirer_member_id, queried_member_id) values(%s,%s)", (inquirer_member_id,member_id))       
            con.commit()
        return {"data":{
            "id":member_data[0],
            "name":member_data[1],
            "email":member_data[2]
            }    
            }
    else:
        return {"data":None}

@app.get("/api/queryhistory")
async def queryhistory(request:Request):
    member_data = request.session.get("member")
    if member_data:
        member_id = member_data["id"]
        cursor.execute("SELECT member.name, queryhistory.inquirer_member_id, queryhistory.time FROM queryhistory JOIN member on member.id=queryhistory.inquirer_member_id WHERE queried_member_id = %s LIMIT 10", (member_id,))
        query_history = cursor.fetchall()
        result = []
        for i in query_history:
            result.append({
                "name":i[0],
                "time":i[2].isoformat() if i[2] else None
            })
        print(result)
        return result
    else:
        return {"data":None}





@app.patch("/api/member")
async def updateMember(request:Request):
    member_data= request.session.get("member")
    if member_data:
        member_id = member_data["id"]
        body = await request.json() 
        new_name = body["name"]
        if new_name: 
            cursor.execute("UPDATE member SET name=%s WHERE id=%s",(new_name, member_id))
            con.commit()
            return {"ok":True}
        else:
            return {"error":True}
    else:
        return {"error":True}







app.mount("/", StaticFiles(directory="public", html=True))

