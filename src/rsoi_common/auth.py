class RsoiUser:

    is_active = True
    is_authenticated = True

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class RsoiAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        username = request.headers.get('x-user-name')

        if username is not None:
            request.user = RsoiUser(username=username)
        
        response = self.get_response(request)

        return response
