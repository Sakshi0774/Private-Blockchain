import hashlib

def hashGenerator(data):
    result=hashlib.sha256(data.encode())
    return result.hexdigest()

class Block:
    def _init_(self, data, hash, prev_hash):
        self.data = data
        self.hash = hash
        self.prev_hash=prev_hash

class Blockchain:
    def _init_(self):
        hashLast=hashGenerator('gen_last')
        hashStart=hashGenerator('gen_hash')
      
        genesis = Block('blockchain',hashStart, hashLast)
        self.chain = [genesis]

    def add_block(self, data):
        prev_hash = self.chain[-1].hash
        hash = hashGenerator(data + prev_hash)
        block = Block(data, hash, prev_hash)
        self.chain.append(block)

bc = Blockchain()
bc.add_block('project1')
bc.add_block('Sakshi')
bc.add_block('Deeksha')

for block in bc.chain:
    print(block._dict_)