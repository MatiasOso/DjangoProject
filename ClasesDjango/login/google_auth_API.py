# En tu aplicación Django, crea un archivo para manejar las interacciones con Google Drive
from google.oauth2 import service_account
from googleapiclient.discovery import build

def get_drive_service():
    SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
    SERVICE_ACCOUNT_FILE = 'path/to/service_account_key.json'  # Ruta al archivo JSON de la cuenta de servicio

    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    
    service = build('drive', 'v3', credentials=creds)
    return service

def get_recipe_image_url(file_id):
    drive_service = get_drive_service()
    file = drive_service.files().get(fileId=file_id, fields='webViewLink').execute()
    return file.get('webViewLink')
