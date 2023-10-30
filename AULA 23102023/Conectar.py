import sqlite3



con = sqlite3.connect("tutorial.db")
cur = con.cursor()
try:
    cur.execute("CREATE TABLE times(id, nome, jogadores)")
except:
    print ("erro ao criar")
try:
    cur.execute("""
        INSERT INTO times VALUES
            (1, "IFRS", "Joao, Gustavo"),
            (2, "IFMG", "Alberto, Jorge")
        """)
except:
    print ("erro ao inserir")
con.commit()
res = cur.execute("SELECT * FROM times")
print (res.fetchall())
