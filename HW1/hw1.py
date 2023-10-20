class hw1():
    def __init__(self): #定義初始數值
        self.bincontainer = [1,0,0]
        self.decimalcontainer = [2,1]

    def output(self):#使用 for 迴圈分別輸出在container的值
        print("------------------")
        print("十進位容器內容為")
        for i in self.decimalcontainer:
            print(i)
        print("------------------")
        print("二進位容器內容為")
        for i in self.bincontainer:
            print(i)
        print("------------------")
    
    def decimal2bin(self): #定義計算過程 十進位轉二進位
        value = 0
        bin = []
        #將list內容轉換為十進位數字
        for num,i in enumerate(self.decimalcontainer[::-1]):
            value += i*10**num
        #計算十進位轉二進位
        while value >=1: #當value<1才會中斷迴圈
            bin.append(value%2)
            value = value//2
        print(bin[::-1])
        return bin[::-1] #回傳二進位後結果

    def bin2decimal(self): #二進位轉十進位
        value = 0
        dec = []
        #計算二進位轉換成十進位
        for num,i in enumerate(self.bincontainer[::-1]):
            value  = value + i*2**num
        #print(value) 
        dec = list(str(value)) #將十進位轉換成list格式
        dec = [int(v) for v in dec]#將list中的單位轉換成int型別以利之後使用
        print(dec)
        return dec



hw = hw1()
hw.output()
hw.decimal2bin()
hw.bin2decimal()
