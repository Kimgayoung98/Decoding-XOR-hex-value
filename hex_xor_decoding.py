import binascii

decoding_value = '' # Value to decode (Hex)
key = '' # Key value for decoding  (Hex)
a = bytes.fromhex(decoding_value)
b = bytes.fromhex(key)
print(len(binascii.b2a_hex(a)))

def xor_strings(xs, ys):
	count = 0
	xord_bytes=b''
	for b1, b2 in zip(xs, ys):
		xord_bytes += (bytes([b1 ^ b2]))
	return xord_bytes

temp = ""
for i in range(int(len(a)/len(b))+1):
	a = a[len(b):]
	temp += xor_strings(a, b).hex()
print(temp) # Decoded Hex value 