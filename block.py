from sha256 import hash

class Block:
    def __init__(self, previous_hash, timestamp, transactions):
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.nonce = 0
        self.hash = None
        
    def calculate_merkle_root(self):
        if not self.transactions:
            return " "

        transaction_hashes = [hash(tx) for tx in self.transactions]
        while len(transaction_hashes) > 1:
            if len(transaction_hashes) % 2 != 0:
                transaction_hashes.append(transaction_hashes[-1])
            transaction_hashes = [
                hash(transaction_hashes[i] + transaction_hashes[i + 1])
                for i in range(0, len(transaction_hashes), 2)
            ]
        return transaction_hashes[0]
        
    def compute_hash(self):
        """Compute the SHA-256 hash of the block."""
        block_string = f"{self.previous_hash}{self.timestamp}{self.transactions}{self.nonce}"
        return hash(block_string)
        
    def mine_block(self, difficulty):
        target = "0" * difficulty
        while not self.hash or not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.compute_hash()
