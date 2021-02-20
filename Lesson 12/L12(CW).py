import pymongo

string = "mongodb+srv://root:root@cluster0.sygbz.mongodb.net/<dbname>?retryWrites=true&w=majority"

client = pymongo.MongoClient(string)
collection = client["MyDataBase"]["Test1"]

# Сохранение (добавление)
data = {"Name": ["Кирил", "Игорь"]}
collection.save(data)

# Получение (простое)
result = collection.find()[0]
print(result)

# Получение (сложное)
for line in collection.find():
    if line['Name'] == ["Кирил", "Игорь"]:
        result = line
print(result)

# Удаление
collection.delete_many({"Name": ["Кирил", "Игорь"]})

# Обновление данных
collection.update_many({"Name": ["Кирилл", "Игорь"]}, {"$set": {"Name": ["Кирилл", "Игорь", "Аня"]}})

client = pymongo.MongoClient(string)
collection2 = client["MyDataBase"]["Test2"]
data2 = {"Немного обо мне": ["Начинающий программист, есть опыт в написании телеграмм-ботов и сайтов"]}
collection2.save(data2)
collection2.update_many({"Немного обо мне": ["Знаком с работой с базами данных"]})
