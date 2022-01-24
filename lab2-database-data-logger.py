import sqlite3

dbconnect = sqlite3.connect("sensorDB.db")
dbconnect.row_factory = sqlite3.Row
cursor = dbconnect.cursor() 

from sense_hat import SenseHat
sense = SenseHat()
sense.clear()

for i in range(10):
	t = sense.get_temperature()
	p = sense.get_pressure()
	h = sense.get_humidity()

	t = round(t, 1)
	p = round(p, 1)
	h = round(h, 1)

	cursor.execute('''insert into sensordata values(?, ?, ?, ?,date('now'), time('now'))''', (i, t, h, p));
dbconnect.commit();
dbconnect.close();
