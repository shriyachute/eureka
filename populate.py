from canvasapi import canvas
import sys
import requests
from dateutil import parser
import pytz

API_URL = "https://vt.instructure.com/api/v1/assignments"

API_KEY = sys.argv[1]

req_str = requests.get("https://vt.instructure.com/api/v1/users/self/todo?access_token=" + API_KEY)

json_obj = req_str.json()
with open('data.txt', "w") as dataFile:
    dataFile.write(json_obj.assignment)

for assignment in json_obj:
    due_date = parser.parse(assignment['assignment']['due_at']).astimezone(pytz.timezone("US/Central"))
    dataFile.write(assignment['assignment']['name']
            + " due " + due_date.strftime("%A %b %d")
            + " at " + due_date.strftime("%-I")
            + ":" + due_date.strftime("%M %p") + "\n\n")