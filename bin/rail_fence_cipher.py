def crypto(text,mode):
    rails = input("Please input rails or \"all\":")
    print()
    start = 2
    end = len(text)
    if rails != "all":
        start=int(rails)
        end=start+1
    ans=[]
    for rails in range(start,end):
        if mode == "en":
            result=''.join(fence(text,rails))
        elif mode == "de":
            rng = range(len(text))
            pos = fence(rng,rails)
            result=''.join(text[pos.index(rails)] for rails in rng)
        ans.append("["+str(rails)+"] "+result)
    print("result:")
    for i in ans:
        print(i)

def fence(lst, numrails):
    fence = [[None] * len(lst) for n in range(numrails)]
    rails = list(range(numrails - 1)) + list(range(numrails - 1, 0, -1))
    for n, x in enumerate(lst):
        fence[rails[n % len(rails)]][n] = x
    if 0:
        for rail in fence:
            print(''.join('.' if c is None else str(c) for c in rail))

    return [c for rail in fence for c in rail if c is not None]
