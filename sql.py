# %%
import sqlite3

# %%
## connect to sqlite
connection=sqlite3.connect("student.db")

# %%
## insert a cursor object to insert record, create table, retreive
cursor=connection.cursor()

# %%
## create the table
table_info="""
Create table STUDENT( NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT);

"""

# %%
cursor.execute(table_info)

# %% [markdown]
# # insert some more records

# %%
cursor.execute('''Insert Into STUDENT values('Bethel','Data Science','A','90' )''')
cursor.execute('''Insert Into STUDENT values('Mike','Data Science','B','100' )''')
cursor.execute('''Insert Into STUDENT values('Chidera','Data Science','A','84' )''')
cursor.execute('''Insert Into STUDENT values('Blessing','DEVOPS','A','50' )''')
cursor.execute('''Insert Into STUDENT values('Jennifer','DEVOPS','A','35' )''')

# %%
## display all the records
print("The inserted records are")

# %%
data=cursor.execute('''Select * From STUDENT''')

# %%
for row in data:
    print(row)

 ## Close the connections

# %%
connection.commit()
connection.close   
