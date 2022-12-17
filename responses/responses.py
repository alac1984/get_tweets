class Response:
    def __init__(self, **kwargs) -> None:
        self.errors = kwargs.get("errors", [])
        self.content = kwargs.get("content", [])

    def add_error(self, name: str, message: str) -> None:
        self.errors.append({"name": name, "message": message})

    def has_error(self) -> bool:
        return len(self.errors) > 0

    def __bool__(self):
        return True if not self.has_error() else False

    def __repr__(self):
        if self.has_error:
            return f"Response[ERROR](errors={self.errors})"
        else:
            return f"Response[OK](content={self.content})"
