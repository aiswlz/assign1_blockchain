from sha256 import hash

class Block:
    def __init__(self, previous_hash, timestamp, transactions):
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.nonce = 0
        self.hash = None
        
    def compute_hash(self):
        """Compute the SHA-256 hash of the block."""
        block_string = f"{self.previous_hash}{self.timestamp}{self.transactions}{self.nonce}"
        return hash(block_string)
        
    def mine_block(self, difficulty):
        target = "0" * difficulty
        while not self.hash or not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.compute_hash()
