import mysql.connector

#createbthe database connection
connection = mysql.connector.connect(host = "localhost", username = "root", password = "12345678", database = "todo")

#to verify the connection is establish or not
if connection.is_connected():
    print("db is connect")
else:
    print("db not connect")
    
    
#create table for todo app - task
task =  "create table if not exists task (taskname text, mobile text)"

#create cursor to execute the mysql queries
mycursor = connection.cursor()

# to execute the create task table in database todo
mycursor.execute(task)

#to commit or save the mysql querry
connection.commit()

#to insert task in todo database
insertTask = "insert into task values('{}','{}')".format(input("Enter task name :"),input("Enter Mobile no :"))

#to execute the insert querry
mycursor.execute(insertTask)

#to save the operation
connection.commit()

#update the task in database
updateTask = "Update task set taskname ='ITS vam' where mobile = '9992289156' "
mycursor.execute(updateTask)
connection.commit()

#to delete the task from database todo
deleteTask = "delete from task where mobile ='111'"
mycursor.execute(deleteTask)
connection.commit()

#to access the data from database
myTask = "select * from task"
mycursor.execute(myTask)
print(mycursor.fetchall())
connection.commit()

#to drop the table
dropTask = "drop table task"
mycursor.execute(dropTask)
connection.commit()

# press 1 to add new Event: eventName, eventDate,venue,eventId
# press 2 to get all Event
# press 3 to delete Event
# press 4 to update Event

# press 5 to add student in event :-stuName , stuEmail, stuMobile, stuDept, stuYear,eventName
