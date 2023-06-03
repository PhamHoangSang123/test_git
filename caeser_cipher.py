def encrypt_text(plaintext,k):
    ans = ""
    for i in range(len(plaintext)):
        ch = plaintext[i]
        # check space
        if ch==" ":
            ans+=" "
            
        elif (ch.isupper()):
            ans += chr((ord(ch) + k-65) % 26 + 65)
        
        else:
            ans += chr((ord(ch) + k-97) % 26 + 97)
    
    return ans

plaintext = input("Nhap Plain Text: ")
k = int(input("Nhap vao KEY: "))
print("Cipher: " + encrypt_text(plaintext,k))