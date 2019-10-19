from datetime import datetime as dt
import time 
host_temp = 'hosts'
host_path = r'C:\Windows\System32\Drivers\etc\hosts'
web_list = ['www.facebook.com','facebook.com','www.netflix.com']
redirect = '127.0.0.1'
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,8,30):
        print('Working hours ...')
        with open(host_path, 'r+') as file:
            content = file.read()
            for website in web_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + ' ' + website + '\n')
    else:
        with open(host_path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in web_list):
                    file.write(line)
            file.truncate()
        print('Fun hours ...')
    time.sleep(5) 

