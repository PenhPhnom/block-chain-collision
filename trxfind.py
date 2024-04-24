from hdwallet import HDWallet
from hdwallet.symbols import TRX as SYMBOL3
from hexer import mHash
from colorama import Fore, Style
import multiprocessing
from multiprocessing import Pool
import win32api,win32con

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
    filename = "trxaddr.txt"
    with open(filename) as f:
        add = f.read().split()
    add = set(add)
    
    z = 1
    w = 0
    while True:
        hex64 = mHash()
        PRIVATE_KEY: str = hex64        
        HDTRX: HDWallet = HDWallet(symbol = SYMBOL3)
        HDTRX.from_private_key(private_key = PRIVATE_KEY)
        priv = HDTRX.private_key()
        addr = HDTRX.p2pkh_address()
        print('TrxTotalScan' , str(z) , str(addr),'私钥',str(priv),end='\r', flush=True)
        z += 1
        
        if addr in add:            
            w += 1
            z += 1
            f = open("result.txt", "a")
            f.write('\nAddress = ' + str(addr))
            f.write('\nPrivate Key = ' + str(priv))
            f.write('\n=========================================================\n')
            f.close()
            win32api.MessageBox(0,"恭喜你碰撞TRX成功,记得打赏开发者和群里的难兄难弟","开心碰碰乐",win32con.MB_OK)                        
            continue
        


seek(r)

if __name__ == '__main__':
    jobs = []
    for r in range(cores):
        p = multiprocessing.Process(target=seek, args=(r,))
        jobs.append(p)
        p.start()
