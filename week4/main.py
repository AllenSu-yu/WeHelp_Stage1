from fastapi import FastAPI, Body, Request, Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, PlainTextResponse
from starlette.middleware.sessions import SessionMiddleware
import json
import hotel
app=FastAPI()
app.add_middleware(SessionMiddleware, secret_key="dkjfaosdijf")

account ={"email":"abc@abc.com", "password":"abc"}

@app.post("/login")
async def login(request: Request):
    body= await request.json()
    email=body["email"]
    password=body["password"]
    if account["email"] == email and account["password"] == password:
        request.session["member"]={
            "email":account["email"], "password":account["password"]
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


@app.get("/member")
async def member():
    return FileResponse("public/member.html")


@app.get("/ohoh")
async def ohoh(msg: str = Query(None)):
    if msg == "信箱或密碼輸⼊錯誤":
        return FileResponse("public/fail_login.html")
    elif msg == "請輸⼊信箱和密碼":
        return FileResponse("public/fail_login_empty.html")
    else:
        # 預設情況或其他錯誤訊息
        return FileResponse("public/fail_login.html")

@app.get("/hotel/{number}")
async def hotel_page(number):
    return FileResponse("public/hotel.html")

@app.get("/hotel/data/{number}")
async def get_hotel(number):
    result = hotel.hotel_data(number)
    return PlainTextResponse(result)

app.mount("/", StaticFiles(directory="public", html=True))

