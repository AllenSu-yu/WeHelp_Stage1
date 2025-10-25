# Task1

def func1(name):
    characters = {
        "悟空":{"x":0, "y":0, "z":0},
        "特南克斯":{"x":1, "y":-2, "z":0},
        "辛巴":{"x":-3, "y":3, "z":0},
        "貝吉塔":{"x":-4, "y":-1, "z":0},
        "丁滿":{"x":-1, "y":4, "z":1},
        "弗利沙":{"x":4, "y":-1, "z":1}
    }
    distance_list = [] #建立一個list放置計算完後所有人的距離
    for person, site  in characters.items():
        if site["z"] == characters[name]["z"]: #跟自己同一邊距離加上0，跟自己不同邊距離加上2
            z1 = 0
        else:
            z1 = 2
        distance = (abs(characters[name]["x"]-site["x"]) + abs(characters[name]["y"] -site["y"]) + z1) #算出所有人的距離        
        distance_list.append(distance) #將所有人的距離放進list        
        characters[person]["distance"] = distance #一個新的字典加上所有人的距離

    # 找到最遠和最近的距離
    distance_list.remove(0)   #移除自己 
    max_distance = max(distance_list) #找到最遠的距離
    min_distance = min(distance_list) #找到最近的距離
    
    # 建立兩個list分別放入距離最遠和最近的兩個人
    far_person_list = []
    near_person_list = []
    for person, site in characters.items():
        if site["distance"] ==max_distance:
            far_person_list.append(person)
        elif site["distance"] ==min_distance:
            near_person_list.append(person)
    
    # 將list裡面的人名組裝好
    far_person = "、".join(far_person_list)
    near_person = "、".join(near_person_list)
    
    print(f"最遠{far_person}；最近{near_person}")


func1("辛巴")
func1("悟空")
func1("弗利沙")
func1("特南克斯")

print("--------")

# Task2 ------------------------------------------------------------------------------------
import re

s1_service = []
s2_service = []
s3_service = []

# 找到符合C數字條件的服務名稱
def find_c_service(match):
    c_list = [800,1000,1200]
    c_list_reverse = [1200,1000,800]
    c_number_list = []
    service_list = []
    # 找到符合標準的數字C
    if match.group(1) == "c":
        if match.group(2) == ">=":
            for c_number in c_list:
                if c_number >= int(match.group(3)):
                    c_number_list.append(c_number)
        elif match.group(2) == "<=":
            for c_number in c_list_reverse:
                if c_number <= int(match.group(3)):
                    c_number_list.append(c_number)              
    #將數字C換成服務名稱
    for i in range(len(c_number_list)):
        if c_number_list[i] == 1000:
            service_list.append("S1")
        elif c_number_list[i] == 1200:
            service_list.append("S2")
        elif c_number_list[i] == 800:
            service_list.append("S3")
    return service_list



#找到符合r數字條件的服務名稱
def find_r_service(match):
    r_list = [3,3.8,4.5]
    r_list_reverse = [4.5,3.8,3]
    r_number_list = []
    service_list = []
    if match.group(1) == "r":
        if match.group(2) == ">=":
            for r_number in r_list:
                if r_number >= float(match.group(3)):
                    r_number_list.append(r_number)
        elif match.group(2) == "<=":
            for r_number in r_list_reverse:
                if r_number <= float(match.group(3)):
                    r_number_list.append(r_number)
    #將數字r換成服務名稱
    for i in range(len(r_number_list)):
        if r_number_list[i] == 4.5:
            service_list.append("S1")
        elif r_number_list[i] == 3:
            service_list.append("S2")
        elif r_number_list[i] == 3.8:
            service_list.append("S3")
    return service_list





# 將使用者想要booking的時段全部存入list(booking_time)回傳
def booking_time(start,end):
    booking_time = []
    time_range = end-start+1
    time = start
    for i in range(time_range):
            booking_time.append(time)
            time+=1
    return booking_time



# 開始booking
def booking(match, start,end):
    # 先判斷Criteria是 c、r or name
    if match.group(1) == "c":
        service_list = find_c_service(match)
    elif match.group(1) == "r":
        service_list = find_r_service(match)
    elif match.group(1) == "name":
        service_list = [match.group(3)]

    
    start_booking_time = booking_time(start,end)
    for service in service_list:
        # 確認符合條件的服務
        if service == "S1":
            # 確認時間是否有衝突
            available_s1_check = True
            for time in start_booking_time:
                if time in s1_service:
                    available_s1_check = False
            # 時間可以時，開始booking時間
            if available_s1_check:
                for time in start_booking_time:
                    s1_service.append(time)                
                return "S1"
        elif service == "S2":
            available_s2_check = True
            for time in start_booking_time:
                if time in s2_service:
                    available_s2_check = False
            if available_s2_check:
                for time in start_booking_time:
                    s2_service.append(time)                
                return "S2"
        elif service == "S3":
            available_s3_check = True
            for time in start_booking_time:
                if time in s3_service:
                    available_s3_check = False
            if available_s3_check:
                for time in start_booking_time:
                    s3_service.append(time)                
                return "S3"
    #三個服務都不行時，回傳Sorry
    return "Sorry"  
                         




def func2(ss, start, end, criteria):
    #將criteria解析成1.目標c r name 2.運算符號><= 3. 數字 or 服務名稱S1 S2 S3 
    match = re.match(r'(\w+)([><=]+)([\d.]+|\w+)', criteria)
    result = booking(match, start, end)
    print(result)



services=[
    {"name":"S1", "r":4.5, "c":1000},
    {"name":"S2", "r":3, "c":1200},
    {"name":"S3", "r":3.8, "c":800}
]



func2(services, 15, 24, "c>=800")  # S3 
func2(services, 11, 13, "r<=4")  # S3 
func2(services, 10, 12, "name=S3")  # Sorry 
func2(services, 15, 18, "r>=4.5")  # S1 
func2(services, 16, 18, "r>=4")  # Sorry 
func2(services, 13, 17, "name=S1")  # Sorry 
func2(services, 8, 9, "c<=1500")  # S2 
func2(services, 8, 9, "c<=1500") #S1

print("--------")

# Task3 ------------------------------------------------------------------------------------

def func3(index): 
    number = 25
    numbers = []
    for i in range(index):
        if i%4 == 0:
            number = number-2
            numbers.append(number)
        elif i%4 == 1:
            number = number-3
            numbers.append(number)
        elif i%4 == 2:
            number = number+1
            numbers.append(number)
        elif i%4 == 3:
            number = number+2
            numbers.append(number)
    numbers.insert(0,25)


    result = numbers[index]
    print(result)
 
 

func3(1)  # print 23 
func3(5)  # print 21 
func3(10)  # print 16 
func3(30)  # print 6 

print("--------")

# Task4 ------------------------------------------------------------------------------------

def func4(sp, stat, n): 
    # 找到不可以載客的車廂index
    unavalable_index_list = [] 
    index = 0
    for i in stat:
        if i == "1":
            unavalable_index_list.append(index)
            index+=1
        else:
            index+=1

    #把不能載客的車廂index的載客量變成1萬
    for i in unavalable_index_list:
        sp[i]=10000

    # 計算車廂載客量和乘客數量的差距
    difference_list = []
    for i in sp:
        difference_list.append(abs(i-n)) 
    
    #印出差異最小的index
    min_index = difference_list.index(min(difference_list))
    print(min_index)




func4([3, 1, 5, 4, 3, 2], "101000", 2)  # print 5 
func4([1, 0, 5, 1, 3], "10100", 4)  # print 4 
func4([4, 6, 5, 8], "1000", 4)  # print 2 






