import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.instagram.com", "instagram.com",
                "https://outlook.live.com/mail/0/inbox", "www.outlook.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("this is your working hour A##, concentrate dumbo!!")
        # r+ is used to simultaenously read and then accordingly write onto it.
        with open(hosts_temp, 'r+') as file:
            content = file.read()
            print(content)

    else:
        print("yeah you can chill now zuckerrrr")
    # print(1)
    time.sleep(5)
