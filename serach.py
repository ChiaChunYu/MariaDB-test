import mysql.connector

# 建立連線
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="411021390",
  database="newdatabase"
)

mycursor = mydb.cursor()

# 獲取資料庫中所有資料表的名稱
mycursor.execute("SHOW TABLES")
tables = mycursor.fetchall()

# 對每個資料表執行 SELECT 查詢
for table in tables:
    table_name = table[0]
    print(f"Table: {table_name}")
    mycursor.execute(f"SELECT * FROM {table_name}")
    result = mycursor.fetchall()
    for row in result:
        print(row)

# 關閉連線
mydb.close()
