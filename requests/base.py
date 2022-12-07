class BaseRequest:
    def __init__(self, filters: dict = dict(), errors: list = list()) -> None:
        self.filters = filters
        self.errors = errors

    def add_error(self, parameter: str, message: str) -> None:
        self.errors.append({"parameter": parameter, "message": message})

    def has_error(self) -> bool:
        return len(self.errors) > 0

    def __bool__(self):
        return True
