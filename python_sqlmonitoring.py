

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 14:25:03 2018

@author: abhimanyu
"""

import mysql.connector
from slackclient import SlackClient
import json

#connecting to database 
mydb = mysql.connector.connect(
  host="localhost",
  user="xxxx",
  passwd="xxxxx",
  database="xxxxxx"
)

mycursor = mydb.cursor()    
    
#table_schema will contain database name
#sql_query1 is used to fetch table name and store it in a list table_list
table_list = []
sql_query1 = "SELECT  table_name from  INFORMATION_SCHEMA.TABLES  WHERE TABLE_SCHEMA = 'xxxxx';"
mycursor.execute(sql_query1)
table_list.extend(mycursor.fetchall())

#sql_query2 fetches the data type of the id,for example if it is int, mediumint or bigint 
#store the value in a list - lst_type
lst_type = []
for x in table_list:
   # print (x)
    sql_query2 = "SELECT Data_type  FROM  INFORMATION_SCHEMA.COLUMNS  WHERE TABLE_SCHEMA = 'xxxxx' AND  table_name = %s AND COLUMN_NAME = 'id'  ;"
    mycursor.execute(sql_query2,x)
    lst_type.extend(mycursor.fetchall())
print(lst_type)

#sql_query3 fetches the auto incremented values and stores it in lst_id

lst_id = []

for y in table_list :
    #print("table name=",myresult ,"data_type=",y)
  
    sql_query3 = "SELECT `AUTO_INCREMENT` FROM  INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'xxxxx' AND Table_name = %s ;"
    
    mycursor.execute(sql_query3,y)
    
    lst_id.extend(mycursor.fetchall())
print(lst_id)


#this loops prints the table name and its incremented value 
for z, p in zip(lst_id, table_list):
    print("table name=",p,"increment_value=",z)
   
    
#this for loops check if the value is equal to the limit value or not  
#send a alert ot slack with table name
#here we have used three datatypes int , mediumint , bigint.
    
    
val_int = 2147483647
val_mediumint = 8388607
val_bigint = 9223372036854775807
for k, j,l in zip(lst_type, lst_id,table_list):
    if k == val_int and j == "int":
        slack_token = "xxxxx"
        sc = SlackClient(slack_token)
        message=l
        intro_msg  = json.dumps([{"text":"this table have reached auto increment limit xxxx","attachment_type":"default"}])
        sc.api_call(
            "chat.postMessage", 
            channel="#general", 
            text={message}, 
        
        attachments=intro_msg, as_user=True)
        
    if k == val_mediumint and j == "bigint":
        slack_token = "xxxx"
        sc = SlackClient(slack_token)
        message=l
        intro_msg  = json.dumps([{"text":"this table have reached auto increment bigint limit xxxx","attachment_type":"default"}])
        sc.api_call(
            "chat.postMessage", 
            channel="#general", 
            text={message}, 
        
        attachments=intro_msg, as_user=True)
        
    if k == val_bigint and j == "mediumint":
        slack_token = "xxxxxxx"
        sc = SlackClient(slack_token)
        message=l
        intro_msg  = json.dumps([{"text":"this table have reached auto increment mediumint limit xxxx","attachment_type":"default"}])
        sc.api_call(
            "chat.postMessage", 
            channel="#general", 
            text={message}, 
        
        attachments=intro_msg, as_user=True)
          
        
        
        























