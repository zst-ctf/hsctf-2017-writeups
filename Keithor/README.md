# Keithor

### Challenge
> [Too many hashes](keithor.py). Help Keith get to the flag! 

### Solution

Look at the source code

	n = ''
    n += md5(FLAG).hexdigest()
    n += sha1(FLAG).hexdigest()
    n += sha224(FLAG).hexdigest()
    n += sha256(FLAG).hexdigest()
    n += sha384(FLAG).hexdigest()
    n += sha512(FLAG).hexdigest()

    if b64encode(n.encode()) == b'<removed for brevity>':

We can see all the hashes are appended together. It is then compared to a base64 encoded string. Decode that string and we get

	4f79807a7c47f697bd5f06beef955cfdf4fdaef8ade8edf707858fe4294d780d69d4d6a897d8598ce3142d207640ca51d8215d0d6c693873fd32c1f6e468750027b5db34b7d9ce0a79753ecc73da664a995889e0d36db4bfc68df9fc8da3d369b266e617a6158d16ccad4189f0a3dcae62d9b103b50b0d4337c96163471b423fc28f3cda29417b7280eb9321492075c5890dc033471cf91781a07001cea6696b32cdf56b2129bc76a83218bee52c830a8bfc09ec55ae372110c0cc8950ef577d32ed211d40307c3fd6684113341e603c

Now, the most vulnerable is MD5, perhaps it is already cracked? MD5 is 128 bits or 32 hex pairs. So retrieve the fist 32 characters

	4f79807a7c47f697bd5f06beef955cfd

We just need to go to [crackhash.com](https://crackhash.com/) and enter the MD5 hash.
	
	Cracked ==>4f79807a7c47f697bd5f06beef955cfd ==> NVL7OA

Now to replace the `FLAG` in `keithor.py`, we need to encode it in base64 before we insert it in
	
	FLAG = b'{insert flag here}'
	FLAG = b64decode(FLAG)

Replace it with `TlZMN09B` (base64 encoded of NVL7OA).

	$ python keithor.py
	Correct flag!

Hence the flag is `TlZMN09B`!