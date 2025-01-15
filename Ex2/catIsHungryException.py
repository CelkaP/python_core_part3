class CatIsHungryException (Exception):
    def __init__(self, message:str="Cat is hungry!"):
        self.message = message
        super().__init__(message)
        
    def __str__(self):
        return self.message