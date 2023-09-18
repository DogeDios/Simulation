import random
import time
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from pymongo import MongoClient     #pip install pymongo
from faker import Faker #pip install faker
from database import DB
from datetime import date
import random
# n is the numbers of excecution 
uri = "mongodb+srv://Preme:abc1234@cluster0.5z3knde.mongodb.net/?retryWrites=true&w=majority"

def Generate_read_workload(n):
    db = DB()
    fake = Faker()
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
        excecute1.append(i)
        start_time_one_ex=time.time()

    
        db.read_person(first_name) 

 
        end_time_one_ex=time.time()
        time_s=end_time_one_ex-start_time_one_ex
        total_time_mysql += time_s
        timestamp1.append(time_s)


        start_time_one_ex_mon = time.time()#<-----

        query={"name":first_name }
        mongo_collection.find(query)


        end_time_one_ex_mon = time.time()#<-----
        time_mon = end_time_one_ex_mon - start_time_one_ex_mon
        total_time_mongodb += time_mon
        timestamp_mon.append(time_mon)
   
   
    # Create a grid with 60% for the graph and 40% for the total time text
    gs = gridspec.GridSpec(1, 2, width_ratios=[5, 5])

    # Plotting the graph with 60% width
    plt.subplot(gs[0])
    plt.plot(excecute1, timestamp1,label='MySQL', color='blue',marker='o', linestyle='-')
    plt.plot(excecute1, timestamp_mon, label='MongoDB', color='green',marker='x', linestyle='-')

    plt.xlabel('number of execution',fontsize=24)
    plt.ylabel('time (seconds)',fontsize=24)
    plt.title('Process time for Read operation',fontsize=24)
    
    # Adding a legend to the graph
    plt.legend()

    # Adding side label for total times within the 40% width
    plt.subplot(gs[1])
    plt.text(0, 0.5, f'Total Time (MySQL): {total_time_mysql:.4f}  second', fontsize=24, color='blue')
    plt.text(0, 0.7, f'Total Time (MongoDB): {total_time_mongodb:.4f}  second', fontsize=24, color='green')
    plt.axis('off')  # Turn off axis for the total time text

    plt.show()


    # Close database connections
    db.close_connection()
    mongo_client.close()
    timestamp1.clear()
    timestamp_mon.clear()
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
        start_time_one_ex_mon = time.time()#<-----


        mongo_collection.insert_one(person_data) #<-----


        end_time_one_ex_mon = time.time()#<-----
        time_mon = end_time_one_ex_mon - start_time_one_ex_mon
        total_time_mongodb += time_mon
        timestamp_mon.append(time_mon)
   
   
    # Create a grid with 60% for the graph and 40% for the total time text
    gs = gridspec.GridSpec(1, 2, width_ratios=[6, 4])

    # Plotting the graph with 60% width
    plt.subplot(gs[0])
    plt.plot(excecute1, timestamp1,label='MySQL', color='blue',marker='o', linestyle='-')
    plt.plot(excecute1, timestamp_mon, label='MongoDB', color='green',marker='x', linestyle='-')

    plt.xlabel('number of execution',fontsize=24)
    plt.ylabel('time (seconds)',fontsize=24)
    plt.title('Process time for Create operation',fontsize=24)
    
    # Adding a legend to the graph
    plt.legend()

    # Adding side label for total times within the 40% width
    plt.subplot(gs[1])
    plt.text(0, 0.5, f'Total Time (MySQL): {total_time_mysql:.6f} secound', fontsize=24, color='blue')
    plt.text(0, 0.7, f'Total Time (MongoDB): {total_time_mongodb:.6f} secound', fontsize=24, color='green')
    plt.axis('off')  # Turn off axis for the total time text

    plt.show()


    # Close database connections
    db.close_connection()
    mongo_client.close()
    timestamp1.clear()
    timestamp_mon.clear()
    excecute1.clear()

    
def Generate_delete_workload(n):
    db = DB()
    fake = Faker()
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

    
        db.delete_person(first_name)


        end_time_one_ex=time.time()
        time_s=end_time_one_ex-start_time_one_ex
        total_time_mysql += time_s
        timestamp1.append(time_s)


        start_time_one_ex_mon = time.time()#<-----
        delete_condition = {"name": first_name}
        # Update the MongoDB document with the new data
        mongo_collection.delete_one(delete_condition)
        end_time_one_ex_mon = time.time()
        time_mon = end_time_one_ex_mon - start_time_one_ex_mon
        total_time_mongodb += time_mon
        timestamp_mon.append(time_mon)
   
   
    # Create a grid with 60% for the graph and 40% for the total time text
    gs = gridspec.GridSpec(1, 2, width_ratios=[6, 4])

    # Plotting the graph with 60% width
    plt.subplot(gs[0])
    plt.plot(excecute1, timestamp1,label='MySQL', color='blue',marker='o', linestyle='-')
    plt.plot(excecute1, timestamp_mon, label='MongoDB', color='green',marker='x', linestyle='-')

    plt.xlabel('number of execution',fontsize=24)
    plt.ylabel('time (seconds)',fontsize=24)
    plt.title('Process time for Delete operation',fontsize=24)
    
    # Adding a legend to the graph
    plt.legend()

    # Adding side label for total times within the 40% width
    plt.subplot(gs[1])
    plt.text(0, 0.5, f'Total Time (MySQL): {total_time_mysql:.4f} secound', fontsize=24, color='blue')
    plt.text(0, 0.7, f'Total Time (MongoDB): {total_time_mongodb :.4f} secound', fontsize=24, color='green')
    plt.axis('off')  # Turn off axis for the total time text

    plt.show()


    # Close database connections
    db.close_connection()
    mongo_client.close()
    timestamp1.clear()
    timestamp_mon.clear()
    excecute1.clear()

def Generate_update_workload(n):
    db = DB()
    fake = Faker()
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

    
        db.update_person(random.randint(2,3000),first_name ,last_name, age, date_of_birth,height,pic)


        end_time_one_ex=time.time()
        time_s=end_time_one_ex-start_time_one_ex
        total_time_mysql += time_s
        timestamp1.append(time_s)


        start_time_one_ex_mon = time.time()#<-----
        query = {"name": i}  # Modify the query to match your MongoDB document
        update_data = {
            "$set": {
                "first_name": first_name,
                "last_name": last_name,
                "age": age,
                "date_of_birth": {
                    "year": date_of_birth.year,
                    "month": date_of_birth.month,
                    "day": date_of_birth.day
                },
                "height": height,
                "picture": pic
            }
        }
        # Update the MongoDB document with the new data
        mongo_collection.update_one(query, update_data)
        end_time_one_ex_mon = time.time()
        time_mon = end_time_one_ex_mon - start_time_one_ex_mon
        total_time_mongodb += time_mon
        timestamp_mon.append(time_mon)
   
   
    # Create a grid with 60% for the graph and 40% for the total time text
    gs = gridspec.GridSpec(1, 2, width_ratios=[6, 4])

    # Plotting the graph with 60% width
    plt.subplot(gs[0])
    plt.plot(excecute1, timestamp1,label='MySQL', color='blue',marker='o', linestyle='-')
    plt.plot(excecute1, timestamp_mon, label='MongoDB', color='green',marker='x', linestyle='-')

    plt.xlabel('number of execution',fontsize=24)
    plt.ylabel('time (seconds)',fontsize=24)
    plt.title('Process time for Update operation',fontsize=24)
    
    # Adding a legend to the graph
    plt.legend()

    # Adding side label for total times within the 40% width
    plt.subplot(gs[1])
    plt.text(0, 0.5, f'Total Time (MySQL): {total_time_mysql:.4f} secound', fontsize=24, color='blue')
    plt.text(0, 0.7, f'Total Time (MongoDB): {total_time_mongodb :.4f} secound', fontsize=24, color='green')
    plt.axis('off')  # Turn off axis for the total time text

    plt.show()


    # Close database connections
    db.close_connection()
    mongo_client.close()
    timestamp1.clear()
    timestamp_mon.clear()
    excecute1.clear()


#Generate_create_workload(1000)
Generate_read_workload(1000)
#Generate_update_workload(1000)
#Generate_delete_workload(1000)

