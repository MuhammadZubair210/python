# import trying
# car = trying.Car("2019",2500)
# car.getSpeed("2019")


import sqlite3
conn = sqlite3.connect("tutorial.db")
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL,datestamp TEXT,keyword TEXT, value REAL)')

def data_entry():
    print("working")
    c.execute("INSERT INTO stuffToPlot VALUES(1453232342343, '2018-6-6', 'python', 55)")
    conn.commit()
    c.close()
    conn.close()

def getAll():
    c.execute("SELECT * FROM stufftoPlot")
    for row in c.fetchall():
        print(row)
    # c.close()

# create_table()
# data_entry()
getAll()