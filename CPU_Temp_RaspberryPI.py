"""
#!/usr/bin/env python
#title           :CPU_Temp_RaspberryPI.py
#description     :Monitoring and reading internal temperature of Raspberry PI (Inside)
#author          :Fajar Muhammad Noor Rozaqi
#date            :2022/07/30
#version         :0.1
#usage           :Python
#notes           :
#python_version  :3.0/2.0 (higher version)
#==============================================================================
"""

#library
import time
import datetime
# import pymysql #uncomment if you use pymsql library
# mport csv #uncomment if you use csv library
# import numpy as np #uncomment if you use numpy library

while True:
    try:
        #temperature
        from gpiozero import CPUTemperature
        cpu = CPUTemperature()
        #time
        timer = datetime.datetime.now()
        print("Time                    :",timer.strftime("%Y-%m-%d %H:%M:%S"))
        print("Temperature Raspberry Pi:",cpu.temperature)
        print("")
        
        #Database Connection
        #Uncomment this below script, if you also use the RDS (Relational database service) for MySQL Database
        #Change the [host],[user],[password], and [db] with your own]
        
        db = pymysql.connect(host='*****',
                     user='****',
                     password='****',
                     db='*****',
                     charset='utf8',
                     cursorclass=pymysql.cursors.DictCursor)
        cur = db.cursor()
        
        try:
              #Uncomment this below script, if you also use the RDS (Relational database service) for MySQL Database
              #Change with your own name version of querry
          
            add_c1 ="INSERT INTO `cpu_temperature`(temperature,time,raspi_id) VALUES(%s,%s,%s)"
            cur.execute(add_c1,(cpu.temperature,
                                timer.strftime("%Y-%m-%d %H:%M:%S"),
                                int(1)))
            db.commit()
            
            time.sleep(2)
            
            #Reading Record Database
            try:
                #Database Connection
                #Uncomment this below script, if you also use the RDS (Relational database service) for MySQL Database
                #Change the [host],[user],[password], and [db] with your own]
              
                db = pymysql.connect(host='****',
                     user='****',
                     password='****',
                     db='****',
                     charset='utf8',
                     cursorclass=pymysql.cursors.DictCursor)
                db.cursor()

                #Uncomment this below script, if you also use the RDS (Relational database service) for MySQL Database
                #Change with your own name version of querry
    
                with db.cursor() as cursor:
                    sql = "SELECT (temperature),(time),(raspi_id) FROM `cpu_temperature`"
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    print(result)
                
                 #Uncomment this below script, if you also use want to converting the file into CSV format
                 #Change with your own name version of querry
      
                Temperature =[]
                Time =[]
                Raspi_id =[]
                 
                #Converting into CSV File
                filename = "/home/pi/temperaturelog.csv"
                with open(filename, mode='w', newline='') as file:
                    a = csv.writer(file, delimiter =',')
                    a.writerow(['Temperature','Time','Raspi_id'])
                    for i in range(0, len(result)):
                        a.writerow(result[i].values())
                        Temperature.append(result[i]['temperature'])
                        Time.append(result[i]['time'])
                        Raspi_id.append(result[i]['raspi_id'])
                
                print("CSV is converted")
                print("")
                time.sleep(0)
  
            except:
                print("CSV is not converted")
                print("")
                time.sleep(0)
        except:
            db.rollback()
            print("Database is not connected")
            
        time.sleep(0)
        
    except:
        pass
