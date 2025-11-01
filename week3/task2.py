import urllib.request as req
import bs4

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"


# 拿到標題
def getTitle(url):
    request=req.Request(url, headers={"user-agent":USER_AGENT})

    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find_all("div", class_="title")
    title_list=[]
    for title in titles:
        if title.a is not None:
            title_list.append(title.a.string)

    nextlink=root.find("a", string="‹ 上頁")
    nexturl=nextlink["href"]
    
    return title_list,nexturl, root


#拿到按讚數
def getCount(root):
    likeCounts=root.find_all("div", class_="nrec")
    count_list=[]
    for count in likeCounts:
        if count.span:
            count_list.append(count.span.string)
        else:
            count_list.append("0")
    return count_list


# 拿到日期
def getDate(title_list,root):
    article_link_list=[]
    for title in title_list:
        article_link_without_https=root.find("a", string=title)
        article_link_list.append("https://www.ptt.cc"+article_link_without_https["href"])
    
    date_list=[]   
    for article_link in article_link_list:
        article_request=req.Request(article_link, headers={"user-agent":USER_AGENT})
        with req.urlopen(article_request) as response:
            data=response.read().decode("utf-8")
            article_root=bs4.BeautifulSoup(data, "html.parser")
            label = article_root.find("span", string=lambda s:s and s.strip() == "時間")
            if label:
                date= label.find_next_sibling("span").get_text(strip=True)
                date_list.append(date)
            else:
                date= ""
                date_list.append(date)
    return date_list   



url = "https://www.ptt.cc/bbs/Steam/index.html"
count = 0
all_title_list=[]
all_count_list= []
all_date_list= []
while count<3:
    title_list, next_url,root = getTitle(url)
    all_title_list+= title_list
    all_count_list+=getCount(root)
    all_date_list+=getDate(title_list,root)
    url="https://www.ptt.cc"+next_url
    count+=1


with open("articles.csv", "w", encoding="utf-8") as file:
     for i in range(len(all_title_list)):
        file.write(all_title_list[i]+","+all_count_list[i]+","+all_date_list[i]+"\n")