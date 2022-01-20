# 커서에 접근하는 코드를 함수로 작성
import cx_Oracle as ora

def myconn():
    dsn = ora.makedsn('localhost', 1521, service_name='orcl')
    conn = ora.connect(user = 'scott', password = 'tiger', dsn = dsn, encoding ='utf-8')
    return conn

def getAlldata(conn): # conn 객체를 매개변수 받아서 쿼리를 실행할 함수
    cur = conn.cursor() # 커서생성
    query = 'SELECT * FROM emp' # emp 테이블에서 데이터 모두 가져와라
    for row in cur.execute(query): # emp 테이블의 최상단에 커서가 위치하면서 모든 데이터를 
        print(row) # 한 줄씩 출력
def getNameAndJobData(conn):

    cur = conn.cursor()
    query = 'SELECT ename, job FROM emp' # emp 테이블 ename, job
    for row in cur.execute(query):
        print(row)
    
def getDeptName(conn, no, loc):

    cur = conn.cursor()
    query = 'SELECT * FROM dept WHERE deptno = :1 AND loc = :2' 
    cur.execute(query,tup)
    row = cur.fetchone()
    print(row)

if __name__ == '__main__' : # 언더바 2개

    print('프로그램 시작')
    # 함수호출
    scott_con = myconn() # dsn, connect() 후 접속개체 conn 리턴
    
    # print('emp 테이블 전체 조회(SELECET *)')
    # getAlldata(scott_con)
    # print('emp 2개 컬럼조회')
    # getNameAndJobData(scott_con)

    no = input ('1.부서번호를 입력하세요 :')
    loc = input('2.지역명을 입력하세요 :').upper()
    tup = (no, loc)
    # print(f'부서번호: {no}, 지역: {loc}')
    getDeptName(scott_con, no, loc) 

    print('프로그램 종료')
