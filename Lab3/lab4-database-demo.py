import sqlite3
dbconnect = sqlite3.connect("mydatabase.db");
dbconnect.row_factory = sqlite3.Row;
cursor = dbconnect.cursor();
cursor.execute('''insert into sensors values (1, "door","kitchen")''');
cursor.execute('''insert into sensors values (2, "temperature","kitchen")''');
cursor.execute('''insert into sensors values (3, "door","garage")''');
cursor.execute('''insert into sensors values (4, "motion","garage")''');
cursor.execute('''insert into sensors values (5,"temperature","garage")''');
dbconnect.commit();
cursor.execute('SELECT * FROM sensors WHERE type = "door" ');

for row in cursor:
	print(row['sensorID'],row['type'],row['zone']);

cursor.execute('SELECT * FROM sensors WHERE zone = "kitchen"');
for row in cursor:
        print(row['sensorID'],row['type'],row['zone']);
dbconnect.close();


