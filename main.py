from blockchain import Blockchain
from transaction import Transaction


blockchain = Blockchain(consensus="pow", difficulty=3)

if blockchain.consensus == "pos":
    blockchain.validators.add_staker("Alice", 50)
    blockchain.validators.add_staker("Bob", 30)

blockchain.add_transaction(Transaction("Owen", "Efe", 5))
blockchain.add_transaction(Transaction("Jack", "Seamus", 2))

print("Mining...")
block_index = blockchain.mine(miner_address="Alice")
print(f"Block {block_index} mined successfully.")

for block in blockchain.chain:
    print(f"Block {block.index}: {block.transactions} -> {block.hash}")
