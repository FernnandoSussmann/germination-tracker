class FrameLoadError(Exception):
    def __init__(self, raw_message, errors) -> None:
        message = f"Image could not be capture for an unknown reasons: {raw_message}"
        super().__init__(message)

        self.errors = errors
