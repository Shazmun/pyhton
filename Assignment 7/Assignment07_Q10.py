#Assignment07_Q10
def scramble2Encrypt(inputFile, outputFile):
    with open(inputFile, 'r') as file:
        plainText = file.read()

    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in plainText:
        if charCount % 2 == 0:
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch
        charCount += 1
    encrypted_text = oddChars + evenChars

    with open(outputFile, 'w') as file:
        file.write(encrypted_text)

def scramble2Decrypt(inputFile, outputFile):
    with open(inputFile, 'r') as file:
        encrypted_text = file.read()

    halfLength = len(encrypted_text) // 2
    oddChars = encrypted_text[:halfLength]
    evenChars = encrypted_text[halfLength:]
    decrypted_text = ""
    
    for x, y in zip(evenChars, oddChars):
        decrypted_text += x + y

    with open(outputFile, 'w') as file:
        file.write(decrypted_text)

def main():
    inputFile = input("Enter a source filename: ")
    outputFile = input("Enter a target filename: ")
    operation = input("Enter 'E' to encrypt or 'D' to decrypt the input file: ").upper()

    if operation == "E":
        scramble2Encrypt(inputFile, outputFile)
        print("Done")
    elif operation == "D":
        scramble2Decrypt(inputFile, outputFile)
        print("Done")
    

if __name__ == "__main__":
    main()
