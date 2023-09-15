import random
import time
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from pymongo import MongoClient     #pip install pymongo
from faker import Faker #pip install faker
from database import DB
from datetime import date
# n is the numbers of excecution 
uri = ""
def Generate_read_workload(n):
    db = DB()
    # MongoDB connection
    mongo_client = MongoClient(uri)
    mongo_db = mongo_client["your_mongodb_database"]
    mongo_collection = mongo_db["tasks"]

    timestamp1=[]
    timestamp_mon=[]
    excecute1=[]
    total_time_mysql = 0  
    total_time_mongodb = 0  
    
    for i in range(n):

#       Read random data in data set <<----
        excecute1.append(i)
        start_time_one_ex=time.time()
        #db.read_person(random.randint(2,n-1))
        end_time_one_ex=time.time()
        time_s=end_time_one_ex-start_time_one_ex
        total_time_mysql += time_s
        timestamp1.append(time_s)


#                                    <<----
        start_time_one_ex_mon = time.time()
        # Read from MongoDB here using pymongo
        end_time_one_ex_mon = time.time()
        time_mon = end_time_one_ex_mon - start_time_one_ex_mon
        total_time_mongodb += time_mon
        timestamp_mon.append(time_mon)
   
   
    # Create a grid with 60% for the graph and 40% for the total time text
    gs = gridspec.GridSpec(1, 2, width_ratios=[8, 2])

    # Plotting the graph with 60% width
    plt.subplot(gs[0])
    plt.plot(excecute1, timestamp1, label='MySQL', color='blue')
    plt.plot(excecute1, timestamp_mon, label='MongoDB', color='green')

    plt.xlabel('number of execute')
    plt.ylabel('time')
    plt.title('Process time per Read execute')

    # Adding a legend to the graph
    plt.legend()

    # Adding side label for total times within the 40% width
    plt.subplot(gs[1])
    plt.text(0, 0.5, f'Total Time (MySQL): {total_time_mysql:.2f} seconds', fontsize=10, color='blue')
    plt.text(0, 0.7, f'Total Time (MongoDB): {total_time_mongodb:.2f} seconds', fontsize=10, color='green')
    plt.axis('off')  # Turn off axis for the total time text

    plt.show()

    # Close database connections
    db.close_connection()
    mongo_client.close()
    timestamp1.clear()
    excecute1.clear()

def Generate_create_workload(n):
    db = DB()
    fake = Faker()
    # MongoDB connection
    mongo_client = MongoClient(uri)
    mongo_db = mongo_client["Simulation"]
    mongo_collection = mongo_db["Test"]
    timestamp1=[]
    timestamp_mon=[]
    excecute1=[]
    total_time_mysql = 0  
    total_time_mongodb = 0  
    for i in range(n):
        first_name=fake.first_name()
        last_name=fake.last_name()
        date_of_birth=fake.date_of_birth()
        age = (date.today() - fake.date_of_birth(maximum_age=120)).days//365
        height=random.uniform(140,200)
        pic=fake.binary(length=1024)
        excecute1.append(i)
        start_time_one_ex=time.time()

    
        db.create_person(first_name,last_name,age,date_of_birth,height,pic) #   <<----


        end_time_one_ex=time.time()
        time_s=end_time_one_ex-start_time_one_ex
        total_time_mysql += time_s
        timestamp1.append(time_s)

        date_of_birth_dict = {
            "year": date_of_birth.year,
            "month": date_of_birth.month,
            "day": date_of_birth.day
        }
        person_data = {
            "first_name": first_name,
            "last_name": last_name,
            "age": age,
            "date_of_birth": date_of_birth_dict,
            "height": height,
            "picture": pic  
        }
        start_time_one_ex_mon = time.time()


        mongo_collection.insert_one(person_data) #<-----


        end_time_one_ex_mon = time.time()
        time_mon = end_time_one_ex_mon - start_time_one_ex_mon
        total_time_mongodb += time_mon
        timestamp_mon.append(time_mon)
   
   
    # Create a grid with 60% for the graph and 40% for the total time text
    gs = gridspec.GridSpec(1, 2, width_ratios=[8, 2])

    # Plotting the graph with 60% width
    plt.subplot(gs[0])
    plt.plot(excecute1, timestamp1, label='MySQL', color='blue')
    plt.plot(excecute1, timestamp_mon, label='MongoDB', color='green')

    plt.xlabel('number of execute')
    plt.ylabel('time')
    plt.title('Process time per Create execute')

    # Adding a legend to the graph
    plt.legend()

    # Adding side label for total times within the 40% width
    plt.subplot(gs[1])
    plt.text(0, 0.5, f'Total Time (MySQL): {total_time_mysql:.2f} seconds', fontsize=10, color='blue')
    plt.text(0, 0.7, f'Total Time (MongoDB): {total_time_mongodb:.2f} seconds', fontsize=10, color='green')
    plt.axis('off')  # Turn off axis for the total time text

    plt.show()


    # Close database connections
    db.close_connection()
    mongo_client.close()
    timestamp1.clear()
    excecute1.clear()

    
def Generate_delete_workload(n):
    db = DB()
    # MongoDB connection
    mongo_client = MongoClient(uri)
    mongo_db = mongo_client["your_mongodb_database"]
    mongo_collection = mongo_db["tasks"]

    timestamp1=[]
    timestamp_mon=[]
    excecute1=[]
    total_time_mysql = 0
    total_time_mongodb = 0
    for i in range(n):

#       Read random data in data set <<----
        excecute1.append(i)
        start_time_one_ex=time.time()
        #db.read_person(random.randint(2,n-1))
        end_time_one_ex=time.time()
        time_s=end_time_one_ex-start_time_one_ex
        total_time_mysql += time_s
        timestamp1.append(time_s)


#                                    <<----
        start_time_one_ex_mon = time.time()
        # Read from MongoDB here using pymongo
        end_time_one_ex_mon = time.time()
        time_mon = end_time_one_ex_mon - start_time_one_ex_mon
        total_time_mongodb += time_mon
        timestamp_mon.append(time_mon)
   
   
    # Create a grid with 60% for the graph and 40% for the total time text
    gs = gridspec.GridSpec(1, 2, width_ratios=[8, 2])

    # Plotting the graph with 60% width
    plt.subplot(gs[0])
    plt.plot(excecute1, timestamp1, label='MySQL', color='blue')
    plt.plot(excecute1, timestamp_mon, label='MongoDB', color='green')

    plt.xlabel('number of execute')
    plt.ylabel('time')
    plt.title('Process time per Delete execute')

    # Adding a legend to the graph
    plt.legend()

    # Adding side label for total times within the 40% width
    plt.subplot(gs[1])
    plt.text(0, 0.5, f'Total Time (MySQL): {total_time_mysql:.2f} seconds', fontsize=10, color='blue')
    plt.text(0, 0.7, f'Total Time (MongoDB): {total_time_mongodb:.2f} seconds', fontsize=10, color='green')
    plt.axis('off')  # Turn off axis for the total time text

    plt.show()


    # Close database connections
    db.close_connection()
    mongo_client.close()
    timestamp1.clear()
    excecute1.clear()

def Generate_update_workload(n):
    db = DB()
    # MongoDB connection
    mongo_client = MongoClient(uri)
    mongo_db = mongo_client["your_mongodb_database"]
    mongo_collection = mongo_db["tasks"]

    timestamp1=[]
    timestamp_mon=[]
    excecute1=[]
    total_time_mysql = 0
    total_time_mongodb = 0
    for i in range(n):


        excecute1.append(i)
        start_time_one_ex=time.time()
        #db.update_person() <<----
        end_time_one_ex=time.time()
        time_s=end_time_one_ex-start_time_one_ex
        total_time_mysql += time_s
        timestamp1.append(time_s)



        start_time_one_ex_mon = time.time()
        # Read from MongoDB here using pymongo <<----
        end_time_one_ex_mon = time.time()
        time_mon = end_time_one_ex_mon - start_time_one_ex_mon
        total_time_mongodb += time_mon
        timestamp_mon.append(time_mon)
   
   
    # Create a grid with 60% for the graph and 40% for the total time text
    gs = gridspec.GridSpec(1, 2, width_ratios=[8, 2])

    # Plotting the graph with 60% width
    plt.subplot(gs[0])
    plt.plot(excecute1, timestamp1, label='MySQL', color='blue')
    plt.plot(excecute1, timestamp_mon, label='MongoDB', color='green')

    plt.xlabel('number of execute')
    plt.ylabel('time')
    plt.title('Process time per Update execute')

    # Adding a legend to the graph
    plt.legend()

    # Adding side label for total times within the 40% width
    plt.subplot(gs[1])
    plt.text(0, 0.5, f'Total Time (MySQL): {total_time_mysql:.2f} seconds', fontsize=10, color='blue')
    plt.text(0, 0.7, f'Total Time (MongoDB): {total_time_mongodb:.2f} seconds', fontsize=10, color='green')
    plt.axis('off')  # Turn off axis for the total time text

    plt.show()


    # Close database connections
    db.close_connection()
    mongo_client.close()
    timestamp1.clear()
    excecute1.clear()


Generate_create_workload(1)
#db = mysql.connector.connect()
