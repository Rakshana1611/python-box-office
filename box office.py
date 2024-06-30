import pandas as pd
view_data=pd.read_csv(r"C:\Users\RAKSHANA\OneDrive\Desktop\Besant\assignment\dataset.csv")
print(view_data)
view_data.fillna({
    'Movie Name': 'Unknown',
    'Movie ratings': 0,
    'Movie Characters Count': 0,
    'Year': 0,
    'Director': 'Unknown'
}, inplace=True)
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="movies"
)
mycursor=mydb.cursor()
for index,row in view_data.iterrows():
    sql="insert into dataset values(%s,%s,%s,%s,%s)"
    val=(row['Movie Name'],row['Movie ratings'],row['Movie Characters Count'],row['Year'],row['Director'])
    mycursor.execute(sql,val)
mydb.commit()
print("data saved successfully")