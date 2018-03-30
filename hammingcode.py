#codeword = input("Enter an input: ")

codeword = '0101'

n = len(codeword)
k = 0
while 2**k < (n + k + 1):
    k+=1

print(k)

L = k + n
encodedcode=[0]*L
print(encodedcode)
for i in range(1, L+1):
    print('Index: ',i)
    for p in range(0,k+1):
        print('P: ',p)
        count = 0
        if ((2**p == i)):
            print('At index: ',i,'Inserting parity')
            encodedcode[i-1]='0'
            print('At index: ', i, 'Encoded: ',encodedcode[i])
            count+=1
            break
        elif ((len(codeword) != 0) and (2**p > i) and (i<=len(encodedcode))):
            print('At index: ', i, 'Inserting code')
            encodedcode[i-1] = codeword[0]
            codeword = codeword[1:]
            break

print(encodedcode)

#Check if parity bits are odd or even
#Count how many parity bits


def p1Elements(a):
    p1 = a[::2]
    for i in range(len(p1)):
        p1[i] = int(p1[i])
    return(sum(p1))

def p2Elements(a):
    p2 = a[1::2]
    for i in range(len(p2)):
        p2[i] = int(p2[i])
    return(sum(p2))

def p4Elements(a):
    p4 = a[3:6:4]
    for i in range(len(p4)):
        p4[i] = int(p4[i])
    return(sum(p4))

def p8Elements(a):
    p8 = a[7:15:8]
    for i in range(len(p8)):
        p8[i] = int(p8[i])
    return (sum(p8))

def p16Elements(a):
    p16 = a[15:30:16]
    for i in range(len(p16)):
        p16[i] = int(p16[i])
    return (sum(p16))

    
        #print(sum(elements))
        # if elements % 2 == 0:
        #     print("Has even parity")
        # else:
        #     elements % 2 == 1
        #     print("Has odd parity")

if (p1Elements(encodedcode)) % 2 == 0:
    print("Has even parity")
else:
    print("Has odd parity")


#slice notation: [start:end:step]


    # if sum(p2 % 2 == 0):
    #     print("Has even parity")
    # else:
    #     if sum(p2 % 2 == 1):
    #         print("Has odd parity")
    #should work but missing last bit?



#print(p2Elements(encodedcode))

#print(p4Elements(encodedcode))


# for elements in p1Elements(a):
#     if elements % 2 == 0:
#         print("Has even parity")
#     else:
#         elements % 2 == 1
#         print("Has odd parity")


