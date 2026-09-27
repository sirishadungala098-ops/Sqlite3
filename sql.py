import sqlite3
a=sqlite3.connect("emp.db")

c=a.cursor()

c.execute("""
create table employee(
empid integer,
empname text,
empph integer
)

""")

a.commit()