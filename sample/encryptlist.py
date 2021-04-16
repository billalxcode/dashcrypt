from dashcrypt.encrypt import Encrypt

text_list = ["Example1", "Example2"]

for text in text_list:
    text_encoded = text.encode()

    e = Encrypt(text_encoded)
    e.setMode(True)
    result = e.crypt(mode=None)
    print (result)