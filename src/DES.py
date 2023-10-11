class DES:

    def dec2bin(dec):
        if dec==0:
            return "0000"
        bin=""
        while dec>0:
            bin+=str(dec%2)
            dec=dec//2
        while len(bin)<4:
            bin+="0"
        return bin[::-1]
    def bin2dec(bin):
        dec=0
        for i in range(len(bin)):
            dec+=int(bin[i])*(2**(len(bin)-i-1))
        return dec
    def hex2bin(hex):
        bin=""
        alpha="0123456789ABCDEF"
        for i in range(len(hex)):
            bin+=DES.dec2bin(alpha.index(hex[i]))
        return bin
    def bin2hex(bin):
        hex=""
        alpha="0123456789ABCDEF"
        for i in range(0,len(bin),4):
            hex+=alpha[DES.bin2dec(bin[i:i+4])]
        return hex
    def isbin(bin):
        for i in range(len(bin)):
            if bin[i]!="0" and bin[i]!="1":
                return False
        return True
   
    def ip(key):

        ip=[58,50,42,34,26,18,10,2,
            60,52,44,36,28,20,12,4,
            62,54,46,38,30,22,14,6,
            64,56,48,40,32,24,16,8,
            57,49,41,33,25,17,9,1,
            59,51,43,35,27,19,11,3,
            61,53,45,37,29,21,13,5,
            63,55,47,39,31,23,15,7]
        key_ip=""
        for i in ip:
            key_ip+=key[i-1]
        return key_ip
    def invip(key):
        invip=[40,8,48,16,56,24,64,32,
                39,7,47,15,55,23,63,31,
                38,6,46,14,54,22,62,30,
                37,5,45,13,53,21,61,29,
                36,4,44,12,52,20,60,28,
                35,3,43,11,51,19,59,27,
                34,2,42,10,50,18,58,26,
                33,1,41,9,49,17,57,25]
        key_invip=""
        for i in invip:
            key_invip+=key[i-1]

        return key_invip
    def efunction(key):
        efunction=[32,1,2,3,4,5,
                4,5,6,7,8,9,
                8,9,10,11,12,13,
                12,13,14,15,16,17,
                16,17,18,19,20,21,
                20,21,22,23,24,25,
                24,25,26,27,28,29,
                28,29,30,31,32,1]
        key_efunction=""
        for i in efunction:
            key_efunction+=key[i-1]
        return key_efunction
    def pfunction(key):
        pfunction=[16,7,20,21,29,12,28,17,
                1,15,23,26,5,18,31,10,
                2,8,24,14,32,27,3,9,
                19,13,30,6,22,11,4,25]
        key_pfunction=""
        for i in pfunction:
            key_pfunction+=key[i-1]
        return key_pfunction

    def pc1(key):
        pc1=[57,49,41,33,25,17,9,
            1,58,50,42,34,26,18,
            10,2,59,51,43,35,27,
            19,11,3,60,52,44,36,
            63,55,47,39,31,23,15,
            7,62,54,46,38,30,22,
            14,6,61,53,45,37,29,
            21,13,5,28,20,12,4]
        key_pc1=""
        for i in pc1:
            key_pc1+=key[i-1]
        return key_pc1
    def pc2(key):
        pc2=[14,17,11,24,1,5,3,28,
            15,6,21,10,23,19,12,4,
            26,8,16,7,27,20,13,2,
            41,52,31,37,47,55,30,40,
            51,45,33,48,44,49,39,56,
            34,53,46,42,50,36,29,32]
        key_pc2=""
        for i in pc2:
            key_pc2+=key[i-1]
        return key_pc2

    def sbox(key):
        s1=[[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
            [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
            [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
            [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]]
        s2=[[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
            [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
            [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
            [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]]
        
        s3=[[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
            [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
            [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
            [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]]
        s4=[[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
            [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
            [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
            [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]]
        s5=[[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
            [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
            [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
            [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]]
        s6=[[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
            [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
            [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
            [4,3,2,12,9,5,15,10,11,14,1,7,10,0,8,13]]
        s7=[[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
            [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
            [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
            [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]]
        s8=[[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
            [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
            [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
            [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]
        sbox=[s1,s2,s3,s4,s5,s6,s7,s8]
        key1=[key[0:6],key[6:12],key[12:18],key[18:24],key[24:30],key[30:36],key[36:42],key[42:48]]
        key2=""
        for i in range(8):
            row=int(key1[i][0]+key1[i][5],2)
            col=int(key1[i][1:5],2)
            key2+=DES.dec2bin(sbox[i][row][col])
        return key2

    def xor(key1,key2):
        key=""
        for i in range(len(key1)):
            key+=str(int(key1[i])^int(key2[i]))
        return key
    def leftshift(key,n):
        shift=[1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
        key=key[shift[n-1]:]+key[:shift[n-1]]
        return key

    def keygen(key):
        key=DES.pc1(key)
        key1=""
        key2=""
        key16=[]
        for i in range(16):
            key1=key[:28]
            key2=key[28:]
            key1, key2 = DES.leftshift(key1, i+1), DES.leftshift(key2, i+1)
            key=key1+key2
            key16.append(DES.pc2(key))

        return key16

    def ffunction(right,key):
        right=DES.efunction(right)
        right=DES.xor(right,key)
        right=DES.sbox(right)
        right=DES.pfunction(right)
        return right

    def encript(plaintext,key):
        count=0
        if DES.isbin(plaintext)==False:
            plaintext=DES.hex2bin(plaintext)
            count=1
        if DES.isbin(key)==False:
            key=DES.hex2bin(key)
        keys=DES.keygen(key)
        plaintext=DES.ip(plaintext)
        left=plaintext[:32]
        right=plaintext[32:]
        for i in range(16):
            temp=right
            right=DES.xor(left,DES.ffunction(right,keys[i]))
            left=temp
        plaintext=right+left
        plaintext=DES.invip(plaintext)
        if count==1:
            plaintext=DES.bin2hex(plaintext)
        return plaintext
   
    def decript(ciphertext,key):
        count=0
        if DES.isbin(ciphertext)==False:
            ciphertext=DES.hex2bin(ciphertext)
            count=1
        if DES.isbin(key)==False:
            key=DES.hex2bin(key)
        keys=DES.keygen(key)
        ciphertext=DES.ip(ciphertext)
        left=ciphertext[:32]
        right=ciphertext[32:]
        for i in range(16):
            temp=right
            right=DES.xor(left,DES.ffunction(right,keys[15-i]))
            left=temp
        ciphertext=right+left
        ciphertext=DES.invip(ciphertext)
        if count==1:
            ciphertext=DES.bin2hex(ciphertext)
        return ciphertext
