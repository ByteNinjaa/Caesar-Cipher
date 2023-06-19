def caesar_cipher_decrypt(ciphertext):
    for shift in range(26):
        plaintext = ''
        for char in ciphertext:
            if char.isalpha():
                if char.islower():
                    decrypted_char = chr((ord(char) - shift - 97) % 26 + 97)
                else:
                    decrypted_char = chr((ord(char) - shift - 65) % 26 + 65)
                plaintext += decrypted_char
            else:
                plaintext += char
        print(f'Shift {shift}: {plaintext}')

# Example usage:
ciphertext = "Pthnpul P ht kljpkpun pm P sprl zvtl uld, olylavmvyl buahzalk mvvk"
caesar_cipher_decrypt(ciphertext)
