from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/calendar']

def authenticate():
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
    return build('calendar', 'v3', credentials=creds)

def create_event(service, summary, start, end):
    event = {
        'summary': summary,
        'start': {'dateTime': start},
        'end': {'dateTime': end},
    }
    return service.events().insert(calendarId='primary', body=event).execute()

def get_events(service):
    events = service.events().list(calendarId='primary').execute()
    return events.get('items', [])
