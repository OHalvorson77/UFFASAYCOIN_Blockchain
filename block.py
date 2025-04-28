import time 
import hashlib

class Block: 
    def __init__(self, index, transactions, timestamp, previous_hash, nonce=0, validator=None):
        self.index=index
        self.transactions=transactions
        self.timestamp=timestamp
        self.previous_hash=previous_hash
        self.nonce=nonce
        self.validator=validator

        self.hash=self.compute_hash()

    def compute_hash(self):
        block_string = f"{self.index}{self.transactions}{self.timestamp}{self.previous_hash}{self.nonce}{self.validator}"
        return hashlib.sha256(block_string.encode()).hexdigest()