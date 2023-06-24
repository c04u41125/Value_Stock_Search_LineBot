import os
import pickle
from google.auth.transport.requests import Request
import pandas as pd
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
def to_drive(userid):
    # 憑證檔案路徑
    credentials_path = 'credentials.json'

    # 權限範圍，此處為完全授權
    SCOPES = ['https://www.googleapis.com/auth/drive']

    def authenticate():
        """進行身份驗證並建立 Google Drive 服務"""
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    credentials_path, SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        return creds

    def upload_file(file_path):
        """上傳本機端 Excel 檔案至 Google Drive"""
        creds = authenticate()
        service = build('drive', 'v3', credentials=creds)

        file_metadata = {
            'name': os.path.basename(file_path),
            'mimeType': 'application/vnd.ms-excel'
        }
        media = MediaFileUpload(file_path, mimetype='application/vnd.ms-excel')
        file = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()

        return file.get('id')

    def set_permission(file_id):
        """開啟檔案的所有權限"""
        creds = authenticate()
        service = build('drive', 'v3', credentials=creds)

        permission = {
            'type': 'anyone',
            'role': 'writer'
        }
        service.permissions().create(
            fileId=file_id,
            body=permission
        ).execute()

    def get_download_link(file_id):
        """取得下載連結"""
        creds = authenticate()
        service = build('drive', 'v3', credentials=creds)

        file = service.files().get(
            fileId=file_id,
            fields='webViewLink'
        ).execute()

        return file.get('webViewLink')

    # 上傳本機端 Excel 檔案
    file_id = upload_file("output"+userid+".xlsx")

    # 開啟檔案的所有權限
    set_permission(file_id)

    # 取得下載連結
    download_link = get_download_link(file_id)
    
    return download_link
# to_drive('hank1125')