import json
import pymongo
a = open('product_1.json','r')
a = a.read()
b = json.loads(a)
c = b["data"][0]["techFeatures"]["fit"][0]["ID"]
d = b["data"][0]["techFeatures"]["warmth"][0]["ID"]
e = b["data"][0]["techTemplateName"]

jstext = {
    'test1':c,
    'test2':d,
    'test3':e,
}


myclient = pymongo.MongoClient(host='localhost',port=27017)
mydb = myclient["jstest"]
mycol = mydb["jstext"]
# mycol.insert_one(jstext)
z = mycol.find_one({'test1':c})
print(z)
