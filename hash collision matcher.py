import hashlib

string=input("Enter the hash value to match in lowercase- ")
candidate = 0
while True:
    plaintext = str(candidate)
    hash = hashlib.md5(plaintext.encode('ascii')).hexdigest() # you can change the hash type by replacing md5 with other types.
    #print(hash)
    if hash[:len(str(string))] == string:
        print('plaintext:' + plaintext + '\nmd5:' + hash)
        break
    candidate = candidate + 1

'''
Supported hashes are

SHA1
SHA224
SHA384
SHA512
MD5

Other types like adler32, crc32 are present in zlib module
'''
