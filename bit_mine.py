#security mechanism with cryptography hash using SHA256 (64 bit hexadecimal)
from hashlib import sha256 

MAX_NONCE=100000000000000000000

def SHA256(text):
	return sha256(text.encode('ascii')).hexdigest()

#block number and previous hash is stored in block for bitcoin mining
#add nonce for numbered one to add difficulty to hash
#difficulty must be first four zeros

#process of guessing nonce is bitcoin mininig
def mine(block_number,transaction,previous_hash,prefix_zeros):
	prefix_str='0'*prefix_zeros
	for nonce in range(MAX_NONCE):
		text=str(block_number)+transactions+previous_hash+str(nonce)
		new_hash=SHA256(text)
		if new_hash.startswith(prefix_str):
			print(f"Yay!! Successfully mined bitcoins with nonce value:{nonce}")
			return new_hash
	raise BaseException(f"Could'nt Find Correct HASH after trying max Nonce times")
# every block has refrence to previous chain

if __name__=='__main__':
	transactions='''
	dhruv->charmi->100,
	piyush->kanan->500
	'''
	difficulty=4 #number of zeros before hash
	new_hash=mine(5,transactions,"2d352ad98eefcc20c28b70414cbbb1b6b7c8d0ad119d3e96b8372039e021d97a",difficulty)
	
	print(new_hash)
