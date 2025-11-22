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
    cursor.execute("SELECT * FROM member")
    members=cursor.fetchall()
    body= await request.json()
    name=body["name"]
    email=body["email"]
    password=body["password"]
    for member in members:
        member_email=member[2]
        if member_email == email:
            return {"ok":False}
        
    cursor.execute("INSERT INTO member(name,email,password) VALUES(%s,%s,%s)", (name,email,password))
    con.commit()
    return {"ok":True}     



@app.post("/login")
async def login(request: Request):
    cursor.execute("SELECT * FROM member")
    members=cursor.fetchall()
    body= await request.json()
    email=body["email"]
    password=body["password"]
    for member in members:
        member_id=member[0]
        member_name=member[1]
        member_email=member[2]
        member_password=member[3]
        if member_email == email and member_password == password:
            request.session["member"]={
                "id":member_id,"name": member_name,"email":member_email, "password":member_password
            }
            return {"ok":True}
    else:
        request.session["member"]=None
        return {"ok":False}

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



app.mount("/", StaticFiles(directory="public", html=True))

