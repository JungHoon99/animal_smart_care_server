import pymysql

class MufiData:
    def __init__(self):
        self.__db = pymysql.connect(
            user='root', 
            passwd='1234', 
            host='127.0.0.1', 
            db='animalCare', 
            charset='utf8'
        )
        self.__cursor = self.__db.cursor(pymysql.cursors.DictCursor)

    def insertdb(self, sql):
        check = self.__cursor.execute(sql)
        self.__db.commit()
        return check
    def selectdb(self, sql):
        self.__cursor.execute(sql)
        return self.__cursor.fetchall()