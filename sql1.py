import sqlite3
a=sqlite3.connect("College.db")

c=a.cursor()

c.execute("Drop table if exists student")

c.execute("""
create table student(
s_id integer,
s_name text,
s_age integer,
s_course text,
s_marks integer
)
""")

c.execute("""
insert into student values (21,"Sirisha",17,"python",89),
insert into student values (20,"vyshu",16,"Java",80),
insert into student values (80,"Sailu",18,"c",90),
insert into student values (22,"Tulasi",17,"C",85),
insert into student values (30,"Varsha",15,"Html",78)]


""")



data=[ (20,"vyshu",16,"Java",80),
(80,"Sailu",18,"c",90),
(21,"Sirisha",18,"Python",89),
(22,"Tulasi",17,"C",85),
(30,"Varsha",15,"Html",78)]

c.executemany("insert into student values(?,?,?,?,?)",data)

c.execute("update student set s_marks=70 where s_name='Sailu'")





a.commit()

p=c.execute("select * from student where s_course='Python'")

for x in p:
    print(x)



