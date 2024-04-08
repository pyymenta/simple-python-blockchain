import datetime
import hashlib
import json

class Blockchain:
    def __init__(self) -> None:
        self.blockchain = []
        self.difficult = 3
        self.generate_block(proof = 1, previous_hash='0')


    def generate_block(self, proof, previous_hash):
        block = {
            'incremental_id': len(self.blockchain) + 1,
            'nounce': proof,
            'previous_hash': previous_hash,
            'timestamp': str(datetime.datetime.now())
        }
        
        self.blockchain.append(block)

        return block
    
    def get_previous_block(self):
        return self.blockchain[-1]

    def mine_block(self, previous_nouce):
        proof = 1
        is_mined = False
        while is_mined is False:
            hash = hashlib.sha256(str(proof**2 - previous_nouce**2).encode()).hexdigest()

            if hash[:self.difficult] == '0' * self.difficult:
                is_mined = True
            else: 
                proof += 1
        return proof

    def generate_block_hash(self, block):
        block_dump = json.dumps(block, sort_keys=True).encode()

        return hashlib.sha256(block_dump).hexdigest()

    def verify_blockchain(self, blockchain):
        previous_block = blockchain[0]
        current_block_id = 1

        while current_block_id < len(blockchain):
            current_block = blockchain[current_block_id]

            if current_block['previous_hash'] != self.hash(previous_block): 
                return False
            
            previous_nounce = previous_block['nounce']
            current_nounce = current_block['nounce']

            current_hash = hashlib.sha256(str(current_nounce**2 - previous_nounce**2).encode()).hexdigest()

            if current_hash[:self.difficult] != '0' * self.difficult: 
                return False
            
            previous_block = current_block
            current_block_id += 1
        return True


