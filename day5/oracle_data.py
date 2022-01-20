# Oracle_data 연동
# cx_oracle 설치 : pip install cx_oracle
import cx_Oracle
import cx_Oracle as ora
# makedsn('호스트명/ip주소', portnum, service_name)
dsn = ora.makedsn('localhost', 1521, service_name = 'orcl') # 접속주소
# connect(user, password, dsn, encoding)
conn = ora.connect(user='scott', password ='tiger', dsn = dsn, encoding='utf-8' )

cur = conn.cursor()

# 예외처리인 경우
try:
    for row in cur.execute('SELECT * FROM emp;'):
         print(row)
    # cur.execute('SELECT COUNT(*) FROM emp')
    # result = cur.fetchone()
    # print(result)
except ora.DatabaseError as e:
    print('쿼리문이 잘못되었습니다. 14번라인 확인요망: {e}')
finally:
    cur.close()  # 커서 닫고
    conn.close() # 접속 닫음
    