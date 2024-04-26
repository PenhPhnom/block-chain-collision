import multiprocessing
from hexer import mHash
from hexer import randKey
from hexer import switch_case
from hdwallet import HDWallet
from hexer import mHash
from hdwallet.symbols import DOGE as SYMBOL4
# =========================================================================================
mmdrza = '''
                        
                         求天选之子打赏
            捐赠地址BTC:  33QZ45PtozQFpTWtHg3FCpromkPBYmwnMd  
            捐赠地址USDT/ETH等(ERC20):  0x5bB588177B2E91E5E66e84307841a0b2c18877b1  
'''
# ============================================================================================

r = 1
print(mmdrza)   
print("            正在加载数据文件，请耐心等待...")
fileBTC = "dogeaddr.txt"
with open(fileBTC) as f :
    add = f.read().split()
    addoge = set(add)
print("数据文件加载完成！","数据包大小为:",addoge.__sizeof__(),"B")
cores =multiprocessing.cpu_count() - 1


def seek(r) :
    w = 0
    z = 0
    puzzle = input("输入谜题编号设置范围(66~160):")
    min,max = switch_case(puzzle)
    while True :
        # hex64 = mHash()#随机生成一个64位私钥
        hex64 = randKey(min,max)#在一个取值范围内生成一个64位的私钥
        privDG = hex64
        HDDG: HDWallet = HDWallet(symbol = SYMBOL4)
        HDDG.from_private_key(private_key = privDG)
        dgpriv = HDDG.private_key()
        dgaddr = HDDG.p2pkh_address()
       

        print('DogeTotalScan' , str(z) , str(dgaddr),'私钥',str(dgpriv),end='\r', flush=True)

        z += 1

        if dgaddr in addoge :
            w += 1
            f = open("result.txt" , "a")
            f.write('\nDoge PRIVATEKEY ======> ' + str(dgpriv))
            f.write('\nAddressDoge =========> ' + str(dgaddr))                  
            f.close()
            print("恭喜你碰撞BTC成功,记得打赏开发者哟^_^","感谢使用开心碰碰乐！")
seek(r)

if __name__ == '__main__' :
    jobs = []
    for r in range(cores) :
        p = multiprocessing.Process(target = seek , args = (r ,))
        jobs.append(p)
        p.start()
