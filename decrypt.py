#CM2025 Computer Security: Midterm Coursework (Source Code)  
# PART B By Maryam Zaman 

# Q1 b

# defining a function for 'decrypt'. It takes two parameters: 'cipher' & 'key'.
def decrypt(cipher, key): 

    # Initialize an empty string for the plaintext.
    plaintext = "" 

    # Loop through each character in the cipher text.
    for i in range(len(cipher)): 

        # Convert the cipher text character from ASCII to a number between 0-25.
        cipher_char = ord(cipher[i]) - 65  

        # Convert the key character from ASCII to a number between 0-25.
        key_char = ord(key[i]) - 65  

        # Subtract the key number from the cipher text number, then modulo 26 to ensure the result is still within 0-25.
        plaintext_char = (cipher_char - key_char) % 26  

        # Convert the plaintext number back to an ASCII character & add it to the plaintext.
        plaintext += chr(plaintext_char + 65)  

    # Return the plaintext.
    return plaintext 

# The cipher text from the previous program (a).
cipher = "FHZQIE"  

# The key used for encryption.
key = "THISISANEXAMPLEKEYINCOMPUTERSECURITYEXAM" 

# Decrypt the cipher text using the key to get the plaintext.
plaintext = decrypt(cipher, key) 

# Print the plaintext.
print(plaintext) 