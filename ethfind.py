from hdwallet import HDWallet
from hdwallet.symbols import ETH as SYMBOL
from hexer import mHash
from colorama import Fore, Style
import multiprocessing
from multiprocessing import Pool

# =========================================================================================
mmdrza = '''
                        
                         求天选之子打赏
            捐赠地址BTC:  33QZ45PtozQFpTWtHg3FCpromkPBYmwnMd  
            捐赠地址USDT/ETH等(ERC20):  0x5bB588177B2E91E5E66e84307841a0b2c18877b1  
'''
# ============================================================================================

r = 1
cores =multiprocessing.cpu_count() - 1



def seek(r):
    print(mmdrza)
    filename = "ethaddr.txt"
    with open(filename) as f:
        add = f.read().split()
    add = set(add)
    
    z = 1
    w = 0
    while True:
        hex64 = mHash()
        PRIVATE_KEY: str = hex64
        hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
        hdwallet.from_private_key(private_key=PRIVATE_KEY)
        priv = hdwallet.private_key()
        addr = hdwallet.p2pkh_address().lower()
        print('EthTotalScan' , str(z) , str(addr),'私钥',str(priv),end='\r', flush=True)
        z += 1
        
        if addr in add:            
            w += 1
            z += 1
            f = open("result.txt", "a")
            f.write('\nAddress = ' + str(addr))
            f.write('\nPrivate Key = ' + str(priv))
            f.write('\n=========================================================\n')
            f.close()
            print("恭喜你碰撞BTC成功,记得打赏开发者哟^_^","感谢使用开心碰碰乐！")                     
            continue
        


seek(r)

if __name__ == '__main__':
    jobs = []
    for r in range(cores):
        p = multiprocessing.Process(target=seek, args=(r,))
        jobs.append(p)
        p.start()
