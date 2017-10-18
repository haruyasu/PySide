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
# sh.update_acell('B2', "update")

# get cell_list
# cell_list = sh.range('A1:D4')
# print cell_list

# read and write
f = open('result.txt')
line = f.readline()

while line:
    if line == "\n":
        print "Empty"
    else:
        words = line.split()
        worksheet = wb.worksheet(words[0])
        values_list_retsu = worksheet.col_values(1)
        values_list_gyo = worksheet.row_values(1)

        for h in values_list_gyo:
            for i in values_list_retsu:
                if i == words[1]:
                    worksheet.update_acell('E5', words[2])

    line = f.readline()
f.close