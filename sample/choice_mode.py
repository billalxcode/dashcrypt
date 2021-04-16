from dashcrypt.encrypt import Encrypt

text = "Hello Indonesia" # Text
text_encoded = text.encode()
mode_crypt = 0

e = Encrypt(text_encoded)
e.setMode(False) # Turn off auto detect mode
result = e.crypt(mode=mode_crypt) # Encrypt text
print (result) # Show result