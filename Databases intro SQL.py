import sqlite3
with sqlite3.connect("company.db") as db:
    cursor=db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS employees(id integer PRIMARY KEY,
name text NOT NULL,
dept text NOT NULL,
salary integer);""")

#cursor.execute("""Insert into employees(id,name,dept,salary)
#VALUES("1","Bob","Sales","25000")""")
#db.commit()

newId=input("Enter id number")
newName=input("Enter a name")
newDept=input("Enter a department")
newSalary=input("enter salary")
cursor.execute("""INSERT INTO employees(id,name,dept,salary)
VALUES(?,?,?,?)""",(newId,newName,newDept,newSalary))
db.commit()

cursor.execute("SELECT*FROM employees")
print(cursor.fetchall())

#db.close()

cursor.execute("SELECT * FROM employees")
for x in cursor.fetchall():
    print(x)

cursor.execute("SELECT * FROM employees ORDER BY name")
for x in cursor.fetchall():
    print(x)
    
cursor.execute("SELECT * FROM employees WHERE salary>20000")

cursor.execute("SELECT * FROM employees WHERE dept='Sales'")

cursor.execute("SELECT id,name,salary FROM employees")

whichDept=input("Enter a department")
cursor.execute("SELECT * FROM employees WHERE dept=?",[whichDept])
for x in cursor.fetchall():
    print(x)
    
cursor.execute("UPDATE employees SET name = 'Tony' WHERE id=1")


    
    

    
