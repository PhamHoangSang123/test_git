def generateKey(string, key): 
  key = list(key) 
  if len(string) == len(key): 
    return(key) 
  else: 
    for i in range(len(string) -len(key)): 
      key.append(key[i % len(key)]) 
  return("" . join(key)) 

def removeSpaces(text):
	newText = ""
	for i in text:
		if i == " ":
			continue
		else:
			newText = newText + i
	return newText
  
def encryption(string, key): 
  encrypt_text = [] 
  for i in range(len(string)): 
    x = (ord(string[i]) +ord(key[i])) % 26
    x += ord('A') 
    encrypt_text.append(chr(x)) 
  return("" . join(encrypt_text)) 

if __name__ == "__main__": 
 string = input("Nhap Plain Text: ")
 keyword = input("Nhap vao KEYWORD: ")
 string2 = removeSpaces(string)
 key = generateKey(string, keyword) 
 encrypt_text = encryption(string2,key) 
 print("Cipher: ", encrypt_text)