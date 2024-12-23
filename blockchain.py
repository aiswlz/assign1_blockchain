import time
from block import Block

class Blockchain:
    def __init__(self):
        self.chain = []
        self.difficulty = 4
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block("0", int(time.time()), [])
        self.chain.append(genesis_block)

    def add_block(self, transactions):
        last_block = self.chain[-1]
        new_block = Block(last_block.hash, int(time.time()), transactions)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def validate_blockchain(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.previous_hash != previous_block.hash:
                return False
            if current_block.merkle_root != current_block.calculate_merkle_root():
                return False
            if not current_block.hash.startswith("0" * self.difficulty):
                return False
        return True
