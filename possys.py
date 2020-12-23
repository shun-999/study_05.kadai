import pandas as pd
import datetime
import eel

### 商品クラス
class Item:
    #インスタンス化
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
    
    #金額
    def get_price(self):
        return self.price


### オーダークラス
class Order:
    #インスタンス化
    def __init__(self, item_master):
        self.item_order_list=[]
        self.item_order_name=[]
        self.item_order_price=[]
        self.item_number = []
        self.item_master=item_master

    #オーダー詳細
    def add_item_order(self, item_code, item_number):
        for i in self.item_master:
            if item_code == i.item_code:
                self.item_order_list.append(item_code)
                self.item_order_name.append(i.item_name)
                self.item_order_price.append(i.price)
                self.item_number.append(item_number)
                code = item_code
                name = i.item_name
                price = i.price
                num = item_number
                eel.view_log_js(f"商品コード:{code},商品名:{name},価格:{price},個数:{num}")

    def payment(self, payment):
        self.deposit = payment
    
    def view_item_list(self):
        sum_price = 0
        sum_num = 0
        for price,num  in zip(self.item_order_price, self.item_number):
            sum_price += price*num
            sum_num += num
        cost = sum_price
        eel.sum_cost(f"{cost}")
        change = int(self.deposit) - sum_price
        eel.finish_change(f"{change}")

#マスタ登録
def master_recog(file):
    item_master=[]
    df = pd.read_csv(file)
    for item,name,price in zip(list(df["商品コード"]),list(df["商品名"]),list(df["価格"])):
        item_master.append(Item(str(item),name,price))
    return item_master



#main実行
item_master = master_recog("./master.csv")
order = Order(item_master)

def main1(code_name, sum_num):
    order.add_item_order(code_name, int(sum_num))

def main2(depo):
    pay_out = depo
    order.payment(pay_out)
    order.view_item_list()
