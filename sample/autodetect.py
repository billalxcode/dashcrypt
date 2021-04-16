from dashcrypt.encrypt import Encrypt

text = "Hello World"
text_encoded = text.encode()

e = Encrypt(text_encoded)
e.setMode(True)
result = e.crypt(mode=None)
print (result)