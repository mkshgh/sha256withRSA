# Import libraries
import rsa
import json
import base64



# private and public key, You might already have this.
(pubkey, privkey) = rsa.newkeys(512)
print(pubkey,'\n\n',privkey,'\n\n')

# if you already have a private key  Use the code below and comment above
# then just oad the string as a privatekey
# privateRSAkey = rsa.PrivateKey.load_pkcs1(pvtKey)


# Convert the given data into json string file.
dict_reqString = {'TransactionId' : "123", 'AccountNumber' : "1900000001" }
# reqString = json.dumps(dict_reqString).encode()
reqString = base64.b64encode(json.dumps(dict_reqString).encode())

# fake string just for testing
dict_reqString_fake = {'TransactionId' : "103", 'AccountNumber' : "1900000001" }
reqString_fake = json.dumps(dict_reqString_fake).encode()

# Signing the data with sha-256
signature = rsa.sign(reqString, privkey,'SHA-256')

# If the value is not tainted in between, then it raises an Verification Error
# verified = rsa.verify(reqString_fake, signature, pubkey)

def verify_data(reqString,signature,pubkey):
    try:
        verified = rsa.verify(reqString, signature, pubkey)
        print('verified:',reqString.decode())
    except rsa.pkcs1.VerificationError:
        print('FailedVerifications','This is not a real Data, Call FBI')
    except rsa.pkcs1.DecryptionError:
        print('ChangedBytes','Large Files? Bytes Changed, Dont show this to users might crack the code')
    except Exception as e:
        print('unidentifiedError',e)

# is it verfied then?
verify_data(reqString,signature,pubkey)

# Print your data and be happy
print(verify_data)