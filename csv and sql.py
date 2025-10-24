import sqlite3
with sqlite3.connect("top_hotels.db") as db:
    cursor=db.cursor()
    
cursor.execute("""CREATE TABLE IF NOT EXISTS top_hotels(id integer PRIMARY KEY,
hotel text NOT NULL,
location text NOT NULL,
country text NOT NULL,
region text NOT NULL,
company text NOT NULL,
score float NOT NULL,
rank integer NOT NULL,
rooms integer NOT NULL,
theme text NOT NULL,
year integer NOT NULL,
oo integer NOT NULL,
past_rank integer NOT NULL);""")


    
# 
#     cursor.execute(""" INSERT INTO top_hotels(hotel,location,country,region,
#     company,score,rank,rooms,theme,year,oo,past_rank)
#     VALUES(?,?,?,?,?,?,?,?,?,?,?,?)""", (Mylist2[0],Mylist2[1],Mylist2[2],Mylist2[3],
#     Mylist2[4],Mylist2[5],Mylist2[6],Mylist2[7],Mylist2[8],Mylist2[9],Mylist2[10],Mylist2[11])
#     )
#     db.commit()
# cursor.execute("SELECT * FROM top_hotels")
# print(cursor.fetchall())

cursor.execute("SELECT * FROM top_hotels")
a = cursor.fetchall()
#     print(x)
#     
# cursor.execute("SELECT * FROM top_hotels ORDER BY Year")
# for x in cursor.fetchall():
#     print(x)
# 
# cursor.execute("SELECT * FROM top_hotels WHERE Year = 2010")
# for x in cursor.fetchall():
#     print(x)



# cursor.execute("UPDATE top_hotels SET hotel = 'HI' WHERE id=1")
# for x in cursor.fetchall():
#     print(x)
# db.commit()

# user_country=input("Enter a country to see hotels from that country")
# cursor.execute("SELECT * FROM top_hotels WHERE country=?",[user_country])
# for x in cursor.fetchall():
#     print(x)

user_country=input("Enter a country")
for line in a:
    if user_country in line:
        print(line)
        
user_region=input("Enter a region")
for line in a:
    if user_region in line:
        print(line)
        
user_rooms=input("Enter the minimum number of rooms")
for line in a:
    if user_rooms =< Rooms in line:
        print(line)




     


    

