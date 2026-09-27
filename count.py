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




data=[ (20,"vyshu",16,"Java",80),
(80,"Sailu",18,"c",90),
(21,"Sirisha",18,"Python",89),
(22,"Tulasi",17,"C",85),
(30,"Varsha",15,"Html",78),
(1,"Siri",14,"Css",90),
(2,"Bashi",17,"AIML",80),
(3,"Sravya",19,"MPC",75),
(4,"Bhavana",17,"CCN",80),
(5,"Bhagya",15,"ECE",86),
(6,"Srii",18,"CME",89),
(7,"Janu",15,"CME",90),
(8,"Tanuu",17,"Python",75),
(9,"Josh",16,"C",80),
(10,"Purna",17,"Java",67)]

c.executemany("insert into student values(?,?,?,?,?)",data)



a.commit()
p=c.execute("select count (*) from student")

for x in p:
    print(x)
