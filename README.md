# Web-Scrapping-with-Sqlite

This repository is aimed to have basic understanding of Web Scrapping, Sqlite and Pyodbc 

There are three task to understand these concepts: -

## Task1

Do Web Scrapping using BeautifulSoup of site "https://en.wikipedia.org/wiki/Linkin_Park_discography" and make separate csv files of the albums. Each csv file should be
named as **"AlbumName.csv"**. Each CSV file shoud contain all the tracks of that particular album with their corresponding length.

## Task 2

Now insert the data of all the csv files into the sqlite database. 
Make two tables

**Table 1**: AlbumDetails (Id, AlbumName)

**Table 2**: TrackDetails (Id, AlbumId, TrackName, Length)

## Task 3

Connet sqlite with MSSQL using pyodbc and make a table in MSSQL which will contain all the data into single table.

**Table** : AlbumFullDetails (Id, AlbumName, TrackName, Length)
