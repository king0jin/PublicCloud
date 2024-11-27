from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

import pymysql

@api_view(['GET'])
def user(request):
    # MySQL 데이터베이스 연결
    try:
        con = pymysql.connect(host='43.203.231.79',
                               port=3306,
                               user='jini',
                               passwd='000000',
                               db='databeseconn',
                               charset='utf8')
        cursor = con.cursor()

        # SQL 쿼리 실행
        cursor.execute("SELECT * FROM users")

        # 데이터 가져오기
        data = cursor.fetchall()

        # 데이터 형식 맞추기
        result = []
        for row in data:
            result.append({
                'id': row[0],  # Assuming the first column is 'id'
                'username': row[1],  # Assuming the second column is 'title'
                'email': row[2],  # Assuming the third column is 'author'
                'password': row[3]
            })
        return Response(result, status=status.HTTP_200_OK)
    
    except pymysql.MySQLError as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    finally:
        # 연결 종료
        if con:
            cursor.close()
            con.close()
