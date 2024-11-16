from cryptography.fernet import Fernet
import random
import os

def mainpass(inp:str):
    
    with open("key.key","rb") as fp:
        o=fp.read()
    gen=Fernet(o)
    if os.path.exists("mainpassword.key") and os.path.getsize("mainpassword.key")>1:
        with open("mainpassword.key","rb") as f:
            mai=f.read()
        if gen.decrypt(mai).decode()==inp:
            return True
        else:
            return "wrong password"
    else:
        if len(inp)>0:
            en=gen.encrypt(inp.encode())
            with open("mainpassword.key","wb") as fp:
                fp.write(en)
            return "successfully created"
        else:
            return "Password Could Not Be Empty"
            

def deletion(key):
    
    if os.path.exists("passmanager.txt") and os.path.getsize("passmanager.txt")>100:
                recived_data=decryption()
                if key in recived_data:
                    del recived_data[key]
                    encryption(recived_data)
                return "Deleted Successfully"
                    

def decryption():
    if os.path.exists("key.key") and os.path.exists("passmanager.txt") and os.path.getsize("passmanager.txt")>0:
        pass
    else:
        key=Fernet.generate_key()
        with open("key.key","wb") as f:
            f.write(key)
        

        with open("key.key","rb") as fp:
            k=fp.read()
        data="{}"
        obj=Fernet(k)
        encrypted_data=obj.encrypt(data.encode())
        with open("passmanager.txt","wb") as fp:
            fp.write(encrypted_data)
    with open("key.key","rb") as fp:
        k=fp.read()
    
        with open("passmanager.txt","rb") as fp:
            r=fp.read()

        obj=Fernet(k)
        decrypte_data=obj.decrypt(r)
        recived_data=eval(decrypte_data.decode())
        return recived_data

def encryption(recived_data):
    with open("key.key","rb") as fp:
        k=fp.read()
    obj=Fernet(k)
    secured_data=obj.encrypt(str(recived_data).encode())

    with open("passmanager.txt","wb") as fp:
        fp.write(secured_data)


def storepasss(domainname:any,password:any):
    if os.path.exists("key.key") and os.path.exists("passmanager.txt") and os.path.getsize("passmanager.txt")>0:
        pass
    else:
        key=Fernet.generate_key()
        with open("key.key","wb") as f:
            f.write(key)
        

        with open("key.key","rb") as fp:
            k=fp.read()
        data="{}"
        obj=Fernet(k)
        encrypted_data=obj.encrypt(data.encode())
        with open("passmanager.txt","wb") as fp:
            fp.write(encrypted_data)

    recived_data=decryption()  
    
    temp=""
    for i in recived_data.keys():
        if i==domainname:
            temp=i
    if temp!="":
        t=recived_data[temp]
        t.append(password)
    else:
        recived_data[domainname]=[password]

    encryption(recived_data)
    return "Your Domain Name And Password Successfully Stored"

def generatepass(words,num,symbols,length):
    if words!="" and num!="" and symbols!="" and length!="":
        word2=words.upper()
        generated_passwords=[]
        while len(generated_passwords)<length:
            generated_passwords.append(random.choice(word2))
            generated_passwords.append(random.choice(words))
            generated_passwords.append(random.choice(num))
            generated_passwords.append(random.choice(symbols))

        if len(generated_passwords)>length:
            t=len(generated_passwords)-length
            for _ in range(t):
                generated_passwords.pop()

        random.shuffle(generated_passwords)
        return "".join(generated_passwords)
    else:
        return "Enter A Valid Input"




print(decryption())