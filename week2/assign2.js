// Task1

function func1(name){ 
    const characters = {
        "悟空":{"x":0, "y":0, "z":0},
        "特南克斯":{"x":1, "y":-2, "z":0},
        "辛巴":{"x":-3, "y":3, "z":0},
        "貝吉塔":{"x":-4, "y":-1, "z":0},
        "丁滿":{"x":-1, "y":4, "z":1},
        "弗利沙":{"x":4, "y":-1, "z":1}
    }
    
    const distance_list = []
    for (let key in characters) {
        let z1 = 0
        if (characters[key]["z"] == characters[name]["z"]){
            z1 = 0;
        } else if (characters[key]["z"] !== characters[name]["z"]){
            z1 = 2;
        } 
        let distance = Math.abs(characters[key]["x"] - characters[name]["x"])+ Math.abs(characters[key]["y"] - characters[name]["y"] ) + z1
        characters[key]["distance"]= distance
        distance_list.push(distance)
    }

    const new_distance_list = distance_list.filter(item => item !== 0)
    const min = Math.min(...new_distance_list)
    const max = Math.max(...new_distance_list)

    const min_character_list = []
    const max_character_list = []
    for (let key in characters){
        if (characters[key]["distance"] == min){
            min_character_list.push(key);
        } else if (characters[key]["distance"] == max){
            max_character_list.push(key);
        } 

    } 
    
   const min_character = min_character_list.join("、")
   const max_character = max_character_list.join("、")
    
    
    
    console.log("最遠"+ max_character, "；最近"+min_character)

    } 

func1("辛巴")
func1("悟空")
func1("弗利沙")
func1("特南克斯")

console.log("--------")

// Task2 ------------------------------------------------------------------------------------

const s1_service = []
const s2_service = []
const s3_service = []


// 找到符合C數字條件的服務名稱
function find_c_service(variable, operator, value) {
    const c_list = [800,1000,1200]
    const c_list_reverse = [1200,1000,800]
    const c_number_list = []
    const service_list = []

    // 找到符合標準的數字C
    if (variable === "c"){
        if (operator === ">="){
            for (let c_number of c_list){
                if (c_number >= parseInt(value)){
                    c_number_list.push(c_number)
                }
            }        
        }
        else if (operator == "<="){
            for (let c_number of c_list_reverse){
                if (c_number <= parseInt(value)){
                    c_number_list.push(c_number)
                }
            }
        }              
    }
    
    // 將數字C換成服務名稱
    for (let i = 0; i< c_number_list.length;i++){
        if (c_number_list[i] == 1000){
            service_list.push("S1")
        }
        else if (c_number_list[i] == 1200){
            service_list.push("S2")
        }
        else if (c_number_list[i] == 800){
            service_list.push("S3")
        }
    }
    return service_list

}

// 找到符合r數字條件的服務名稱
function find_r_service(variable, operator, value){
    const r_list = [3,3.8,4.5]
    const r_list_reverse = [4.5,3.8,3]
    const r_number_list = []
    const service_list = []
    if (variable == "r"){
        if (operator == ">="){
            for (let r_number of r_list){
                if (r_number >= parseFloat(value)){
                    r_number_list.push(r_number)
                }
            }
        }
        else if (operator == "<="){
            for (let r_number of r_list_reverse){
                if (r_number <= parseFloat(value)){
                    r_number_list.push(r_number)
                }
            }
        }
    }

  
    // 將數字r換成服務名稱
    for (let i=0; i< r_number_list.length; i++){
        if (r_number_list[i] == 4.5){
            service_list.push("S1")
        }
        else if (r_number_list[i] == 3){
            service_list.push("S2")
        }
        else if (r_number_list[i] == 3.8){
            service_list.push("S3")
        }
    }
    return service_list
}



// 將使用者想要booking的時段全部存入list(booking_time)回傳
function booking_time(start,end){
    const booking_time = []
    let time_range = end-start+1
    let time = start
    for (let i=0; i<time_range; i++){
            booking_time.push(time)
            time+=1
    }
    return booking_time
}



// 開始booking
function booking(start,end, variable, operator, value){
    // 先判斷Criteria是 c、r or name
    let service_list = []
    if (variable == "c"){
        service_list = find_c_service(variable, operator, value)
    } else if (variable == "r"){
        service_list = find_r_service(variable, operator, value)
    } else if (variable == "name"){
        service_list = [value]
    }

    
    let start_booking_time = booking_time(start,end)
    for (let service of service_list){
        // 確認符合條件的服務
        if (service == "S1"){
            // 確認時間是否有衝突
            let available_s1_check = true;
            for (let time of start_booking_time){
                if (s1_service.includes(time)){
                    available_s1_check = false;
                }
            }
            // 時間可以時，開始booking時間
            if (available_s1_check){
                for (let time of start_booking_time){
                    s1_service.push(time)
                }                
                return "S1"

            }
        } else if (service == "S2"){
            let available_s2_check = true;
            for (let time of start_booking_time){
                if (s2_service.includes(time)){
                    available_s2_check = false;
                }
            }
            if (available_s2_check){
                for (let time of start_booking_time){
                    s2_service.push(time) 
                }               
                return "S2"
            }
        } else if (service == "S3"){
            let available_s3_check = true;
            for (let time of start_booking_time){
                if (s3_service.includes(time)){
                    available_s3_check = false;
                }
            }
            if (available_s3_check){
                for (let time of start_booking_time){
                    s3_service.push(time)  
                }              
                return "S3"
            }
        }
    }
    // 三個服務都不行時，回傳Sorry
    return "Sorry"
}  




function func2(ss, start, end, criteria){ 
    // 將criteria解析成1.目標c r name 2.運算符號><= 3. 數字 or 服務名稱S1 S2 S3 
    const match = criteria.match(/^([a-zA-Z_][a-zA-Z0-9_]*)\s*(==|!=|>=|<=|=|>|<)\s*(.+)$/);
    const variable = match[1]; // 變數名稱，例如 "name" 或 "c"
    const operator = match[2]; // 運算子，例如 "=" 或 ">="
    const value = match[3];    // 值，例如 "S3" 或 "800"
    
    let result = booking(start, end, variable, operator, value)
    console.log(result)
} 
const services=[ 
    {"name":"S1", "r":4.5, "c":1000}, 
    {"name":"S2", "r":3, "c":1200}, 
    {"name":"S3", "r":3.8, "c":800} 
]; 


func2(services, 15, 24, "c>=800")  //S3 
func2(services, 11, 13, "r<=4")  //S3 
func2(services, 10, 12, "name=S3")  // Sorry 
func2(services, 15, 18, "r>=4.5")  // S1 
func2(services, 16, 18, "r>=4")  // Sorry 
func2(services, 13, 17, "name=S1")  // Sorry 
func2(services, 8, 9, "c<=1500")  // S2 
func2(services, 8, 9, "c<=1500") //S1

console.log("--------")

// Task3 ------------------------------------------------------------------------------------


function func3(index){ 
    let number = 25
    let numbers = []
    for (let i=0; i<index; i++){
        if (i%4 == 0){
            number = number-2
            numbers.push(number)
        }
        else if (i%4 == 1){
            number = number-3
            numbers.push(number)
        }
        else if (i%4 == 2){
            number = number+1
            numbers.push(number)
        }
        else if (i%4 == 3){
            number = number+2
            numbers.push(number)
        }
    }
    numbers.unshift(25)


    let result = numbers[index]
    console.log(result)
}
 
 

func3(1)  // print 23 
func3(5)  // print 21 
func3(10)  // print 16 
func3(30)  // print 6 

console.log("--------")



// Task4 ------------------------------------------------------------------------------------


function func4(sp, stat, n){
    // 找到不可以載客的車廂index
        const unavalable_index_list = [] 
        let index = 0
        for (let i of stat){
            if (i == "1"){
                unavalable_index_list.push(index)
                index+=1
            }
            else {index+=1}
        }
    
        // #把不能載客的車廂index的載客量變成1萬
        for (let i of unavalable_index_list){
            sp[i]=10000
        }
    
        // # 計算車廂載客量和乘客數量的差距
        const difference_list = []
        for (let i of sp){
            difference_list.push(Math.abs(i-n)) 
        }
    
        // #印出差異最小的index
        let min_index = difference_list.indexOf(Math.min(...difference_list))
        console.log(min_index)
    
    }
    
    
    
    
    func4([3, 1, 5, 4, 3, 2], "101000", 2)  // print 5 
    func4([1, 0, 5, 1, 3], "10100", 4)  // print 4 
    func4([4, 6, 5, 8], "1000", 4)  // print 2 
    
    
    