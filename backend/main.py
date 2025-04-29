from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from blockchain import Blockchain
import time

app = FastAPI()
blockchain = Blockchain()

class Transaction(BaseModel):
    sender: str
    recipient: str
    amount: float

@app.get("/chain")
def get_chain():
    return {
        "length": len(blockchain.chain),
        "chain": [block.__dict__ for block in blockchain.chain]
    }

@app.post("/transaction")
def add_transaction(transaction: Transaction):
    blockchain.add_transaction(transaction.dict())
    return {"message": "Transaction added successfully."}

@app.post("/mine")
def mine_block():
    result = blockchain.mine("miner_address")
    if result:
        return {"message": f"Block #{result} mined successfully."}
    else:
        raise HTTPException(status_code=400, detail="No transactions to mine.")
