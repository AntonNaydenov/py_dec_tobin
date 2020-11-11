import sys

try:
    getArgs = sys.argv[1]
except IndexError:
    getArgs = 'null'
if getArgs=='null':
    print('Please use "dectobin help"')
elif sys.argv[1] == 'help':
    print("""
        Script usage:
            To convert decimal number in range of 0 to 255 type "dectobin num <number>"
            To convert decimal ip to binary type "dectobin ip <ip_address>" 
    """)
# else:
#     print('sysargv1 ', sys.argv[1])



def toBin(num):
    i = int(num)
    dec=""
    while i >=1:
        
        dec =dec+ str(i % 2)

       
        i = i // 2
    result = dec[::-1]
    if len(result) == 1 :
        result = '0000000'+ result
    elif len(result) == 2 :
        result = '000000'+ result
    elif len(result) == 3 :
        result = '00000'+ result
    elif len(result) == 4 :
        result = '0000'+ result
    elif len(result) == 5 :
        result = '000'+ result
    elif len(result) == 6 :
        result = '00'+ result
    elif len(result) == 7 :
        result = '0'+ result
    elif len(result) == 8 :
        result = result
    else:
        print('Error....')
    return result
        




def decIP(ip):
    ipList = ip.split('.')
    
    # print(ipList)
    res=''
    i=0
    while i < len(ip.split('.')):
        
        if i ==3:
            res = res + str(toBin(int(ip.split('.')[i])))
        else:
            res = res + str(toBin(int(ip.split('.')[i]))) + '.'
        i+=1
    
    return res

if sys.argv[1] == 'ip':
    print(decIP(sys.argv[2]))
    # print(decIP('7.202.146.23'))
elif sys.argv[1] == 'num':
    print(toBin(sys.argv[2]))
