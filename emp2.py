import sqlite3
a=sqlite3.connect("emp.db")

c=a.cursor()


c.execute("DROP TABLE IF EXISTS employees")

c.execute("""
create table employees(
empid integer primary key,
empname text,
empph integer 
)

""")

data=[
    (25,"Siri",6300654500),
   (80,"Sri",9701238907),
   (75,"Bashi",9010234532),
   (20,"Bhagya",9010234532)
]

c.executemany("insert into employees values (?,?,?)",data)

c.execute("update employees set empid=85 where empname='Siri'")


c.execute("select empname,count(*) from employees group by empname")



a.commit()  
p=c.execute("select * from employees")
for i in p:
    print(i)

priny(p.fetchone())
print(p.fetchall())

a.close()