import sqlite3
con=sqlite3.connect('my_database.db')
c=con.cursor()

 # create tables
c.execute("""CREATE TABLE contacts(
          name text
          p_no int
          msg text
          date datetime
          email varchar)
          """)
con.commit()
con.close()