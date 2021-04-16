# Dash Crypt
Dash Crypt adalah sebuah pustaka untuk enkrpsi sebuah text. Pustaka ini terdapat beberapa macam mode enkripsi.

## Cara kerja
Alat ini menggunakan algoritma yang sangat mudah untuk di pelajari, bahkan kalangan newbie atau pemula dapat memahami algoritma yang saya buat sendiri.
1. Pertama kita ubah dahulu text atau string ke hash, Dash Crypt telah mendukung beberapa hash yaitu 
- MD5
- SHA1
- SHA224
- SHA512
- BLAKE2B

2. Kedua, lalu kita ubah hash tersebut menggunakan algoritma yang sudah dibuat
3. Ketiga, setelah itu kita tambahkan bilangan biner yang telah di acak

## Contoh
```python
from dashcrypt.encrypt import Encrypt

s = "Hello Indonesia".encode()

e = Encrypt(s)
e.setMode(False)
result = e.crypt(mode=0)
print(result)
```

Lihat lain nya di [Sample](https://github.com/billalxcode/dashcrypt/tree/master/sample)

## Fungsi
### Encrypt
- ```setMode``` mempunyai argumen bertipe boolean, berfungsi untuk mengaktifkan automode (mendeteksi mode secara otomatis)
- ```crypt``` mempunyai argumen bertipe integer, berfungsi untuk mengenkripsi text.
- ```generateHash``` tidak mempunyai argumen apapun, berfungsi untuk mengubah text ke hash (md5, sha1, sha224, sha512, blake2b)
