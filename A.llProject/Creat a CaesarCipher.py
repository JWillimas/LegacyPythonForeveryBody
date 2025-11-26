def caesar(text,shift,encrypt=True):

    if not isinstance(shift,int):
        return "shift must be integret" 

    if shift<1 or shift>25:
        return "shift must <1 or >25"
    
    if not encrypt:
        shift=-shift

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    shift_alpahbet=alphabet[shift:]+ alphabet[:shift]

    translation_table=str.maketrans(alphabet+alphabet.upper(),
                                  shift_alpahbet+shift_alpahbet.upper())
    
    encrypted_text=text.translate(translation_table)

    return encrypted_text

def encrypt(text,shift):
    return caesar(text,shift)

def decrypt(text,shift):
    return caesar(text,shift,encrypt=False)


    


text = 'hello world'

print(encrypt(text,13))

text = encrypt(text,13)

print(decrypt(text,13))