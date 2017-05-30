from Crypto.Cipher import AES

#########################################################################################

# Some of the decimal numbers are negative, and since ASCII is 8-bits,
# we need to calculate the two's complement 
# https://stackoverflow.com/questions/28383585/how-to-get-binary-representation-of-negative-numbers-in-python
def twos_complement(input):
	return ((1<<8) + int(input)) & 0xFF

# Map all the decimals to 8-bit unsigned integers and then to chars
def unsigned_octet_array_to_text(input):
	char_array = map((lambda x: chr(twos_complement(x))), input)
	return "".join( list(char_array) ) 

# https://stackoverflow.com/questions/14179784/python-encrypting-with-pycrypto-aes
def pad_to_16_bytes(data):
	length = 16 - (len(data) % 16)
	data += chr(length)*length
	return data
#########################################################################################

key = "/Vl4PKzS9d+Vm/0eePmaYw==".decode("base64")
#########################################################################################
'''
cipher_text = \
"-93^35^23^82^-4^57^-128^83^-95^-60^-100^73^40^-86^7^73^-101^" + \
"3^118^-66^-104^69^121^76^1^-124^-124^-1^-64^29^28^43^2^-25^" + \
"54^52^-79^-62^11^-43^52^-72^-117^-25^-103^-55^75^-97^"

# Remove last character ^ as there is nothing after it
cipher_text = cipher_text[:-1].split("^")
cipher_text = unsigned_octet_array_to_text(cipher_text).strip()
'''

#cipher_text = "efbfbd231752efbfbd39efbfbd53efbfbdc49c4928efbfbd0749efbfbd0376efbfbdefbfbd45794c01efbfbdefbfbdefbfbdefbfbd1d1c2b02efbfbd3634efbfbdefbfbd0befbfbd34efbfbdefbfbdefbfbdefbfbd4befbfbd".decode("hex")
with open("ciphertext.txt") as myfile:
	cipher_text = myfile.read()

print "cipher", cipher_text.encode("hex"), len(cipher_text)
#########################################################################################

iv = [ 10, -73, -33, -65, 87, 87, -121, -41, -16, 89, 12, 31, 7, 82, -43, -100 ]
iv = unsigned_octet_array_to_text(iv).strip()
# Pad the IV to 16 bytes
iv = pad_to_16_bytes(iv)

#########################################################################################

crypt = AES.new(key, AES.MODE_CBC, iv)
output = crypt.decrypt(cipher_text)
print output