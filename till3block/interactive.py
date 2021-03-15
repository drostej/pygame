import psycopg2
import csv
import pandas as pd
import argparse
import logging

logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)
con = psycopg2.connect(database="winback", user="winback", password="winback", host="localhost", port="5432")

# ein logging gibt gezielter Aufschluss über das was Programm macht als print Befehle. Durch die log level prod, dev, info kann
# konfiguriert werden, wie geschwätzig ein logging ist. Auf dev Maschinen ist meistens dev (hier z.B: logging.dev("Ich bin ein develeopemt logging") konfigurieret, damit die Entwickler viele Informationen von
# der Anwendung erhalten. Auf prod ist es meist info (hier z.B: logging.info("Ich bin ein prod/validation logging"), wo nur wichtige geschäftsrelevante Inhalte in das logfile geschrieben werden. Dieses Skript schreibt
# das file example.log.

#print("Database opened successfully")
logging.info("datase opend successfully")
# SQL-Befehl ausführen
cursor = con.cursor()
SQLBefehl = 'SELECT name, einwohner FROM land'
cursor.execute(SQLBefehl) # sendet den SQL-Befehl an die Datenbank, die diesen ausführt.
# Dabei werden noch keine Daten auf den Client übertragen.

# Durchlaufen der Ergebnisse
row=cursor.fetchone() #wird der erste Datensatz gelesen und in der Liste row gespeichert
while (row!=None): #Weitere Aufrufe der Methode liefern dann die folgenden Datensätze.
    #print(row[0], row[1])
    logging.debug(row[0], row[1])
    row = cursor.fetchone() #Ist der letzte Datensatz erreicht, wird von der Methode None zurückgegeben.

dland = "SELECT * FROM land WHERE name LIKE 'D%'"
sql = "SELECT * FROM land"
cursor.execute(sql)
row = cursor.fetchone()
while (row!=None):
    print(row)
    row= cursor.fetchone()

#export to csv without header
cursor.execute(dland)
results = cursor.fetchall()
with open("dland.csv", "w") as file:
    for row in results:
        csv.writer(file).writerow(row)

#export to csv with header
sql_query = pd.read_sql_query("SELECT * FROM land"
                              ,con) # here, the 'con' is the variable that contains your database connection information from step 2

df = pd.DataFrame(sql_query)
df.to_csv (r'export_abcd_data.csv', index = False) # place 'r' before the path name to avoid any errors in the path
logging.info("file written")


# Ende der Verarbeitung
cursor.close()
con.close()
logging.info("database connection closed")
# README:
# Cursor sind Objekte, die es erlauben, die Datensätze aus einer Datenbank-Anfrage auszulesen.
# https://www.inf-schule.de/information/datenbanksysteme/zugriff/pythonzugriff/konzept_cursor


query = "SELECT * FROM land WHERE name LIKE \'" + "g" + "%\'"
continent = "SELECT * FROM land WHERE kontinent = \'" + "europe" + "\'"
