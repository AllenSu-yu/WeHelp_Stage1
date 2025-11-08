import urllib.request as request
import json
src_chinese="https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-ch"
src_english="https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-en"



hotel_dic={}

with request.urlopen(src_chinese) as response_chinese:
    data_chinese=json.load(response_chinese)
    for chinese_list in data_chinese["list"]:
        dic={}
        dic["旅宿名稱"]=chinese_list["旅宿名稱"]
        dic["電話或手機號碼"]=chinese_list["電話或手機號碼"]
        hotel_dic[chinese_list["_id"]]=dic



with request.urlopen(src_english) as response_english:
    data_english=json.load(response_english)
    for english_list in data_english["list"]:
        for hotel_id in hotel_dic:
         if english_list["_id"] == hotel_id:
            hotel_dic[hotel_id]["hotel name"] = english_list["hotel name"]


def hotel_data(id):
    id = int(id)
    if id not in hotel_dic:
        return "查詢不到相關資料"
    hotel = hotel_dic[id]
    result = hotel["旅宿名稱"]+"、"+hotel["hotel name"]+"、"+hotel["電話或手機號碼"]
    return result



