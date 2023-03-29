import pyodbc
import sqlite3

# # connection with source
conn_source = sqlite3.connect("task.db")
c_source = conn_source.cursor()

# connection with destination
conn_dest = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=GGKU5DELL1917;'
    'DATABASE=hello;'
    'Trusted_Connection=yes;'
)
c_dest = conn_dest.cursor()
c_dest.execute(
    """
    Create table AlbumFulldetails
    (
        ID int identity(1,1),
        Albumname nvarchar(50),
        Trackname nvarchar(50),
        Length nvarchar(50)
    )
    """
)

data = c_source.execute("""
                Select A.AlbumName,T.TrackName,T.Length from Albumdetails A
                inner join TrackDetails T on A.ID=T.AlbumID 
                 """).fetchall()

for d in data:
    c_dest.execute("""
                    Insert into AlbumFullDetails(Albumname,Trackname,Length) Values(?,?,?)
    """, (d[0], d[1], d[2]))

conn_dest.commit()
conn_dest.close()
conn_source.close()
