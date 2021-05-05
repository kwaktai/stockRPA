from httplib2 import Http
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
# Google API 요청 시 필요한 권한 유형
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
# 구글 시트 ID
SPREADSHEET_ID = '1TH5ix1ioiQwcsAsVboXFLAjtX3UQ2hXAYG4AvBultE8'


def main():
    values = [
        ['이건', '첫 번째', '행입니다.'],
        ['첫 번째'],
        ['열입니다.'],
    ]
    body = {
        'values': values
    }

    # json 파일로 서비스 계정 credential 정의
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        '/Users/taikwak/TaiCloud/Documents/Project/stockRPA/key2.json', SCOPES)
    http_auth = credentials.authorize(Http())
    service = build('sheets', 'v4', http=http_auth)

    # 업데이트 요청 및 실행
    request = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID,
                                                     range='시트1!A1:D3',  # 2
                                                     valueInputOption='RAW',
                                                     body=body)
    request.execute()


if __name__ == '__main__':
    main()
