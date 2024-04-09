import pymysql
from collections import deque

def BFS(v, id_list):
    visited = [False] * v
    queue = deque()
    
    queue.append(id_list[0][0])
    
    visited[queue[0]] = True
    parent = [[-1, -1, ""]] * v # In order parentId, movieId, selfname
    
    findP = False
    
    # finding person2 with BFS
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
                parent[index] = [a, i[2], i[0]]
                visited[index] = True
            if i[1] == id_list[1][0]:
                findP = True
                break
        if findP is True:
            break
    
    index = id_list[1][0]
    
    # Finding route for person1 -> person2
    result = deque();
    while True:
        if parent[index][0] == -1 or index == id_list[0][0]:
            sql = "SELECT name FROM people WHERE id = %s;"
            curs.execute(sql, id_list[0][0])
            firstN = curs.fetchall()
            result.append(firstN[0][0])
            break
        else:
            result.append(parent[index][2])
        
        findMovie = parent[index][1]
        
        sql = "SELECT name FROM kmovie WHERE id = %s;"
        curs.execute(sql, str(findMovie))
        edge = curs.fetchall()
        result.append(edge[0][0])
        
        index = parent[index][0]
        
    while result:
        print(result.pop())
        if (result):
            print("↓")

        
# 이름은 api로 가져와야 함
namedata = ('공유', '구교환')

# 데이터베이스와 연결
conn = pymysql.connect(host='kmoviedb.cn6my6gmusre.ap-northeast-2.rds.amazonaws.com',
                        user='admin',
                        password='qhdnjs1207',
                        db='kmovie',
                        charset='utf8')

curs = conn.cursor()

# 서버로부터 actor 데이터 두 개 GET -> 해야하지만, 임의로 이름 두 개 설정

sql = "SELECT id FROM people WHERE name = %s or name = %s;"
curs.execute(sql, namedata)
id_list = curs.fetchall()

sql = "SELECT COUNT(*) FROM kmovieCast;"
curs.execute(sql)
tmp = curs.fetchall()

cast_num = int(tmp[0][0])

BFS(cast_num, id_list)

conn.close()