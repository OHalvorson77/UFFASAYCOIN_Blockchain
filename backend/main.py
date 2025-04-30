from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import datetime
import hashlib
import uuid

app = Flask(__name__)
CORS(app)

client = MongoClient('mongodb://localhost:27017/')
db = client.blockchain_app
blockchain = db.chain
transactions = db.pending_transactions
users = db.users

from bson import ObjectId

def convert_objectid(obj):
    if isinstance(obj, list):
        return [convert_objectid(item) for item in obj]
    elif isinstance(obj, dict):
        return {k: convert_objectid(v) for k, v in obj.items()}
    elif isinstance(obj, ObjectId):
        return str(obj)
    else:
        return obj


# Utility: create wallet with public/private keys
def create_wallet():
    return {
        "address": str(uuid.uuid4()),
        "balance": 100  # Initial airdrop
    }

# Blockchain: create genesis block if empty
if blockchain.count_documents({}) == 0:
    genesis_block = {
        "index": 0,
        "timestamp": str(datetime.datetime.now()),
        "transactions": [],
        "previous_hash": "0",
        "hash": "0"
    }
    blockchain.insert_one(genesis_block)

# Hashing function
def hash_block(block):
    block_str = f"{block['index']}{block['timestamp']}{block['transactions']}{block['previous_hash']}"
    return hashlib.sha256(block_str.encode()).hexdigest()

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data['username']
    if users.find_one({"username": username}):
        return jsonify({"error": "User already exists"}), 400
    wallet = create_wallet()
    users.insert_one({ "username": username, "wallet": wallet })
    return jsonify({ "username": username, "wallet": wallet })

@app.route('/wallet/<username>', methods=['GET'])
def get_wallet(username):
    user = users.find_one({ "username": username })
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user['wallet'])

@app.route('/transaction', methods=['POST'])
def add_transaction():
    data = request.json
    transactions.insert_one(data)
    return jsonify({ "message": "Transaction added" })

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']

    user = users.find_one({"username": username})
    if not user:
        return jsonify({"error": "User not found"}), 404

    
    
    return jsonify({
            "username": username,
            "wallet": {
                "address": user['wallet']['address'],
                "balance": user['wallet']['balance']
            }
        })




@app.route('/mine', methods=['POST'])
def mine():
    pending = list(transactions.find({}, {'_id': 0}))  # Exclude _id from transactions

    if not pending:
        return jsonify({ "message": "No transactions to mine" }), 400

    last_block = blockchain.find().sort("index", -1).limit(1)[0]

    new_block = {
        "index": last_block["index"] + 1,
        "timestamp": str(datetime.datetime.now()),
        "transactions": pending,
        "previous_hash": last_block["hash"]
    }
    new_block["hash"] = hash_block(new_block)

    # Insert and get inserted block (with ObjectId)
    inserted = blockchain.insert_one(new_block)
    new_block['_id'] = str(inserted.inserted_id)  # Convert to string if you want to include it
    transactions.delete_many({})

    return jsonify({ "message": "Block mined", "block": new_block })

@app.route('/chain', methods=['GET'])
def get_chain():
    chain = list(blockchain.find({}, { "_id": 0 }))
    return jsonify({ "chain": convert_objectid(chain) })

if __name__ == '__main__':
    app.run(debug=True)
