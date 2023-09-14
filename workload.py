import random
import time
import matplotlib.pyplot as plt
import mysql.connector      #pip install mysql-connector-python
from pymongo import MongoClient     #pip install pymongo
from faker import Faker #pip install faker


# n is the numbers of excecution 

def Generate_read_workload(n):
    mysql_conn = mysql.connector.connect(
        host="your_mysql_host",
        user="your_mysql_user",
        password="your_mysql_password",
        database="your_mysql_database"
    )
    mysql_cursor = mysql_conn.cursor()

    # MongoDB connection
    mongo_client = MongoClient("mongodb://your_mongodb_host:27017/")
    mongo_db = mongo_client["your_mongodb_database"]
    mongo_collection = mongo_db["tasks"]

    timestamp1=[]
    excecute1=[]
    start=time.time()
    for i in range(n):
        excecute1.append(i)
        start_time_one_ex=time.time()
#       Read random data in data set <<----
        
#                                    <<----
        end_time_one_ex=time.time()
        time_s=end_time_one_ex-start_time_one_ex
        timestamp1.append(time_s)
    end = time.time()
    print('Time to excecute read:',end-start)
    plt.scatter(excecute1, timestamp1,s=3)
    plt.xlabel('number of excecute ')
    plt.ylabel('time')
    plt.title('Process time per excecute')
    plt.show()
    timestamp1.clear()
    excecute1.clear()

def Generate_create_workload(n):
    start=time.time()
    for i in range(n):
        pass
    end = time.time()
    print('Time to excecute create:',end-start)
def Generate_delete_workload(n):
    start=time.time()
    for i in range(n):

        pass
    end = time.time()
    print('Time to excecute delete:',end-start)

def Generate_update_workload(n):
    start=time.time()
    for i in range(n):

        pass
    end = time.time()
    print('Time to excecute update:',end-start)


Generate_read_workload(1000)
#db = mysql.connector.connect()
