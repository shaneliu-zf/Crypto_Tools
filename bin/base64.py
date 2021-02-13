import base64

def crypto(text,mode):
    print("result:")
    text=text.encode("UTF-8")
    if mode == 'en':
        text=base64.b64encode(text)
    elif mode =='de':
        text=base64.b64decode(text)
    print(str(text)[2:-1])
