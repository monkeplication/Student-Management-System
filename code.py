# Project code:-
import mysql.connector
def show_database():
db = mysql.connector.connect(host = "localhost",user =
"root", passwd = "omega")
cursor = db.cursor()
cursor.execute("show databases")
print(cursor.fetchall())
def create_table():
db = mysql.connector.connect(host = "localhost",user =
"root", passwd = "omega",database = "student12")
cursor = db.cursor()
cursor.execute("create table student5(rollno int primarykey,name varchar(20), stream varchar(10), total int, gradevarchar(3), Class int);")
print("Table created")
def showtables():
db = mysql.connector.connect(host = "localhost",user =
"root", password = "omega",database = "student12")
cursor = db.cursor()
cursor.execute("show tables;")
for x in cursor:
print(x)
def display_struc():
db = mysql.connector.connect(host = "localhost",user =
"root", password = "omega",database = "student12")
cursor = db.cursor()
cursor.execute("desc student5;")
for x in cursor:
print(x)
def add_rec():
db = mysql.connector.connect(host = "localhost",user =
"root", password = "omega", database = "student12")
cursor = db.cursor()
rno = int(input("Enter roll number"))
nm = input("Enter name")
st = input("Enter stream")
tot = int(input("Enter total"))
gr = input("Enter grade")
C = int(input ("Enter class"))
sql_query = "insert into student5 values(%s,%s,%s,%s,%s,%s);"
val = (rno,nm,st,tot,gr,C)
cursor.execute(sql_query,val)
db.commit()
print("Record added")
def update_rec():
db = mysql.connector.connect(host = "localhost",user =
"root", password = "praharsha79", database = "student12")
cursor = db.cursor()
rno = int(input("Enter rollno"))
tot = int(input("Enter total"))
sql_query = "Update student5 set total = %s where rollno =%s;"
val = (tot,rno)
cursor.execute(sql_query,val)
print(cursor.rowcount, "record updated")
db.commit()
def delete_rec():
db = mysql.connector.connect(host = "localhost",user =
"root", password = "praharsha79",database = "student12")
cursor = db.cursor()
rno = int(input("Enter rollno"))
sql_query = "delete from student5 where rollno = %s;"
cursor.execute(sql_query,(rno,))
print(cursor.rowcount, "record deleted")
db.commit()
def fetch_data():
db = mysql.connector.connect(host = "localhost",user =
"root", password = "praharsha79", database = "student12")
cursor = db.cursor()
cursor.execute("SELECT * FROM student5;")
records = cursor.fetchall()
for x in records:
print(x[0],x[1],x[2],x[3],x[4],x[5])
def topper_list():
db = mysql.connector.connect(host = "localhost",user =
"root", password = "praharsha79",database = "student12")
cursor = db.cursor()
cursor.execute("select * from student5 order by totaldesc;")
records = cursor.fetchall()
for x in records:
print(x[0],x[1],x[2],x[3],x[4],x[5])
while True:
print("*STUDENT REGISTRATION SYSTEM*")
print("1: To show databases")
print("2: To create a table")
print("3: To show tables present in the database")
print("4: To display structure of the table")
print("5: To add a record in the table")
print("6: To update a record in the table")
print("7: To delete a record from the table") 
print("8: Todisplay all the records from the table") 
print("9: To sort the data in descending order of total") 
print("10: To quit")
choice = int(input("Enter your choice"))
if choice == 1:
show_database()
elif choice == 2:
create_table()
elif choice == 3:
showtables()
elif choice == 4:
display_struc()
elif choice == 5:
add_rec()
elif choice == 6:
update_rec()
elif choice == 7:
delete_rec()
elif choice == 8:
fetch_data()
elif choice == 9:
topper_list()
elif choice == 10:
print("Exiting")
break
