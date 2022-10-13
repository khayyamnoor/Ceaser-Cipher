alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Since there is very much repetition of code in both functions 
# so we reduce the code by creating a new function called ceaser

# ---------------------------------------------------

# def ceaser(start_text,shift_number,cipher_direction):
#   cipher_text=''
#   for char in start_text:
#     position=alphabet.index(char)
#     if cipher_direction=='decode':
#       shift_number*= -1
#     new_position=position+shift_number
#     new_letter=alphabet[new_position]
#     cipher_text+=new_letter
#   print(f"The {cipher_direction}d text is {cipher_text}")
    
# ceaser(start_text=text,shift_number=shift,cipher_direction=direction)

# ------------------------------------------------------




def encrypt(plain_text,plain_shift):
  cipher_text=''
  for char in plain_text:
    position=alphabet.index(char)
    new_position=position+plain_shift
    new_letter=alphabet[new_position]
    cipher_text+=new_letter
  print(f"The encoded text is {cipher_text}")

def decrypt(plain_text,plain_shift):
  cipher_text=''
  for char in plain_text:
    position=alphabet.index(char)
    new_position=position-plain_shift
    new_letter=alphabet[new_position]
    cipher_text+=new_letter
  print(f"The decoded text is {cipher_text}")

if direction=='encode':
  encrypt(plain_text=text,plain_shift=shift)
elif direction=='decode':
  decrypt(plain_text=text,plain_shift=shift)