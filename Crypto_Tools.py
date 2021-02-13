import os

Filelist = []
for home,dirs,files in os.walk("bin"):
    for filename in files:
        if home != "bin/__pycache__":
            Filelist.append(filename[:-3])

print("\nwelcome to use ZF's Crypto Tools")
keep_go = True
while keep_go:
    print("="*50)
    print()
    print("here is the list of Crypto")
    for i in range(0,len(Filelist)):
        print("[",i+1,"] ",Filelist[i],sep='')

    print()
    mode = input("Please select the Crypto:")
    print()
    if mode.isdigit(): mode = Filelist[int(mode)-1]
    exec("from bin import "+mode+" as crypto")
    mode2=input("encrypto or decrypto? :")[:2]
    print()
    x=input("Please input the string:")
    print()
    crypto.crypto(x,mode2)
    print()
    keep_go=input("Use another Crypto? (Y/N) :")
    print()
    keep_go = True if keep_go == 'Y' or keep_go == 'y' else False
