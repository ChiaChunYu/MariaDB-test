import mysql.connector

# 建立連線
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="411021390",
  database="newdatabase"
)

mycursor = mydb.cursor()

sql = "DROP TABLE 2023_Q4_獲利能力"

# 執行 SQL 語句
mycursor.execute(sql)

# 提交更改
mydb.commit()

# 確認有多少筆資料被刪除
print(mycursor.rowcount, "record(s) deleted")

# 關閉連線
mydb.close()
