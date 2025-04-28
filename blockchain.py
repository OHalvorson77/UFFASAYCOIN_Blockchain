from block import Block
from validator import ValidatorSelection
import time

class Blockchain:
    def __init__(self, consensus="pow", difficulty=2):
        self.unconfirmed_transactions = []
        self.chain = []
        self.difficulty = difficulty
        self.consensus = consensus
        self.validators = ValidatorSelection()
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, [], time.time(), "0")
        self.chain.append(genesis_block)

    def add_transaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)

    def proof_of_work(self, block):
        block.nonce = 0
        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * self.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()
        return computed_hash

    def add_block(self, block, proof):
        previous_hash = self.last_block.hash

        if previous_hash != block.previous_hash:
            return False

        if not proof.startswith('0' * self.difficulty) and self.consensus == "pow":
            return False

        block.hash = proof
        self.chain.append(block)
        return True

    def mine(self, miner_address):
        if not self.unconfirmed_transactions:
            return False

        last_block = self.last_block

        if self.consensus == "pow":
            new_block = Block(index=last_block.index + 1,
                              transactions=[tx.to_dict() for tx in self.unconfirmed_transactions],
                              timestamp=time.time(),
                              previous_hash=last_block.hash)

            proof = self.proof_of_work(new_block)
            self.add_block(new_block, proof)
            self.unconfirmed_transactions = []
            return new_block.index

        elif self.consensus == "pos":
            validator = self.validators.select_validator()
            new_block = Block(index=last_block.index + 1,
                              transactions=[tx.to_dict() for tx in self.unconfirmed_transactions],
                              timestamp=time.time(),
                              previous_hash=last_block.hash,
                              validator=validator)

            new_block.hash = new_block.compute_hash()
            self.add_block(new_block, new_block.hash)
            self.unconfirmed_transactions = []
            return new_block.index

    @property
    def last_block(self):
        return self.chain[-1]
