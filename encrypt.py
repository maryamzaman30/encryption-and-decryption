#CM2025 Computer Security: Midterm Coursework (Source Code)  
# PART B By Maryam Zaman 

# Q1 a

# defining a function for 'encrypt'. It takes two parameters: 'plaintext' & 'key'.
def encrypt(plaintext, key):
    
    # Initialize an empty string for the cipher text
    cipher = ""

    # Loop through each character in the plaintext
    for i in range(len(plaintext)):  

        # Convert the plaintext character from ASCII to a number between 0-25
        plaintext_char = ord(plaintext[i]) - 65

        # Convert the key character from ASCII to a number between 0-25
        key_char = ord(key[i]) - 65

        # Add the plaintext & key numbers, then modulo 26 to ensure the result is still within 0-25
        cipher_char = (plaintext_char + key_char) % 26

        # Convert the cipher number back to an ASCII character & add it to the cipher text
        cipher += chr(cipher_char + 65)  

    # Return the cipher text
    return cipher  

# The plaintext to be encrypted
plaintext = "MARYAM" 

# The key to be used for encryption
key = "THISISANEXAMPLEKEYINCOMPUTERSECURITYEXAM" 

# Call the encrypt function to encrypt the plaintext
cipher = encrypt(plaintext, key) 

# Print the cipher text
print(cipher) 