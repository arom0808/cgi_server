#!/usr/bin/env python3
import cgi
import html
import json
from os.path import exists


def user_to_html(number, first_name, last_name):
    return """
        <tr class="text-gray-700">
            <td class="border p-4 dark:border-dark-5">
                """ + str(number) + """
            </td>
            <td class="border p-4 dark:border-dark-5">
                """ + first_name + """
            </td>
            <td class="border p-4 dark:border-dark-5">
                """ + last_name + """
            </td>
        </tr>"""


if not exists("db.json"):
    with open('db.json', 'w') as outfile:
        json.dump([], outfile)

form = cgi.FieldStorage()
first_name = html.escape(form.getfirst("user_first_name", "none"))
last_name = html.escape(form.getfirst("user_last_name", "none"))
if first_name != 'none' and last_name != 'none':
    with open('db.json', 'r') as file:
        users = json.load(file)
    users.append({"first_name": first_name, "last_name": last_name})
    with open('db.json', 'w') as file:
        json.dump(users, file)

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <link type="text/css" rel="stylesheet" href="/style.css">
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")
print("""<form action="/cgi-bin/form.py"> <input type="text" id="simple-email" class=" flex-1 appearance-none border 
border-gray-300 w-full py-2 px-4 bg-white text-gray-700 placeholder-gray-400 shadow-sm text-base focus:outline-none 
focus:ring-2 focus:ring-purple-600 focus:border-transparent" placeholder="Your first name" name="user_first_name"> <input 
type="text" id="simple-email" class=" flex-1 appearance-none border border-gray-300 w-full py-2 px-4 bg-white 
text-gray-700 placeholder-gray-400 shadow-sm text-base focus:outline-none focus:ring-2 focus:ring-purple-600 
focus:border-transparent" placeholder="Your last name" name="user_last_name"> <input type="submit"> </form>""")

users_html = ""
with open('db.json', 'r') as file:
    users = json.load(file)
for i in range(len(users)):
    users_html += user_to_html(i + 1, users[i]["first_name"], users[i]["last_name"])
print("""
<table class="table p-4 bg-white shadow rounded-lg">
    <thead>
        <tr>
            <th class="border p-4 dark:border-dark-5 whitespace-nowrap font-normal text-gray-900">
                #
            </th>
            <th class="border p-4 dark:border-dark-5 whitespace-nowrap font-normal text-gray-900">
                First name
            </th>
            <th class="border p-4 dark:border-dark-5 whitespace-nowrap font-normal text-gray-900">
                Last name
            </th>
        </tr>
    </thead>
    <tbody>""" + users_html + """
    </tbody>
</table>""")

print("""</body>
        </html>""")
