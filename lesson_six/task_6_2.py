# реализация доступа к сохранненой базе данных
import pickle

dbfile = open('sales_pickle', 'rb')
db = pickle.load(dbfile)
for key in db:
    print(key, '=>\n', db[key])
print(db['sales_amounts']['1'])