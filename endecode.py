import base64

def encode(filename, newfilename):
    
    try:
        with open(filename, 'rb') as f:
            reading = f.read()
            encoding = base64.b64encode(reading)
        with open(newfilename,"wb") as f:
            f.write(encoding)

    except FileNotFoundError:
        print("FILE NOT FOUND ! ! ! ")


def decode(filename, newfilename):
    try:
        with open(filename, "rb") as f:
            reading = f.read()
            decoding = base64.b64decode(reading)        
        with open(newfilename,"wb") as f:
            f.write(decoding)

    
    except FileNotFoundError:
        print("FILE NOT FOUND !! ! ! ")

    except base64.binascii.Error:
        print("invalid base64 data ! ! ! ! ")
    
