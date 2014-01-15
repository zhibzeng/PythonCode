import sqlite3
def convert(value):
    if value.startswith('~'):
        return value.strip('~')
    if not value:
        value='0'
    return float(value)
conn = sqlite3.connect('foods.db')
curs = conn.cursor()
curs.execute('''
CREATE TABLE food5(
id TEXT PRIMARY KEY,
desc TEXT,
water FLOAT,
kcal FLOAT,
protein FLOAT,
fat FLOAT,
ash FLOAT,
carbs FLOAT,
fiber FLOAT,
sugar FLOAT
)
''')
query = 'INSERT INTO food5 VALUES (?,?,?,?,?,?,?,?,?,?)'
for line in open('ABBREV.txt'):
    fields = line.split('^')
    vals = [convert(f) for f in fields[:10]]
    curs.execute(query,vals)
conn.commit()
conn.close()
