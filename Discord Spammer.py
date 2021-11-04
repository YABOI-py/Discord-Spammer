Discord Spammer
import requests
import time
import string
import random
from random import choice

def main():

    token = "x"

    start = input("channel name => ")
    if len(start) > 10:
        print("use a short name nigger\n")
        main()
    else:
        serverid = input("what is the server ID => ")
        url = "(serverid)

        catergoryID = input("what is the category ID => ")

        headers = {"content-type": "application/json", "authorization": token}

    while True:

        stringg = string.ascii_letters + string.digits
        message = "".join(random.choice(stringg)for i in range(20))

        channelname = "{}-{}".format(start, message)
        data = {"name": channelname, "parent_id": catergoryID}


        time.sleep(0.2)
        r = requests.post(url, headers=headers, json=data)

        if r.status_code == 201:
            print("succesfully made a channel")
        else:
            print("ur being rate limited or account is probably locked lol")


if name == "main":
    main()