import argparse


print("Enter in binary the message you wish to transmit, see -h for program requirements")
parser = argparse.ArgumentParser(description="Hamming code error detection and correction of binary string")
parser.add_argument('hamcode', type=str,help="Binary code you want to transmit e.g. '101010101101'")
args = parser.parse_args()

codeword = args.hamcode

#codeword = '0101'
#codeword = '0000000011000001'

n = len(codeword)
k = 0
while 2**k < (n + k + 1):
    k += 1

#print(k)

L = k + n
encodedcode = [0]*L
#print(encodedcode)
for i in range(1, L+1):
    #print('Index: ',i)
    for p in range(0, k+1):
        #print('P: ',p)
        count = 0
        if ((2**p == i)):
            #print('At index: ',i,'Inserting parity')
            encodedcode[i-1] = '0'
            #print('At index: ', i, 'Encoded: ',encodedcode[i])
            count += 1
            break
        elif ((len(codeword) != 0) and (2**p > i) and (i <= len(encodedcode))):
            #print('At index: ', i, 'Inserting code')
            encodedcode[i-1] = codeword[0]
            codeword = codeword[1:]
            break

print("Encoded code is: \n", encodedcode)


#To decode
#Check if parity bits are odd or even
#Sum parity bits, %2 sum == 0, parity bit is zero, otherwise flip it to 1


#Slicing every other bit
def p1Elements(a):
    p1 = a[::2]
    for i in range(len(p1)):
        p1[i] = int(p1[i])
    return sum(p1)


#Slicing every other pair of bits, starting at bit 2
def p2Elements(a):
    p2_bits = []
    for a, b, c, d, e, f in zip(a[1:3], a[5:7], a[9:11], a[13:15], a[17:19], a[21:23]):
        p2_bits.append(a)
        p2_bits.append(b)
        p2_bits.append(c)
        p2_bits.append(d)
        p2_bits.append(e)
        p2_bits.append(f)
    for i in range(len(p2_bits)):
        p2_bits[i] = int(p2_bits[i])
    return sum(p2_bits)


def p4Elements(a):
    p4_bits = []
    for a, b, c in zip(a[3:7], a[11:14], a[19:23]):
        #print(a, b, c)
        p4_bits.append(a)
        p4_bits.append(b)
        p4_bits.append(c)
    for i in range(len(p4_bits)):
        p4_bits[i] = int(p4_bits[i])
    #return(type(p4_bits))
    return sum(p4_bits)


def p8Elements(a):
    p8_bits = []
    for a, b in zip(a[7:15], a[23:29]):
        p8_bits.append(a)
        p8_bits.append(b)
    for i in range(len(p8_bits)):
        p8_bits[i] = int(p8_bits[i])
    return sum(p8_bits)


def p16Elements(a):
    p16 = a[15:34]
    for i in range(len(p16)):
        p16[i] = int(p16[i])
    return sum(p16)


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
#print(p2checked)


while len(encodedcode) >= 4:
    if (p4Elements(p2checked)) % 2 == 0:
        p2checked[3] = 0
    else:
        p2checked[3] = 1
    break
p4checked = p2checked
#print(p4checked)


while len(encodedcode) >= 8:
    if (p8Elements(p4checked)) % 2 == 0:
        p4checked[7] = 0
    else:
        p4checked[7] = 1
    break
p8checked = p4checked
#print(p8checked)


while len(encodedcode) >= 16:
    if (p16Elements(p8checked)) % 2 == 0:
        p8checked[15] = 0
    else:
        p8checked[15] = 1
    break
p16checked = p8checked
#print(p16checked)

print("After error detection + correction: \n", p16checked)
