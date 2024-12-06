import requests


class LibraryClient:
    def __init__(self, api_url):
        self.api_url = api_url
    
    def get_libraries(self, city='', page=1, size=10):
        response = requests.get(f'{self.api_url}/libraries', params={"city": city, "page": page, "size": size})
        data = response.json()
        return {"page": page, "pageSize": size, "totalElements": data["count"], "items": data["results"]}
