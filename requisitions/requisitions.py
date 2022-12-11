class Requisition:
    def __init__(self, **kwargs) -> None:
        self.errors = kwargs.get("errors", [])
        self.payload = kwargs.get("payload", {})

    def add_error(self, parameter: str, message: str) -> None:
        self.errors.append({"parameter": parameter, "message": message})

    def has_error(self) -> bool:
        return len(self.errors) > 0

    def __bool__(self):
        return True if not self.has_error() else False
