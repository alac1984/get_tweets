class Response:
    def __init__(self, errors: list = list(), content: dict = dict()) -> None:
        self.errors = errors
        self.content = content

    def add_error(self, name: str, message: str) -> None:
        self.errors.append({"name": name, "message": message})

    def has_error(self) -> bool:
        return len(self.errors) > 0

    def __bool__(self):
        return True if not self.has_error else False
