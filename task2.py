## Insertion of data from csv file to table using sqlite3

import csv
import sqlite3
from pathlib import Path

conn = sqlite3.connect('task.db')
c = conn.cursor()

c.execute("""CREATE TABLE ALBUMDETAILS
( ID INTEGER PRIMARY KEY AUTOINCREMENT,
AlbumName TEXT
)
""")

c.execute("""CREATE TABLE TRACKDETAILS
( ID INTEGER PRIMARY KEY AUTOINCREMENT,
AlbumID INTEGER,
TrackName Text,
Length Text,
FOREIGN KEY (AlbumID)
    REFERENCES ALBUMDETAILS (ID)
)
""")

path = Path('C:\\Users\\jai.jain\\PycharmProjects\\csvjson').resolve()
files = path.glob("*.csv")
for file in files:
    c.execute("Insert into ALBUMDETAILS(AlbumName) Values(?)", [file.stem])
    a = c.lastrowid
    with open(file, 'r') as track_file:
        csv_reader = csv.DictReader(track_file)

        for i in csv_reader:
            c.execute("Insert into TRACKDETAILS(AlbumID,TrackName,Length)Values(?,?,?)",
                      (a, i['name'], i['length']))
conn.commit()
conn.close()
