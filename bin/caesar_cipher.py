
def crypto(text,mode):
    shift = input("Please input shift or \"all\":")
    print()
    start = 1
    end = 26
    if shift != "all":
        start=int(shift)
        end=start+1
    ans=[]
    for shift in range(start,end):
        result = ""
        if mode == "de": shift*=-1
        for c in text:
            if (c.isupper()):
                result+=chr((ord(c)+shift-65)%26+65)
            else:
                result+=chr((ord(c)+shift-97)%26+97)
        ans.append("["+str(shift)+"] "+result)
    print("result:")
    for i in ans:
        print(i)
