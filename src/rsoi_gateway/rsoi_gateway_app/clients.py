import requests


class LibraryClient:
    def __init__(self, api_url):
        self.api_url = api_url
    
    def get_libraries(self, city='', page=1, size=10):
        response = requests.get(f'{self.api_url}/libraries', params={"city": city, "page": page, "size": size})
        data = response.json()
        items = data['results']
        for item in items: 
            item['libraryUid'] = item['library_uid']
            del item['library_uid']
        return {"page": page, "pageSize": size, "totalElements": data["count"], "items": items}

    def get_library_books(self, library_uid='', page=1, size=10, show_all=False): 
        params = {'library__library_uid': library_uid, 'page': page, 'size': size}
        if not show_all:
            params['available_count__gt'] = 0
        response = requests.get(f'{self.api_url}/library_books', params=params)
        data = response.json()
        items = data['results']
        for item in items: 
            del item['library']
            item['bookUid'] = item['book']['id']
            del item['book']
            item['availableCount'] = item['available_count']
            del item['available_count']
        return {"page": page, "pageSize": size, "totalElements": data["count"], "items": items}