import json
import gspread
import oauth2client.client

json_key = json.load(open('API Project-6e755c855745.json'))
scope = ['https://spreadsheets.google.com/feeds']
credentials = oauth2client.client.SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
gc = gspread.authorize(credentials)

wb = gc.open("test")
sh = wb.worksheet("sheet1")

# change cell_value
sh.update_acell('B2', "update")

# get cell_list
cell_list = sh.range('A1:D4')
print cell_list
