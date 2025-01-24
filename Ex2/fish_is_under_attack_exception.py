class FishIsUnderAttackException(Exception):
    def __init__(self, message="Fish is under attack!"):
        self.message = message
        super().__init__(message)

    def __str__(self) -> str:
        return self.message
