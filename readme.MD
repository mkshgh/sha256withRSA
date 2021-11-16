

## SHA(Hashing) vs RSA(Encryption)

- **Hashing**: MD5 and SHA are hash functions (SHA is actually a family of hash functions) - they take a piece of data, compact it and create a suitably unique output that is very hard to emulate with a different piece of data. They don't encrypt anything - you can't take MD5 or SHA output and "unhash" it to get back to your starting point. The difference between the two lies in what algorithm they use to create the hash. Also note that MD5 is now broken as a way was discovered to easily generate collisions and should not be used nor trusted anymore.

- **Encryption**: RSA is an assymetric encryption algorithm. You have two keys (private and public) and you can perform a function with one key (encrypt or decrypt) and reverse with the other key. Which key you use depends on whether you are trying to do a digital signature or an encryption.


## Basic working

- Private key with the client and public key with us
- Convert the given data into json string file.
- Get the byte data of the json file
- Encrypt the data with the RSA private key
- Validate the data with the public key

## SHA signature Generation

- **Creating your own keys and signing the data**

```
import rsa

# If you don't have your own public and private keys, Create a new one

(pubkey, privkey) = rsa.newkeys(512)
```

- **sign and verify your signature and keys**

```

# If you have you own private public keys then you can use
pvtkey = 'some_valid_key_here_|_can_be_string'

# You need to provide a private key of valid format, this checks it
privateRSAkey = rsa.PrivateKey.load_pkcs1(pvtKey)

# rsa signature using SHA-256 Algorithm
signature = rsa.sign(message, privkey, 'SHA-256')

#Verify the signature with public key
rsa.verify(message, signature, pubkey)
```

- **If you only need SHA hashing**

```

import hashlib
import hmac

message='somesecretmessage'
secret = 'somesecretThatIsToo$ecret'
sign = hmac.new(secret, message, hashlib.sha512).hexdigest()

```

## References

- [rsa 4.6](https://stuvel.eu/python-rsa-doc/usage.html)
- [understand the bytes encode/decode](https://www.youtube.com/watch?v=5kRCbHEnyBw)
- [Encode/Decode Base-64](https://docs.python.org/3/library/base64.html)
