import os
import mysql.connector
from util.PropertyUtil import PropertyUtil

class DBConnection:
    connection = None

    @staticmethod
    def getConnection():
        if DBConnection.connection is None or not DBConnection.connection.is_connected():
            file_path = os.path.join(os.path.dirname(__file__), '..', 'db.properties')
            props = PropertyUtil.getPropertyString(file_path)
            try:
                DBConnection.connection = mysql.connector.connect(**props)
                print("Connected to MySQL.")
            except mysql.connector.Error as e:
                print(f"Connection failed: {e}")
        return DBConnection.connection
