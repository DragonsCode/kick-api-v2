class JSONFailedError(Exception):
    def __init__(self, message: str = "Failed to parse JSON. This could be the cloudflare captcha. Please try again later.") -> None:
        super().__init__(message)

class NoLivestreamError(Exception):
    def __init__(self, message: str = "No livestream found.") -> None:
        super().__init__(message)