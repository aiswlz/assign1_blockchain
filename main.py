from blockchain import Blockchain

if __name__ == "__main__":
    blockchain = Blockchain()

    transactions1 = [
        "Alice->Bob->10",
        "Bob->Charlie->20",
        "Charlie->David->30",
        "David->Eve->40",
        "Eve->Frank->50",
        "Frank->Grace->60",
        "Grace->Hannah->70",
        "Hannah->Ivy->80",
        "Ivy->Jack->90",
        "Jack->Kathy->100"
    ]
    blockchain.add_block(transactions1)

    if blockchain.validate_blockchain():
        print("Blockchain is valid.")
    else:
        print("Blockchain is invalid.")

    for block in blockchain.chain:
        print(f"Block Hash: {block.hash}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Merkle Root: {block.merkle_root}")
        print(f"Timestamp: {block.timestamp}")
        print("------")


