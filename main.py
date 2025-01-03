from blockchain import EnhancedBlockchain
from rsa import generate_keys
from wallet import create_transaction


blockchain = EnhancedBlockchain()

wallet_private_key, wallet_public_key = generate_keys()
recipient_private_key, recipient_public_key = generate_keys()

transaction = create_transaction(
    wallet_private_key,
    wallet_public_key,
    recipient_public_key,
    "Alice",
    "Bob",
    100
)

# Save the transaction to a database (text file)
blockchain.save_transaction_to_db(transaction)

# Retrieve transactions and add them to the blockchain
transactions = blockchain.retrieve_transactions_from_db()
for tx in transactions:
    blockchain.add_signed_transaction(tx)

for block in blockchain.chain:
    print("Block:")
    print(f"  Hash: {block.hash}")
    print(f"  Previous Hash: {block.previous_hash}")
    print(f"  Transactions: {block.transactions}")

