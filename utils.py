from pymongo import MongoClient

connection_string="mongodb+srv://yathribtravelsystem:hlmX7YK4cD8td8wC@cluster0.ilrd5xy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(connection_string)
db = client['db_name']

# connection_string = mongodb+srv://<username>:<password>@<atlas cluster>/<myFirstDatabase>?retryWrites=true&w=majority