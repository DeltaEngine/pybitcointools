from cryptos import *
dash = Dash(testnet=True)
privateKey = "cTUzgAvkrZBKVoKdqmn6vcS919A13cypViLJEospHW8BWrznqpms"
address = dash.privtoaddr(privateKey)
print("Expected address ydtic3kGcRnJw6oaYTF7i8pHX5x8Afso9X: "+address)
#balanceInDuffs = 29260200000
#slow and electrum stuff not working very well: tx = dash.preparesignedtx(privateKey, address, balanceInDuffs-192, fee=192)
