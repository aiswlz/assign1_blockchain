from hash import hash
import json

class Block:
    def __init__(self, previous_hash, timestamp, transactions):
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.merkle_root = self.calculate_merkle_root()
        self.nonce = 0
        self.hash = self.compute_hash()

    def calculate_merkle_root(self):
        if not self.transactions:
            return ""

        transaction_hashes = [hash(json.dumps(tx, sort_keys=True)) for tx in self.transactions]
        while len(transaction_hashes) > 1:
            if len(transaction_hashes) % 2 != 0:
                transaction_hashes.append(transaction_hashes[-1])
            transaction_hashes = [hash(transaction_hashes[i] + transaction_hashes[i + 1]) for i in range(0, len(transaction_hashes), 2)]
        return transaction_hashes[0]

    def compute_hash(self):
        block_string = f"{self.previous_hash}{self.timestamp}{self.merkle_root}{self.nonce}"
        return hash(block_string)

    def mine_block(self, difficulty):
        target = "0" * difficulty
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.compute_hash()
