import sqlite3

con = sqlite3.connect("mydatabase.db") # veri tabanı oluşturuyorum
cursor = con.cursor()


# tablo oluşturma
def creating_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS bakkaldefter (isim TEXT, Soyisim TEXT, Sokak TEXT, odenecek_tutar INT)")
    con.commit()

# creating_table()


con.close()