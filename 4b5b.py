import argparse

#for each 4 bits in the bitstream entered
#split into sections of 4 bits
#how to deal with trailing digits e.g. less than 4bits

parser = argparse.ArgumentParser(description="Calculate the 4B5B mapping of 4 binary bits")
parser.add_argument('encodedbits', type=str, help="Binary code you want to transmit e.g. '101010101101'")
args = parser.parse_args()

mydict = {'0000': '11110', '0001':'01001','0010':'10100','0011':'10101','0100':'01010','0101':'01011','0110':'01110','0111':'01111'
,'1000':'10010','1001':'10011','1010':'10110','1011':'10111','1100':'11010','1101':'11011','1110':'11100','1111':'11101'}

#s = '11010101010101001000'
s = args.encodedbits

if len(s) % 4 != 0:
    print("Error, can only process groups of 4 bits")

# length = len(s) % 4
# if length % 4 == 1:
#     letter = s[-1:]
#     s = s[:-1]
# if length % 4 == 2:
#     letter = s[-2:]
#     s = s[:-2]
# if length % 4 == 3:
#     letter = s[-3:]
#     s = s[:-3]
# else:
#     s = s[:]

o = []

while s:
    o.append(s[:4])
    s = s[4:]
   
print (o)

for i, k in mydict.items():
    for j in o:
        if j == i:
            j = k
            #print (i, "is now", k)
            print(j, sep=' ', end='')









