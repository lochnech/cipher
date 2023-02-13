#  Caesar Cipher

#  def encrypt(text,s):
#     result = ""
 
#     # traverse text
#     for i in range(len(text)):
#         char = text[i]
 
#         # Encrypt uppercase characters
#         if (char.isupper()):
#             result += chr((ord(char) + s-65) % 26 + 65)
 
#         # Encrypt lowercase characters
#         else:
#             result += chr((ord(char) + s - 97) % 26 + 97)
 
#     return result
 
# #check the above function
# text = "Stuff and things"
# s = 4
# print ("Text  : " + text)
# print ("Shift : " + str(s))
# print ("Cipher: " + encrypt(text,s))



# Affine Cipher

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y
 
def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None
    else:
        return x % m


def affine_encrypt(text, key):
    # C = (a*P + b) % 26
    return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26) + ord('A')) for t in text.upper().replace(' ', '') ])


def affine_decrypt(cipher, key):
    # P = (a^-1 * (C - b)) % 26
    return ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1]))% 26) + ord('A')) for c in cipher ])


text = 'We done and whatnot'
key = [17, 20]

affine_encrypted_text = affine_encrypt(text, key)

print('Encrypted Text: {}'.format(affine_encrypted_text))

# print('Decrypted Text: {}'.format(affine_decrypt(affine_encrypted_text, key)))



#Bacon Cipher

# message = 'I DOn’t LikE cATs oR lIONs'

# def bacon_encrypt(text) :
#     encrypted = ''
#     for char in text:
#         if 65 <= ord(char) < 91 :
#             ord(char)-65


#     return encrypted

# print(bacon_encrypt(message))