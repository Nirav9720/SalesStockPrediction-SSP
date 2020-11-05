import pymysql


def connection():
    con = pymysql.connect(
        host='localhost',
        user='root',
        password='Linux@123',
        port=3306,
        db='project_ssp',
        cursorclass=pymysql.cursors.DictCursor
    )
    return con
