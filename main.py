from blockchain import Blockchain

blockchain = Blockchain()

def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['nounce']
    proof = blockchain.mine_block(previous_proof)
    previous_hash = blockchain.generate_block_hash(previous_block)
    block = blockchain.generate_block(proof, previous_hash)

    return block

def show_blockchain():
    print(blockchain.blockchain)

mine_block()
mine_block()
mine_block()

show_blockchain()