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

a.commit()
a.close()