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
