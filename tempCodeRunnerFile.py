import requests
import sys

if len(sys.argv)!=2:
    sys.exit()

response=requests.get("https://www.flipkart.com/search?q=apple+mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&as-pos=1&as-type=RECENT&suggestionId=apple+mobiles%7CMobiles&requestId=74513d15-9fcc-41ea-a7e0-16499e689ee3&as-backfill=on&otracker=nmenu_sub_Electronics_0_Apple")
print(response.json())