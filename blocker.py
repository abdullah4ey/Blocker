import time
from datetime import datetime as dt
#very important pyw python files run at the background without any command line
#make a copy of host file
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
hosts_temp="hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","dub119.mail.live.com","www.dub119.mail.live.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,15) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
                    print ("workking")
    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            #move the cursor to the top so the latest result stays at the top
            #jo text ka result hai wo neechay janay ka bajai uper ata hai us ki waja say truncate poorana process
            #delete kerta hai.
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                    print("working time")
            file.truncate()
            #truncate deletes duplicated text created by the loop
    #time.sleep()
