import mysql.connector

class DatabaseHelper(object):

    __instance = None

    @staticmethod 
    def getInstance():
        if DatabaseHelper.__instance == None:
            DatabaseHelper()
        return DatabaseHelper.__instance
    
    def __init__(self):
        if DatabaseHelper.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            self.__cnx = None

            DatabaseHelper.__instance = self

    def db(self):
        if self.__cnx is None:
            # open a databse connection
            self.__cnx = mysql.connector.connect(user='root', password='?=Sq66.t',
                                host='35.244.65.158',
                                database='sql6430075')
        elif not self.__cnx.is_connected():
            self.__cnx.reconnect()
        return self.__cnx

    def close(self):
        
        if self.__cnx is not None and self.__cnx.is_connected():
            self.__cnx.close()
        
        self.__cnx = None

    