from rsoi_gateway_app.clients.abstract import *


class MockLibraryClient(AbstractLibraryClient):
    def get_libraries(self, city='', page=1, size=10):
        data = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": 1,
                    "library_uid": "83575e12-7ce0-48ee-9931-51919ff3c9ee",
                    "name": "Библиотека имени 7 Непьющих",
                    "city": "Москва",
                    "address": "2-я Бауманская ул., д.5, стр.1"
                }
            ]
        }
        items = data['results']
        for item in items: 
            item['libraryUid'] = item['library_uid']
            del item['library_uid']
        return {"page": page, "pageSize": size, "totalElements": data["count"], "items": items}

    def get_library_books(self, library_uid='', book_uid=None, page=1, size=10, show_all=False): 
        raise NotImplementedError()
    
    def get_library_book(self, library_uid=None, book_uid=None):
        raise NotImplementedError()
    
    def update_book_available_count(self, user=None, library_book_id=None, available_count=0):
        raise NotImplementedError()