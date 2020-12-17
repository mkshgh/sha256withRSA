# Import libraries
import rsa
import json
import base64
# private RSA key
pvtKey:str = '''-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAobsOqppUjBQY1uWjN0IHAYgDzsSSqOf7jlleoqrTGuELsfeG
ArfdfumUHkahDmpwPP3K5YJAvoHQprV7tSj3hhGZi/KS0ZVn/LA2F+xb5MrTtKH4
DLrVUkUi5hnH3wUID8n3jtURcnN/M8THeqdnEQaWfdBz9J0AuGw0bUImaE6MFyFq
1ZZ7+JlxyeAXEbAQjFSsYFTBmqkQSuf8TRV+2G2nXd1KqJxAY+o04Wfc9oLPLAHY
n7Zh/K/U6ue5YdzvjP1EVkRzrMkQwsympor4r1vDU3Ygd14vQ4ivxoJD83HhcyLd
1wtPNeQG4NmUGn8QYgqhwE7OiyWc6ZVMdKoBrQIDAQABAoIBAAKpjczA0fUlBuGm
vGtA8tToyciXaM35/6SbaQORf1HOdD7/kvJW14EVfu2JU8ZlJH2EigNW2RJUbbxe
JBqv1snws+U0tDZaA3EKmjaw7978zcOyn4mKG8/eY9GDiXbs4hyXF7RUt+mj6BX7
PnNmRRE9LrCvLpwkvNR3B4foPQdI2QOktjDtbknN5F4nwGuJlWJRkAD+tXrwySOA
cW/88FMJLYHk/Wg4k2JjdZUdterXlI3kuSPHwp6VFjNKNFf4Rj3GfSYgWeFOQk8e
QAIIwgwtTZLBZOwt0/k5gudWT88JN1f4LmvNB5JifDtJImK0ZZL4eL8YDvi9xys0
Tple1WECgYEA2acXJLvD0ciI33cr3/3qclNE09x4nFgSnDIJ9z9wt5pjlxmNSCO9
ySxHnrbW7j75cgVBDQ5QM7iU6nFGh9MRg9y+Y+Yq9WpqLDKvnac+LAh6IzrlbCg6
Egw7zZdcR913zE2LMR7hN8C+rHEMR42DJLS+UlYQdksjf1/thd+E1HECgYEAvjmv
loKjWkhiUV9e7gp6I0niAtu6BU8FpWztxk43gnkLtt6DqxDgTKvTytPYT3DnHo08
0AlBiu1JMzwdOg8aT2Yx7DI0n0jxPG4gfEs/91cvrNEbrSxHUOTYLxBJ5mjdjo61
IAI2LyrwSmUJc6nJqrrF/X5hctW4fyYJllST7v0CgYAq1cmmPxXg2Zimciu+X5ie
e2jWUVOjYWn4N5jigifK2qWy/SJjCjW1u/M0d0OBi/9Hw2T0DtcV9sPICBcbcBzI
WM9XldrqhdDzdd4+JsYDoH95I4Q3bwtOtf2nDpzov9tt5+z2897bPCHKik0iX+Vp
efDi/3Ep9su7q8NxT3Yy4QKBgQCKfXLxcAC/fQ1fUsDJKwWK5YJPNGs07DgfHLPr
eQx+x+OYal2P0ISMLVjPRPYpt/f7zTXl+6clHuX5EB3zJAWyoqNb451eDfvbVA4A
j8RtLaN+/OpaZG8zXLhrYz96KQSMgicpu5J5OpiggPilpYo16y60BCusMB7XKvk1
4jOlfQKBgGGMB8qvqaCvCL/MlbfI5nqj9x1NVP1PE3ywbGzAsdJSroj8vq1Bme+J
A9IRPG+3wwriXOIUGjL0P3AyDcKBNXLga7lyuVswStifx68X/JFheEPB1UYJAWjw
iOWqYRSvv/KrAR6BxF4deRbpyUbkuwdB12+SlQTTwRyU5T2dnNlE
-----END RSA PRIVATE KEY-----'''
 
# Convert the given data into json string file.
dict_reqString = {'TransactionId' : "123", 'AccountNumber' : "1900000001" }
reqString = json.dumps(dict_reqString).encode()
 
# reqString = base64.b64encode(json.dumps(dict_reqString))
 
# load the string as a privatekey
privateRSAkey = rsa.PrivateKey.load_pkcs1(pvtKey)
 
# Sign the data with the private key
signature = rsa.sign(reqString, privateRSAkey, 'SHA-256')
 
print(base64.b64encode(signature))