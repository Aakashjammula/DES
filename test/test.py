import sys
sys.path.insert(1,"//home//aakash//git//DES//src")
from DES import DES

def main():
    #read plaintext.txt
    #f=open("//home//aakash//git//DES//test//plaintext.txt","r")
    #plaintext=f.read()
    #f.close()
    #read key.txt
    #f1=open("//home//aakash//git//DES//test//key.txt","r")
    #key=f1.read()
    #f1.close()
    plaintext="5AFE"*4
    key="C0DE"*4
    #plaintext="1111000011110000111100001111000011110000111100001111000011110000"
    #key="0001001100110100010101110110101110011011101111111111111111110001"
    ciphertext=DES.encript(plaintext,key)
    print("ciphertext:",ciphertext)
    print("plaintext:",DES.decript(ciphertext,key))

if __name__ == "__main__":
    main()