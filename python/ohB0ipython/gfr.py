import requests
import pprint
import csv


def get_user(user):
    url = "URL"

    payload = "LoginName="+str(user)+"&UserType=Gfrusers" # will vary depending on API

    headers = {
        'X-TR-API-APP-ID': '', # missing
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': '' # missing auth key
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json().get('lastLogin')


users = ['userid%40domain.com.xh6', 'userid2'] # will vary by contents of list as well as with the payload


with open('gfrlastLogin.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["loginName", "lastLogin"])
    for user in users:
        print(get_user(user))
        writer.writerow([user, get_user(user)])
        next(iter(user))
