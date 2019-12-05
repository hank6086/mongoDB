import pymongo
 
myclient = pymongo.MongoClient(host='localhost',port=27017)
mydb = myclient["test"]
mycol = mydb["student"]

dblist = myclient.list_database_names()
#dblist = myclient.database_names() 

student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
}
x = mycol.insert_one(student)
print(x)
if "test" in dblist:
  print("数据库已存在！")