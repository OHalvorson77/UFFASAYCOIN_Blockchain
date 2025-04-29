class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender=sender
        self.recipient=recipient
        self.amount=amount
        
    def to_dict(self):
        return self.__dict__