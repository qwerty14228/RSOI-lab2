import requests


class LibraryClient:
    def __init__(self, api_url):
        self.api_url = api_url
    
    def get_libraries(self):
        response = requests.get(f'{self.api_url}/libraries')
        return response.json()
