from string import digits, ascii_lowercase, ascii_uppercase
from itertools import product

result = 'c9b5af9864efa933'

def compute_hash(uinput):
	if len(uinput) > 32: return
	blen = 32
	n = blen - len(uinput) % blen
	if n == 0:
		n = blen
	pad = chr(n)
	ninput = uinput + pad * n
	r = ""
	for i in range(0, blen, 4):
		s = ninput[i:i+4]
		h = 0
		for j in range(len(s)):
			h = (h << 4) + ord(s[j])
			g = h & 4026531840
			if not(g == 0):
				h ^= g >> 24
			h &= ~g
		r += chr(h % 256)
	h = ""
	for c in r:
		h += c.encode("hex")
	return h

chars = digits+ascii_lowercase+ascii_uppercase+'_'+'{}'

for n in range(1, 32):
    for comb in product(chars, repeat=n):
        a = ''.join(comb)
        if compute_hash(a) == result:
            print a

