class ApiException(Exception):
    def __init__(self, errors=[], *args, **kwargs):
        super(ApiException, self).__init__(*args, **kwargs)
        self.errors = errors
