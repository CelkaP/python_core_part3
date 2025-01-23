class SofaIsDamagedException(Exception):
    def __init__(self, message="Sofa is damaged!"):
        self.message = message
        super().__init__(message)

    def __str__(self) -> str:
        return self.message
