import time
from datetime import datetime as dt

temp_hosts_path=r"C:\Users\sohai\PycharmProjects\PythonTutorials\WebsiteBlocker\hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com", "facebook.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("working hours")
        with open(hosts_path, 'r+') as file:
            content= file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_path,'r+') as file:
            content= file.readlines()
            file.seek(0) #when u read file the pointer is at last line using this method it comes on top of the line on starting point
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                file.truncate() #using this it will all the things coming after this
        print("fun hours")
    time.sleep(5)