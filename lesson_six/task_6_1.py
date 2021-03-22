# сохранить записи в файле
from task_6 import db
import pickle

dbfile = open('sales_pickle', 'wb')
pickle.dump(db, dbfile)
dbfile.close()