from googleapiclient.discovery import build
api_key = "AIzaSyAbuQmPrj70BagkqN5czCMmiav7hS3OEB8"
youtube = build('youtube', 'v3', developerKey=api_key)
request = youtube.channels().list(
    part="statistics",
    forUsername="schafer5"
)
r = request.execute()
print(r)