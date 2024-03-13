#Assignment08_Q07

#function that opens a specified text file, reads its contents, uses the dictionary to write an encrypted version of the file’s contents to a second file
def encrypt_text(inp, out):
    codes =  {'A':')','a':'0','B':'(','b':'9','C':'*','c':'8','D':'&','d':'7','E':'^',

              'e':'6','F':'%','f':'5','G':'$','g':'4','H':'#','h':'3','I':'@','i':'2',

              'J':'!','j':'1','K':'Z','k':'z','L':'Y','l':'y','M':'X','m':'x','N':'W',

              'n':'w','O':'V','o':'v','P':'U','p':'u','Q':'T','q':'t','R':'S','r':'s',

              'S':'R','s':'r','T':'Q','t':'q','U':'P','u':'p','V':'O','v':'o','W':'N',

              'w':'n','X':'M','x':'m','Y':'L','y':'l','Z':'K','z':'k','!':'J','1':'j',

              '@':'I','2':'i','#':'H','3':'h','$':'G','4':'g','%':'F','5':'f','^':'E',

              '6':'e','&':'D','7':'d','*':'C','8':'c','(':'B','9':'b',')':'A','0':'a',

              ':':',',',':':','?':'.','.':'?','<':'>','>':'<',"'":'"','"':"'",'+':'-',

              '-':'+','=':';',';':'=','{':'[','[':'{','}':']',']':'}'}
    # Open input and output files
    with open(inp, 'r') as input_file, open(out, 'w') as output_file:
        # Iterate through each linin the input file
        for line in input_file:
            encrypt = ''
            for letter in line:
                # Substitute the harcter using the dictionary, 
                #if not found, keep the orignal character
                encrypt += codes.get(letter, letter)
            # Write the encrypted line to the output file
            output_file.write(encrypt)
            
#opens an encrypted file and displays its decrypted contents on the screen
def decrypt_text(encrypted_fip):
    codes =  {'A':')','a':'0','B':'(','b':'9','C':'*','c':'8','D':'&','d':'7','E':'^',

              'e':'6','F':'%','f':'5','G':'$','g':'4','H':'#','h':'3','I':'@','i':'2',

              'J':'!','j':'1','K':'Z','k':'z','L':'Y','l':'y','M':'X','m':'x','N':'W',

              'n':'w','O':'V','o':'v','P':'U','p':'u','Q':'T','q':'t','R':'S','r':'s',

              'S':'R','s':'r','T':'Q','t':'q','U':'P','u':'p','V':'O','v':'o','W':'N',

              'w':'n','X':'M','x':'m','Y':'L','y':'l','Z':'K','z':'k','!':'J','1':'j',

              '@':'I','2':'i','#':'H','3':'h','$':'G','4':'g','%':'F','5':'f','^':'E',

              '6':'e','&':'D','7':'d','*':'C','8':'c','(':'B','9':'b',')':'A','0':'a',

              ':':',',',':':','?':'.','.':'?','<':'>','>':'<',"'":'"','"':"'",'+':'-',

              '-':'+','=':';',';':'=','{':'[','[':'{','}':']',']':'}'}
    # Open the encrypted input file
    with open(encrypted_fip, 'r') as encrypted_fip:
        # Iterate throu each line in the encrypted file
        for line in encrypted_fip:
            decrypted = ''
            # Iterate through each character in the line
            for letter in line: 
                decrypted += codes.get(letter, letter)
            print(decrypted, end='')

def main():
    # Get user input for input file, output file, and encrypted input file
    inp = input("Enter the name of the input text file: ")
    out = input("Enter the name of the output file to save encrypted text: ")
    encrypted_fip = input("Enter the name of the encrypted input file: ")
# Encrypt the text and save it to the output file
    encrypt_text(inp, out)
 # Decrypt the encrypted text and print it to the console
    decrypt_text(encrypted_fip)

if __name__ == "__main__":
    main()
