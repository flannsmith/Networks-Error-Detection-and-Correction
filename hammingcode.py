import argparse


print("Enter in binary the message you wish to transmit, see -h for program requirements")
parser = argparse.ArgumentParser(description="Hamming code error detection and correction of binary string")
parser.add_argument('hamcode', type=str, help="Binary code you want to transmit e.g. '101010101101'")
args = parser.parse_args()

codeword = args.hamcode

#codeword = '0101'
#codeword = '0000000011000001'

n = len(codeword)
k = 0
while 2**k < (n + k + 1):
    k+=1

#print(k)

L = k + n
encodedcode=[0]*L
#print(encodedcode)
for i in range(1, L+1):
    #print('Index: ',i)
    for p in range(0,k+1):
        #print('P: ',p)
        count = 0
        if ((2**p == i)):
            #print('At index: ',i,'Inserting parity')
            encodedcode[i-1]='0'
            #print('At index: ', i, 'Encoded: ',encodedcode[i])
            count+=1
            break
        elif ((len(codeword) != 0) and (2**p > i) and (i<=len(encodedcode))):
            #print('At index: ', i, 'Inserting code')
            encodedcode[i-1] = codeword[0]
            codeword = codeword[1:]
            break
            
print("Encoded code is: \n", encodedcode)

#To decode
#Check if parity bits are odd or even
#Count how many parity bits

def p1Elements(a):
    p1 = a[::2]
    for i in range(len(p1)):
        p1[i] = int(p1[i])
    return sum(p1)

def p2Elements(a):
    p2 = a[1::2]
    for i in range(len(p2)):
        p2[i] = int(p2[i])
    return sum(p2)
   
def p4Elements(a):
    p4 = a[3:6:4]
    for i in range(len(p4)):
        p4[i] = int(p4[i])
    return sum(p4)

def p8Elements(a):
    p8 = a[7:15:8]
    for i in range(len(p8)):
        p8[i] = int(p8[i])
    return sum(p8) 

def p16Elements(a):
    p16 = a[15:30:16]
    for i in range(len(p16)):
        p16[i] = int(p16[i])
    return sum(p16)

def p20Elements(a):
    p20 = a[19:40:20]
    for i in range(len(p20)):
        p20[i] = int(p20[i])
    return sum(p20)


#if sum of parity bits are equal to zero, insert 0 at its designated checkbit, else insert 1/flip bit
#print(p1Elements(encodedcode))

if (p1Elements(encodedcode)) % 2 == 0:
    encodedcode[0] = 0
else:
    encodedcode[0] = 1

p1checked = encodedcode
#print(p1checked)


while len(encodedcode) >= 2:
    if (p2Elements(p1checked)) % 2 == 0:
        p1checked[1] = 0
    else:
        p1checked[1] = 1
    break
p2checked = p1checked


while len(encodedcode) >= 4:
    if (p4Elements(p2checked)) % 2 == 0:
        p2checked[3] = 0
    else:
        p2checked[3] = 1
    break
p4checked = p2checked


while len(encodedcode) >= 8:
    if (p8Elements(p4checked)) % 2 == 0:
        p4checked[7] = 0
    else:
        p4checked[7] = 1
    break
p8checked = p4checked


while len(encodedcode) >= 16:
    if (p16Elements(p8checked)) % 2 == 0:
        p8checked[15] = 0
    else:
        p8checked[15] = 1
    break
p16checked = p8checked


while len(encodedcode) >= 20:
    if (p20Elements(p16checked)) % 2 == 0:
        p16checked[19] = 0
    else:
        p16checked[19] = 1
    break
p20checked = p16checked

print("After error detection + correction: \n",p20checked)




