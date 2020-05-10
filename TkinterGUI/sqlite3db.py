import sqlite3

def creat_table():
    
    conn=sqlite3.connect("lite.db") #creates a connection and new database or to exsitin
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")#sql code needs to be in quotes
    conn.commit()
    conn.close()
    #cmd ] to indent lines 
    
def insert(item,quantity,price):
    conn=sqlite3.connect("lite.db") #creates a connection and new database or to exsitin
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?)", (item,quantity,price))
    conn.commit()
    conn.close()
    


def view():
    conn=sqlite3.connect("lite.db") #creates a connection and new database or to exsitin
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn=sqlite3.connect("lite.db") #creates a connection and new database or to exsitin
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn=sqlite3.connect("lite.db") #creates a connection and new database or to exsitin
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity,price,item))
    conn.commit()
    conn.close()

#insert("water glass", 10, 5)
#delete("cofee cup")
update(12,6,"water glass")
print(view())
    
    
    
    