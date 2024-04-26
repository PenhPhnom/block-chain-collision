import random
import string

#生成16进制64位随机数
def mHash():
    metax = []
    for i in range(64):
        bx = str(random.choice('0123456789abcdef'))
        metax.append(bx)
    hashstring = ''.join(metax)
    return hashstring

#生成二进制256位随机数
def randKey(min,max):
    # 生成一个在2到2^256之间的随机十进制数
    decimal_number = random.randint(min, max)
    print(decimal_number)
    # 将十进制数转换为十六进制字符串
    hex_string = hex(decimal_number)[2:]  # [2:] 去掉 '0x' 前缀
    print(hex_string)
    # 如果生成的十六进制字符串长度小于64位，前面补零
    hex_string = hex_string[:64].zfill(64)
    print(hex_string)
    # 输出结果
    return hex_string


#设置谜题66~160 前65个谜题已经被破解，所以从66开始
def switch_case(case_number):
    return getMaxMin(2**(int(case_number)-1),2**(int(case_number))-1)
def getMaxMin(a,b):
    return a,b



    


