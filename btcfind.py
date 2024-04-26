import multiprocessing
from hexer import mHash
from hexer import randKey
from hexer import switch_case
from hdwallet import HDWallet
from hdwallet.symbols import BTC as SYMBOL2

# =========================================================================================
mmdrza = '''
                        
                         求天选之子打赏
            捐赠地址BTC:  33QZ45PtozQFpTWtHg3FCpromkPBYmwnMd  
            捐赠地址USDT/ETH等(ERC20):  0x5bB588177B2E91E5E66e84307841a0b2c18877b1  

            BTC谜题:网址https://privatekeys.pw/puzzles/bitcoin-puzzle-tx
'''
# ============================================================================================

r = 1

print(mmdrza)   
print("            正在加载数据文件，请耐心等待...")
fileBTC = "btcaddr.txt"
with open(fileBTC) as f :
    add = f.read().split()
    addbtc = set(add)
print("数据文件加载完成！","数据包大小为:",addbtc.__sizeof__(),"B")
cores =multiprocessing.cpu_count() - 1

def seek(r) :
    w = 0
    z = 0
    puzzle = input("输入谜题编号设置范围(1~256):")
    min,max = switch_case(puzzle)
    while True :
        # hex64 = mHash()#随机生成一个64位私钥
        hex64 = randKey(min,max)#在一个取值范围内生成一个64位的私钥
        PRIVATE_KEY: str = hex64
        # =============================================
        HDBTC: HDWallet = HDWallet(symbol = SYMBOL2)
        HDBTC.from_private_key(private_key = PRIVATE_KEY)
        privBTC = HDBTC.private_key()
        btcadd = HDBTC.p2pkh_address()
        btcadd1 = HDBTC.p2un_address()
        btcadd2 = HDBTC.p2sh_address()#
        btcadd3 = HDBTC.p2wpkh_address()
        btcadd4 = HDBTC.p2wsh_address()#
        btcadd5 = HDBTC.p2wsh_in_p2sh_address()#
        btcadd6 = HDBTC.p2wpkh_in_p2sh_address()
        print('私钥',str(z),str(privBTC), str(btcadd),btcadd1,str(btcadd2),str(btcadd3),str(btcadd4),str(btcadd5), str(btcadd6),end='\n', flush=True)
        z += 1
        if btcadd  in addbtc or  btcadd1  in addbtc or btcadd2  in addbtc or btcadd3 in addbtc or btcadd4 in addbtc or btcadd5 in addbtc or btcadd6 in addbtc :
            w += 1
            f = open("result.txt" , "a")
            f.write('\nBTC PRIVATEKEY ======> ' + str(privBTC))
            f.write('\nAddressBTC =========> ' + str(btcadd))
            f.write('\nAddressBTC =========> ' + str(btcadd1))
            f.write('\nAddressBTC =========> ' + str(btcadd2))
            f.write('\nAddressBTC =========> ' + str(btcadd3))
            f.write('\nAddressBTC =========> ' + str(btcadd4))
            f.write('\nAddressBTC =========> ' + str(btcadd5))
            f.write('\nAddressBTC =========> ' + str(btcadd6))
            f.close()
            print("恭喜你碰撞BTC成功,记得打赏开发者哟^_^","感谢使用开心碰碰乐！")
seek(r)

if __name__ == '__main__' :

    jobs = []
    for r in range(cores) :
        p = multiprocessing.Process(target = seek , args = (r,))
        jobs.append(p)
        p.start()
