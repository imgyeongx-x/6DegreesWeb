import pymysql
from collections import deque

def BFS(v, id_list):
    visited = [False] * v
    queue = deque()
    
    queue.append(id_list[0][0])
    
    print(queue)
    visited[queue[0]] = True
    closer = [-1, -1, ""] * v # 순서대로 parent id, 영화 id, 본인 이름
    cnt = 0
    
    findP = False
    
    
    while queue:
        a = queue.popleft()
        sql = "SELECT peopleName, peopleId, movieId FROM kmovieCast WHERE movieId IN (SELECT movieId FROM kmovieCast WHERE peopleId = %s AND role = 'actor') AND peopleName != '' AND peopleId IS NOT NULL;"

        curs.execute(sql, a)
        cast_list = curs.fetchall()
        
        for i in cast_list:
            index = i[1]
            #print(type(index))
            if visited[index] is False:
                queue.append(i[1])
                closer[i[1]] = [a, i[2], i[0]]
            if i[1] == id_list[1][0]:
                findP = True
                pid = i[1]
                break
        if findP is True:
            print("찾았당")
            break
        print("한바퀴 돌았다")
        print(queue)
    
    
    ## 내일의 나경이에게
    ## 루트까지 찾음
    ## 최단경로만 찾으면 됨
    
    print(closer)
    
    parent = id_list[0][0]
    
    while pid != parent:
        print(closer[pid])
        pid = closer[pid][0]
        
        sql = "SELECT id FROM people WHERE id = "
        curs.execute(sql, namedata)
        id_list = curs.fetchall()
        
        
        
    
    
        
        
        
        

    
    
    

# 이름은 api로 가져와야 함
namedata = ('공유', '마동석')

# 데이터베이스와 연결
conn = pymysql.connect(host='kmoviedb.cn6my6gmusre.ap-northeast-2.rds.amazonaws.com',
                        user='admin',
                        password='qhdnjs1207',
                        db='kmovie',
                        charset='utf8')

curs = conn.cursor()

# 서버로부터 actor 데이터 두 개 GET -> 해야하지만, 임의로 '공유'와 '비비'으로 지정

sql = "SELECT id FROM people WHERE name = %s or name = %s;"
curs.execute(sql, namedata)
id_list = curs.fetchall()

#for i in id_list:
#    print(i)
#print(id_list[0])


#for i in cast_list:
#    print(i)


sql = "SELECT COUNT(*) FROM kmovieCast;"
curs.execute(sql)
tmp = curs.fetchall()

cast_num = int(tmp[0][0])
print(cast_num)

BFS(cast_num, id_list)

conn.close()