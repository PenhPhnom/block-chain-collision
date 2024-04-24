import multiprocessing
from hexer import mHash
from colorama import Fore
from hdwallet import HDWallet
from hexer import mHash
import win32api,win32con
from hdwallet.symbols import LTC as sym
# =========================================================================================
mmdrza = '''
                        
                         求天选之子打赏
            捐赠地址BTC:  33QZ45PtozQFpTWtHg3FCpromkPBYmwnMd  
            捐赠地址USDT/ETH等(ERC20):  0x5bB588177B2E91E5E66e84307841a0b2c18877b1  
'''
# ============================================================================================

r = 1
cores =multiprocessing.cpu_count() - 1


def seek(r) :
    print(mmdrza)   
    fileLTC = "ltcaddr.txt"
    with open(fileLTC) as f :
        add = f.read().split()
        addltc = set(add)
    w = 0
    z = 0
    while True :
        hex64 = mHash()
        privLTC = hex64
        HD: HDWallet = HDWallet(symbol=sym)
        HD.from_private_key(private_key=privLTC)
        ltcadd2 = HD.p2pkh_address()
        ltcadd= HD.p2wpkh_address()
        ltcadd3 = HD.p2wsh_address()
        ltcadd4 = HD.p2sh_address()
       

        print('LtcTotalScan' , str(z) , str(ltcadd),'私钥',str(privLTC),end='\r', flush=True)

        z += 1

        if ltcadd  in addltc or ltcadd2  in addltc or ltcadd3 in addltc or ltcadd4 in addltc :
            w += 1
            f = open("result.txt" , "a")
            f.write('\nLTC PRIVATEKEY ======> ' + str(privLTC))
            f.write('\nAddressLTC =========> ' + str(ltcadd))
            f.write('\nAddressLTC =========> ' + str(ltcadd2))
            f.write('\nAddressLTC =========> ' + str(ltcadd3))
            f.write('\nAddressLTC =========> ' + str(ltcadd4))
            f.close()
            print("恭喜你碰撞BTC成功,记得打赏开发者哟^_^","感谢使用开心碰碰乐！")
seek(r)

if __name__ == '__main__' :
    jobs = []
    for r in range(cores) :
        p = multiprocessing.Process(target = seek , args = (r ,))
        jobs.append(p)
        p.start()
