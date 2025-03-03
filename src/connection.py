from pymongo import MongoClient
client = MongoClient('mongodb+srv://vijay_carmods:khmdsunaNivJ45d52vsfh@car-mod.yytzf.mongodb.net/?retryWrites=true&w=majority&appName=car-mod')
db = client['batman-car-mods']
add_datas = db['add_datas']
