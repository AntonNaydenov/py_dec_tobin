def toDec(num):
    i = num
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
    
    print(ipList)
    res=''
    i=0
    while i < len(ip.split('.')):
        
        if i ==3:
            res = res + str(toDec(int(ip.split('.')[i])))
        else:
            res = res + str(toDec(int(ip.split('.')[i]))) + '.'
        i+=1
    
    return res


print(decIP('172.18.188.35'))
