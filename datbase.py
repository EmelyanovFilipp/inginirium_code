import sqlite3


class Database:
    def __init__(self, file):
        self.con = sqlite3.connect(file)

        self.cur = self.con.cursor()
        self.create_table('score')

    def create_table(self, table_name):
        que = f'''CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGRER PRIMARY KEY,
            name TEXT,
            score_point INTEGRER
            )
            '''
        self.cur.execute(que)
        self.con.commit()

    def get(self, qeu='SELECT * FROM score ORDER BY score_point DESC'):
        return self.cur.execute(qeu).fetchall()

    def insert(self, name, score):
        que = f'''INSERT INTO score (name,score_point) VALUES('{name}',{score})'''
        self.cur.execute(que)
        self.con.commit()

    def __del__(self):
        self.con.close()


db = Database('score.sqlite3')
db.insert('tort',4)
db.insert('zero',0)
db.insert('grek',15)
db.insert('man',3)
list = db.get()
list = sorted(list, key=lambda x: -x[2])
for i in list:
    print(i)
