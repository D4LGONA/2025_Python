

class Machine:
    def __init__(self):
        self.money = 0
        self.items = {"아이시스": Item(800, 40), "아쿠아제로": Item(2000),  "레몬워터": Item(1800, 40),
                      "옥수수수염차": Item(1600, 40), "황금보리" : Item(1600), "트레비":Item(1300, 40),
                      "펩시제로":Item(1100),"펩시":Item(1100), "칠성사이다제로":Item(1300), "칠성사이다":Item(1300), "델몬트망고": Item(1200, 40),
                      "립톤아이스티":Item(1200), "사과에이드":Item(1100, 40), "포도에이드":Item(1100), "레쓰비":Item(900),
                      "가나초코":Item(900), "핫식스제로":Item(1300), "밀키스":Item(1100), "핫식스":Item(1300), "레쓰비카페타임":Item(1200),
                      "게토레이":Item(1000, 40), "코코포도":Item(1000), "잔치집식혜":Item(1000) }

    def insert_money(self, amount):
        if amount > 0:
            self.money += amount
            return True
        return False

    def add_item(self, name, obj):
        self.items[name] = obj

    def get_items(self):
        return self.items

    def purchase(self, name):
        item = self.items[name]
        item.purchase(self.money)
        self.money -= item.price

    def purchase_card(self, name):
        item = self.items[name]
        item.purchase(self.money)
        print(f"{name} 구매 성공")

    def is_available(self, name):
        return self.items[name].is_available(self.money)

    def refund(self):
        refund_amount = self.money
        self.money = 0
        return refund_amount


class Item:
    def __init__(self, price, stock = 20):
        self.price = price
        self.stock = stock
        self.maxStock = stock

    def is_available(self, money): # 구매 가능한지 확인하는 함수
        return self.stock > 0 and (money >= self.price or money == -1)

    def purchase(self, money):
        if self.is_available(money):
            self.stock -= 1 # 재고 -1
            return True
        return False