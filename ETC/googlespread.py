import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive',
]

json_file_name = '/Users/taikwak/TaiCloud/Documents/Project/stockRPA/key.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    json_file_name, scope)
gc = gspread.authorize(credentials)


# spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1TH5ix1ioiQwcsAsVboXFLAjtX3UQ2hXAYG4AvBultE8/edit#gid=0'
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1455vpFLPWAQxlJx1EarMwRr231bfB1LfNqM4MVcPZCA/edit#gid=0'

# 스프레스시트 문서 가져오기
doc = gc.open_by_url(spreadsheet_url)

# 시트 선택하기
worksheet = doc.worksheet('무매1')

cell_data = worksheet.acell('A1').value
print(cell_data)
