import sqlite3

def shit(word): 
    conn = sqlite3.connect(r'C:\Users\Athan\OneDrive\Documents\Dissertation\Python\webscraper\url.db')
    curr = conn.cursor()
    conurl = []
    conurl1 = []
    start_url = []
    start_url1 =[]
    starturl =[]
    j = 0
    miakurvabajodvan = 0
    curr.execute("""SELECT DISTINCT connections FROM 'origoParagaph_tb' WHERE connections LIKE '%index.hu%' ORDER BY time;""")
    for row in curr.fetchall():
        conurlrow = str(row)
        conurlrow = conurlrow.replace('!£!'," ")
        conurlrow = conurlrow.replace('(',"")
        conurlrow = conurlrow.replace(')',"")
        conurlrow = conurlrow.replace("'","")
        conurlrow = conurlrow.replace(',',"")
        conurlrow = conurlrow.split()        
        conurl.append(conurlrow)
    curr.execute("""SELECT DISTINCT start_url FROM 'origoParagaph_tb' WHERE connections LIKE '%index.hu%' ORDER BY time;""")
    for row in curr.fetchall():
        start_urlrow = str(row)
        start_urlrow = start_urlrow.replace('(',"")
        start_urlrow = start_urlrow.replace(')',"")
        start_urlrow = start_urlrow.replace("'","")
        start_urlrow = start_urlrow.replace(',',"")
        start_urlrow = start_urlrow.split()        
        start_url.append(start_urlrow)
    for row in conurl:
        conurlrow = str(row).split()
        conurl1.append(conurlrow)
        for i in conurlrow:
            start_url1.append([start_url[j],[i]])
        j+=1
    while miakurvabajodvan < len(start_url1):
        if word in str(start_url1[miakurvabajodvan][1][0]):
            starturl.append([start_url1[miakurvabajodvan][1][0],start_url1[miakurvabajodvan][0][0]])
        miakurvabajodvan += 1
 
    return starturl
print(shit("index.hu"))