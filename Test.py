import hashlib
pass=str(input("Enter random Pass: "))
pass=hashlib.sha3_512(pass)
pass=pass.hexidgest
pass=hashlib.sha3_384(pass)
pass=pass.hexidgest
pass=hashlib.blake2b(pass)
pass=pass.hexidgest
print(pass)
stop=input("Stop? ")
