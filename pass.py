from cryptography.fernet import Fernet




'''
def write_key():
    key=Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)

write_key()
'''

def load_key():
    file=open("key.key", "rb")
    key=file.read()
    return key


master_pwd= input("What is the master password?")

key=load_key()+ master_pwd.encode()
fer=Fernet(key)







def add():
    name=input("Account Name:")
    pwd=input("Password:")
    with open("pass.txt",mode="a") as f:
        f.write(name+"|"+fer.encrypt(pwd.encode()).decode()+"\n")




def view():
    with open("pass.txt",mode="r") as f:
        for line in f.readlines():
            data=line.rstrip()
            name,passw=data.split("|")
            print(f"User:{name}, Password:{fer.decrypt(passw.encode()).decode()}")

while True:
    mode =input("would u like to input new paswords or input new ones or quit(view,add,q)?")
    if mode=="view":
        view()
    elif mode=="add":
        add()
    elif mode=="q":
        break
    else:
        print("invalid mode")
        continue
     


