# SENSELESS BY UNUTK4N
from endecode import encode, decode


print("\n SENSELESS BY UNUTK4N \n")
whattodo = input("what do you want to do? en for encoding de for decoding : ") # en for encode de for decode
filename = input("what is the base file name: ")
newfilename = input("what do you want the name of the new file to be ? ")


if whattodo == "en":
    encode(filename, newfilename)
        
elif whattodo == "de":
    decode(filename, newfilename)
        
else:
    print("unexpected value ! ! ! ")