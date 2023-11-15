# Private-Blockchain
Creating private Blockchain using Python
Importing hashlib:This line imports the hashlib module, which provides a common interface to various secure hash and message digest algorithms, including SHA-256, which is used in this code.
hashGenerator function:This function takes a 'data' parameter, encodes it using UTF-8, computes its SHA-256 hash, and returns the hexadecimal representation of the hash.
'Block' class:This class represents a block in the blockchain. It has three attributes: 'data' (the information stored in the block), 'hash' (the SHA-256 hash of the block's data), and 'prev_hash' (the hash of the previous block in the blockchain).
'Blockchain' class:This class represents the blockchain itself. It has an '__init__' method that initializes the blockchain with a single genesis block containing some default data. The chain attribute holds the list of blocks in the blockchain.
                    The 'add_block' method is used to add new blocks to the blockchain. It calculates the new block's hash based on the input data and the previous block's hash. Then, it creates a new 'Block' object and appends it to the 'chain'.
 Creating and using the blockchain:     Here, an instance of the 'Blockchain class '(bc) is created, and three blocks with different data are added to the blockchain.                    Finally, it iterates through the blocks in the blockchain and prints the attributes of each block using 'print(block._dict_)'. Note that there's a typo here; it should be 'print(block.__dict__)' to print the attributes of the block.
