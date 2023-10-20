#####################  HOMEWORK1  ########################## 
container = [5,1,"a"]

'''
定義輸出 利用for迴圈取出並輸出container的內容
'''
def output(container):
    dec = [0,1,2,3,4,5,6,7,8,9]
    #將container內容輸出，並且利用enumerate計算順序
    for num,i in enumerate(container):
        if i not in dec:#檢查是否符合每一元素皆為0~9
           print("第"+str(num)+"個元素不可為 "+str(i))
           break
        print("第"+str(num)+"個元素為 "+str(i))  #輸出 

'''
將container中的內容由左至右轉換成十進位格式，再計算成二進位值回傳
'''
def decimal2bin(decimalcontainer): #定義計算過程 十進位轉二進位
        dec = [0,1,2,3,4,5,6,7,8,9]
        _value = 0 #儲存list --> 十進位結果
        bin = []   #儲存十進位 --> 二進位list結果
        #將list內容轉換為十進位數字
        for num,i in enumerate(decimalcontainer[::-1]):
            if i not in dec:#檢查是否符合每一元素皆為0~9，若否則終止函式，回傳None
                print("第"+str(len(decimalcontainer)-num-1)+"個元素不可為 "+str(i))
                return None
            _value += i*10**num
        #計算十進位轉二進位
        while _value >=1: #當value<1才會中斷迴圈
            bin.append(_value%2)
            _value = _value//2
        print("二進位結果為"+str(bin[::-1])) 
        #此轉換方法會使得list中的第零個為2^0開始
        #但習慣會從最右邊為2^0，因此利用[::-1]將順序反轉
        return bin[::-1] #回傳二進位後結果

output(container)
decimal2bin(container) 
