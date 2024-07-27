#----------------------#
#--Data bases=>Intro --#
#----------------------#

#- Data bases Is Place Where we can story data 
#- Date bases Organized Into Tables (user,Categories)
#- Tables Has columns (Id,username,Password)
#- Theres many type of data base (MongoDb,Mysql,sqllite)
#- sql stand for structer quere language 
#- sqllite=>can run in memory or in a single file 
# -- browers file https://sqlitebrowser.org/ 
##############################################################

######################################
#      creat data base and connect   #
######################################    

#- Connect
#- Execute
#- Close
#---------------------------------------







#import sqllite module
import sqlite3
#import psycopg2

#creat data base and connect
db=sqlite3.connect("app.db")

#creat the tables and Fields
db.execute("create table if not exists skill(name text ,progress integer,user_id integer)")

#db.close()



    
# conn=psycopg2.connect(
#             database="postgres",
#             user="postgres",
#             password="password",
#             host="localhost",
#         )
    


# if conn:
#     print("Connection to the PostgreSQL established successfully.")
# else:
#     print("Connection to the PostgreSQL encountered and error.")










##########################################################
#--Data bases=> SQLite Insert Data Into Database       --#
#--------------------------------------------------------#

#-cursor => All operation done by cursor not by the connection itself
#-commit => Save All changes
#-----------------------------------------------------------------------


# setting up the cursor 
cursor= db.cursor()


cursor.execute("create table if not exists user (userid integer , name text)")

#Inserting data

cursor.execute("insert into user (userid,name) values(1,'abd')")
cursor.execute("insert into user (userid,name) values(2,'abood')")
cursor.execute("insert into user (userid,name) values(3,'abdalrheem')")

list=["java","python","c","c++","django"]
i=0
for key,user in enumerate(list):
    i+=1
    cursor.execute(f"insert into skill (name,progress,user_id) values('{user}',0,{i})")

for key,user in enumerate(list):
     cursor.execute(f"insert into user (userid,name) values({key},'{user}')")
tuple=("abooooood",15)
cursor.execute("insert into user  values(?,?)",tuple)
cursor.execute("insert into user  values(?,?)",("abooooood",15))


# Fetch Data 
# fetchone() : return single record 
# fetchall() : fetch all the record of  the query result
# fetchmany(size) 





cursor.execute("select name from user")
print(cursor.fetchmany(2))#[('abd',), ('abood',)]

print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())#None

cursor.execute("select userid,name from user")
cursor.execute("select userid,name from user order by name")
cursor.fetchall()
cursor.execute("select userid,name from user order by userid")
cursor.fetchall()

cursor.execute("select userid,name from user order by userid asc")
cursor.fetchall()

cursor.execute("select userid,name from user order by userid desc")
print(cursor.fetchall())
cursor.execute("select userid,name from user order by name limit 2")
print(cursor.fetchall())
cursor.execute("select userid,name from user order by name limit 2 offset 4")#start after offset
print(cursor.fetchall())
cursor.execute("select userid,name from user where userid > 1")#start after offset
print(cursor.fetchall())
cursor.execute("select * from user where userid not in(1,2,3)")
print(cursor.fetchall())
cursor.execute("select * from user where userid in(1,2,3)")
print(cursor.fetchall())

# print(cursor.fetchall())#[(1, 'abd'), (2, 'abood'), (3, 'abdalrheem'), (1, 'java'), (2, 'python'), (3, 'c'), (4, 'c++'), (5, 'django')]      

def get_all_data():
    try:
#         #Connect to data base
        db=sqlite3.connect("app.dp")
        print("connect database is successfully")
        #setting up cursor
        cr=db.cursor()

#         #Fetch Data From Database
        cr.execute("select * from users")

        #Assign data to variable
        results=cr.fetchone()
        print(results)
        results=cr.fetchall()
        print(results)
        print(results[0])
        #print number of rows
        print(f"data base has {len(results)} rows.")
        #printing massage
        print("showing data")
        #loop on results
        for row in results:
            print(f"user Id=>{row[0]}",end=" ")
            print(f"user name=>{row[1]}",end=" ")

    except sqlite3.Error as error:
        print("error reading data {er}")    
    finally :
        if(db):
            db.close()
            print("connection to data base is close")








#save commit changes 
db.commit()






##########################################################
#--Data bases=>  Update And Delete      --#
#--------------------------------------------------------#

# Update And Delete  
cursor.execute("update user set name = 'abd' ")
cursor.execute("select name from user")
print(cursor.fetchone())#('abd')
print(cursor.fetchone())#('abd')
print(cursor.fetchone())#('abd')
print(cursor.fetchone())#('abd')
print(cursor.fetchall())
cursor.execute(f"update user set name = 'admin' where userid = 1")
cursor.execute("select * from user")
print(cursor.fetchall())
#delete data 
cursor.execute("delete from  user ")
cursor.execute("select name from user")
print(cursor.fetchall())#[]
cursor.execute("delete from  user ")
def comm_close():
    db.commit()
    db.close()
    print("commit and close method ")



##########################################################
#--     Data bases=>  create skills App patr 1         --#
#--------------------------------------------------------#

input_Massage="""
what do you want to do?
"show"=>show all skills
"add "=>add new skill
"delete "=>delete a skill
"update"=>update skill progress
"quit"=>quit app
choos option:
"""
#input option choose
userinput=input(input_Massage).strip().lower()
print(userinput)

#input id
userid=input("input user id ").strip().capitalize()

#Command list
command_list=["show","add","delete","update","quit"]

#Define the method
def show_skill():
   print(f"show")
   cursor.execute("select * from skill where user_id='{userid}' ")
   resulte=cursor.fetchall()
   print(f"you have {len(resulte)} skill.")
   if len(resulte)>0:
        print(f"showing skill with progress")
   for row in resulte:
       print(f"skill => {row[0]},",end=" ")
       print(f"progress => {row[1]}%")

    
  # comm_close()

def add_skill():
    print(f"add")
    sk=input("skill name : ").strip().capitalize()
    cursor.execute(f"select name from skill where name= '{sk}' and  user_id = ' {userid}'   ")
     
    print(f"{cursor.fetchall()}")
    if cursor.fetchall()!=None:
        print("skill is exists :)")
        
    else:    
       progress=input("skill progress :").strip().capitalize()
       cursor.execute(f"insert into skill (name,progress,user_id) values('{sk}','{progress}','{userid}')")
    #comm_close()
    db.commit()


def delete_skill():
    print(f"delete")
    sk=input("skill name to delete :").strip().capitalize()
    cursor.execute(f"delete from skill where name ='{sk}'and user_id='{userid}'")

    comm_close()

    
def update_skill():
    print(f"update")
    # cursor.execute("select userid from user where name = '{oldskill}'")
    # strint=str(cursor.fetchall())
    # print(cursor.fetchall())
    # strint2=strint.strip("( )").strip(",")
    sk=input("skill name : ").strip().capitalize()
    progress=input("progress name").strip().capitalize()
    cursor.execute(f"update skill set progress='{progress}' where name='{sk}' and  user_id = '{userid}' ")

    comm_close()

def quit_skill():
    print(f"quit")
    comm_close()






#Check if command is exict
if userinput in command_list:
    print(f"command is found  {userinput}")
    if userinput=="show":
        show_skill()
    elif userinput=="add":
        add_skill()
    elif userinput=="delete":
        delete_skill()

    elif userinput=="update":
        oldskill=input("old skill to update").strip().capitalize()
        update_skill(oldskill)

    elif userinput=="quit":
        quit_skill()
    else:
        print("App is closed")







else:
    print(f"command is not found{userinput}")    





