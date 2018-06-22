#! /usr/bin/env 
import psycopg2
import time
def connects():
    return psycopg2.connect("dbname=news")

data1="select title,views from article_view limit 3"
data2="select * from author_view"
data3="select to_char(date,'Mon DD,YYYY') as date,err_prc from err_perc where err_prc>1.0"

def popular_article(data1):
    db=connects()
    c=db.cursor()
    c.execute(data1)
    results=c.fetchall()
    for result in range(len(results)):
        title=results[result][0]
        views=results[result][1]
        print("%s--%d" % (title,views))
    db.close()

def popular_authors(data2):
    db=connects() 
    c=db.cursor()
    c.execute(data2)
    results=c.fetchall()
    for result in range(len(results)):
        name=results[result][0]
        views=results[result][1]
        print("%s--%d" % (name,views))
    db.close()

def error_percent(query3):
    db=connects()
    c=db.cursor()
    c.execute(data3)
    results=c.fetchall()
    for result in range(len(results)):
        date=results[result][0]
        err_prc=results[result][1]
        print("%s--%.1f %%" %(date,err_prc))

if __name__ == "__main__":
  print("THE LIST OF POPULAR ARTICLES ARE:")
  popular_article(data1)
  print("\n")
  print("THE LIST OF POPULAR AUTHORS ARE:")
  popular_authors(data2)
  print("\n")
  print("PERC ERROR MORE THAN 1.0:")
  error_percent(data3)
    
