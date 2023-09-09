import pandas as pd
from bs4 import BeautifulSoup as bs
import re

yt = pd.read_excel("YouTubers.xlsx")
air = pd.read_excel("airtable_creators.xlsx")

data = {
    "Username": [],
    "Content": [],
    "Channel": [],
    "Followers": [],
    "URL": [],
}

for index, row in yt.iterrows():
    # get username
    not_duplicate = True
    url = row[2]
    # print(row[2])
    match = re.match(r"https://www\.youtube\.com/c/(\w+)", str(url))

    if match:
        username = match.group(1)
        for index_air, row_air in air.iterrows():
            if username == row_air[0]:
                not_duplicate = False
    else:
        continue

    if not_duplicate and match:
        data["Username"].append(username)
    else:
        continue

    # get content
    content = row[1]
    if pd.notna(content):
        data["Content"].append(content)
    else:
        data["Content"].append("")  # Handle missing content by adding an empty string

    # get channel
    data["Channel"].append("YouTube")

    # get followers
    data["Followers"].append(row[3])

    # get link
    data["URL"].append(row[2])


# Debugging: Check the lengths of the lists
print("Username:", len(data["Username"]))
print("Content:", len(data["Content"]))
print("Channel:", len(data["Channel"]))
print("Followers:", len(data["Followers"]))
print("URL:", len(data["URL"]))


final_data = pd.DataFrame(data=data)
final_data.to_excel("creators.xlsx")
