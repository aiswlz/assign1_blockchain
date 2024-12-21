class Block:
    def __init__(self, previous_hash, timestamp, transactions):
        """Initialize the block with basic attributes."""
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.nonce = 0
        self.hash = None
