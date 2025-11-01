import urllib.request as request
import json
src_chinese="https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-ch"
src_english="https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-en"


# hotel_dic = {
#    216: {"旅宿名稱": "帛堯初見輕旅", "地址": "臺北市信義區松壽路2號","電話或手機號碼": "02-25863161","房間數": "29","hotel name": "HAMP COURT PALACE","address": "No.7, Sec. 2, Jianguo N. Rd., Zhongshan Dist., Taipei City 104, Taiwan (R.O.C.)"}}
hotel_dic={}

with request.urlopen(src_chinese) as response_chinese:
    data_chinese=json.load(response_chinese)
    for chinese_list in data_chinese["list"]:
        dic={}
        dic["旅宿名稱"]=chinese_list["旅宿名稱"]
        dic["地址"]=chinese_list["地址"]
        dic["電話或手機號碼"]=chinese_list["電話或手機號碼"]
        dic["房間數"]=chinese_list["房間數"]
        hotel_dic[chinese_list["_id"]]=dic
       

with request.urlopen(src_english) as response_english:
    data_english=json.load(response_english)
    for english_list in data_english["list"]:
        for hotel_id in hotel_dic:
         if english_list["_id"] == hotel_id:
            hotel_dic[hotel_id]["hotel name"] = english_list["hotel name"]
            hotel_dic[hotel_id]["address"] = english_list["address"]
         


with open("hotels.csv", "w", encoding="utf-8") as file:
    for hotel_id in hotel_dic:
        file.write(hotel_dic[hotel_id]["旅宿名稱"]+","+hotel_dic[hotel_id]["hotel name"]+","+hotel_dic[hotel_id]["地址"]+","+hotel_dic[hotel_id]["address"]+","+hotel_dic[hotel_id]["電話或手機號碼"]+","+hotel_dic[hotel_id]["房間數"]+"\n")



# districts.csv 


#找出所有的區放到districts_dic
districts_dic = {}
for id in hotel_dic:
    adress = hotel_dic[id]["地址"]
    part1 = adress.split("市")
    part2 = part1[1].split("區")
    district = part2[0]+"區"
    if district not in districts_dic:
        districts_dic[district] = {"HotelCount":0,"RoomCount":0}

#算出每個區的HotelCount和RoomCount
for district in districts_dic:
    HotelCount=0
    RoomCount=0
    for id in hotel_dic:
        adress = hotel_dic[id]["地址"]
        if district in adress:
            HotelCount+=1
            RoomCount+=int(hotel_dic[id]["房間數"])
    districts_dic[district]["HotelCount"] = HotelCount
    districts_dic[district]["RoomCount"] = RoomCount


with open("districts.csv", "w", encoding="utf-8") as file:
    for district in districts_dic:
        HotelCount = districts_dic[district]["HotelCount"]
        RoomCount = districts_dic[district]["RoomCount"]
        file.write(district+","+str(HotelCount)+","+str(RoomCount)+"\n")


# districts_dic = {
#      "中正區":{HotelCount:30,RoomCount:300}
# }


