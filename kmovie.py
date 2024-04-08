import pymysql
from collections import deque

"""def BFS(v):
    queue = deque(curs.execute("SELECT movieID FROM "))
    visited[v] = 1
    
    
    while queue:
        target = queue.popleft()
        
        for i in graph[target]:
    """




# 데이터베이스와 연결
conn = pymysql.connect(host='kmoviedb.cn6my6gmusre.ap-northeast-2.rds.amazonaws.com',
                         user='admin',
                         password='qhdnjs1207',
                         db='kmovie',
                         charset='utf8')

curs = conn.cursor()

# 서버로부터 actor 데이터 두 개 GET -> 해야하지만, 임의로 '공유'와 '비비'으로 지정

curs.execute("SELECT id, name FROM people WHERE name = '공유' or name = '비비';")
id_list = curs.fetchall()

for i in id_list:
    print(i)


curs.execute("SELECT name, director, cast, writer FROM movie WHERE cast LIKE '%공유,%'")
cast_list = list(curs.fetchall());

print(cast_list[0][0])


for i in cast_list:
    print(i)




conn.close()
