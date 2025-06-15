import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Machine import Machine, Item

names = ["아이시스", "아이시스", "아쿠아제로", "레몬워터", "레몬워터", "옥수수수염차", "옥수수수염차", "황금보리", "트레비", "트레비",
              "펩시제로", "펩시", "칠성사이다제로", "칠성사이다", "델몬트망고", "델몬트망고", "립톤아이스티", "사과에이드", "사과에이드", "포도에이드",
              "레쓰비", "가나초코", "핫식스제로", "밀키스", "핫식스", "레쓰비카페타임", "게토레이", "게토레이", "코코포도", "잔치집식혜"]

load_files = ["Images/water.jpg", "Images/water.jpg", "Images/aqua.jpg",  "Images/lemonwater.jpg", "Images/lemonwater.jpg",
                      "Images/oksusu.jpg", "Images/oksusu.jpg", "Images/bori.jpg",  "Images/trevi.jpg", "Images/trevi.jpg",
                      "Images/pz.jpg", "Images/p.png", "Images/chilsz.png", "Images/chils.jpg", "Images/mango.jpg", "Images/mango.jpg",
                      "Images/lipton.jpg", "Images/dapple.jpg", "Images/dapple.jpg", "Images/dgrape.jpg", "Images/letsbe.jpg",
                      "Images/gna.jpg", "Images/hzero.jpg", "Images/milkis.jpg", "Images/hot6.jpg", "Images/gafetime.jpg",
                      "Images/geto.jpg", "Images/geto.jpg", "Images/koko.jpg", "Images/eafw.png"]

class VendingMachineUI:
    def __init__(self, root):
        self.root = root
        self.root.title("자판기")
        self.root.geometry("1024x720")
        self.root.resizable(False, False)

        self.machine = Machine()

        self.notebook = ttk.Notebook(self.root)
        self.sales_page = SalesPage(self.notebook, self.machine)
        self.admin_page = AdminPage(self.notebook, self.machine, self.sales_page)
        self.notebook.add(self.sales_page, text="소비자 모드")
        self.notebook.add(self.admin_page, text="관리자 모드")
        self.notebook.pack(expand=True, fill="both")

class SalesPage(tk.Frame):
    def __init__(self, master, machine):
        super().__init__(master, bg="white")
        self.Machine = machine
        self.root = master
        self.width = 1024
        self.height = 720
        self.images = []
        self.buttons = []

        # GUI 세팅값 #
        self.slot_width = 80
        self.slot_height = 100
        self.gap = 15
        self.num_cols = 10
        self.num_rows = 3
        self.frames = []

        self.init_image()

        self.render_tab()
        self.update_ui()
        print("초기화 완료")

    def init_image(self):
        for i in range(30):
            img = Image.open(load_files[i])
            img = img.resize((70, 70))
            self.images.append(ImageTk.PhotoImage(img))


    def render_tab(self):
        for frame in self.frames:
            frame.destroy()
        self.frames.clear()
        self.buttons.clear()

        # 가운데 정렬
        total_width = self.num_cols * self.slot_width + (self.num_cols - 1) * self.gap
        left_margin = max((self.width - total_width) // 2, 0)

        # 현재 금액 표시
        self.money_var = tk.StringVar()
        self.money_var.set("현재 금액:  " + str(self.Machine.money))
        money_label = tk.Label(self, textvariable=self.money_var, font=("Arial", 14), bg="white")
        money_label.place(x=20, y=380)

        # 금액 투입 버튼들
        values = [1000, 500, 100, 50]
        for i, val in enumerate(values):
            btn = tk.Button(self, text=str(val), width=8, height=2, bg="#3399FF",
                            command=lambda n=val: self.addMoney(n))
            btn.place(x=20 + i * 100, y=600)

        # 카드 버튼
        card_btn = tk.Button(self, text="카드", width=8, height=2, bg="#3399FF", command=self.card)
        card_btn.place(x=20 + len(values) * 100, y=600)

        # 잔돈 반환 버튼
        return_btn = tk.Button(self, text="잔돈 반환", width=8, height=2, bg="#3399FF", command=self.return_money)
        return_btn.place(x=20 + (len(values) + 1) * 100, y=600)

        # 로그
        self.cur_log = tk.StringVar()
        self.cur_log.set("어서오세요!")
        cur_log = tk.Label(self, textvariable=self.cur_log, font=("Arial", 14), bg="white")
        cur_log.place(x=700, y=400)

        for row in range(self.num_rows):
            for col in range(self.num_cols):
                x = left_margin + col * (self.slot_width + self.gap)
                y = 20 + row * 110

                frame = tk.Frame(self, width=self.slot_width, height=self.slot_height,
                                 bg="#ADD8E6", bd=1, relief="solid")
                frame.place(x=x, y=y)

                # 이미지 추가
                img_label = tk.Label(frame, image=self.images[row * 10 + col], bg="#ADD8E6")
                img_label.place(relx=0.5, rely=0.4, anchor="center")

                # 슬롯별 버튼 (추후 품절/비활성화 처리 가능)
                button = tk.Button(frame, bg="green", disabledforeground="black",width=7, height=1, relief="raised",
                                   text= str(self.Machine.items[names[row * 10 + col]].price),
                                   command=lambda n=row * 10 + col: self.buy(n))
                button.place(relx=0.5, rely=0.8, anchor="center")

                self.frames.append(frame)
                self.buttons.append(button)

    def card(self):
        if self.Machine.money != 0: return
        self.Machine.money = -1
        self.update_ui()

    def update_ui(self):
        if self.Machine.money == -1:
            for i in range(len(names)):
                self.buttons[i].config(state="normal", bg="green",
                                       text=str(self.Machine.items[names[i]].price))
            self.money_var.set("현재 금액:  " + "카드 결제 가능!")
        else:
            for i in range(len(names)):
                self.buttons[i].config(
                    text=str(self.Machine.items[names[i]].price))
                if self.Machine.is_available(names[i]):
                    self.buttons[i].config(state="normal", bg="green")
                else:
                    self.buttons[i].config(state="disabled", bg="red")
            self.money_var.set("현재 금액:  " + str(self.Machine.money))

    def return_money(self):
        change = self.Machine.money
        self.Machine.money = 0
        self.update_ui()

        if change <= 0:
            self.cur_log.set("반환할 돈이 없습니다!")
            return

        result = ""
        denominations = [1000, 500, 100, 50]
        for coin in denominations:
            count = change // coin
            change %= coin
            if count > 0:
                result += f"{coin}원: {count}개\n"
        result += "잔돈이 반환되었습니다!"
        self.cur_log.set(result)
        self.update_ui()

    def addMoney(self, num):
        self.Machine.insert_money(num)
        self.update_ui()

    def buy(self, idx):
        if self.Machine.money == -1:
            self.Machine.purchase(names[idx])
            self.Machine.money = 0
        else:
            self.Machine.purchase(names[idx])
        self.cur_log.set(names[idx] + "을(를) 구매했습니다!")
        self.update_ui()

class AdminPage(tk.Frame):
    def __init__(self, master, machine, sales_page):
        super().__init__(master, bg="white")
        self.Machine = machine
        self.sales_page = sales_page
        self.root = master
        self.width = 1024
        self.height = 720
        self.images = []
        self.entries = []

        # GUI 세팅값 #
        self.slot_width = 80
        self.slot_height = 100
        self.gap = 15
        self.num_cols = 10
        self.num_rows = 3
        self.frames = []

        self.init_image()

        self.render_tab()
        print("초기화 완료")

    def render_tab(self):
        for frame in self.frames:
            frame.destroy()
        self.frames.clear()

        # 가운데 정렬
        total_width = self.num_cols * self.slot_width + (self.num_cols - 1) * self.gap
        left_margin = max((self.width - total_width) // 2, 0)

        # 로그
        self.cur_log = tk.StringVar()
        self.cur_log.set("어서오세요!")
        cur_log = tk.Label(self, textvariable=self.cur_log, font=("Arial", 14), bg="white")
        cur_log.place(x=self.width/2, y=400,  anchor="center")

        for row in range(self.num_rows):
            for col in range(self.num_cols):
                x = left_margin + col * (self.slot_width + self.gap)
                y = 20 + row * 110

                frame = tk.Frame(self, width=self.slot_width, height=self.slot_height,
                                 bg="#ADD8E6", bd=1, relief="solid")
                frame.place(x=x, y=y)

                item_index = row * 10 + col
                item_name = names[item_index]
                item = self.Machine.items[item_name]

                img_label = tk.Label(frame, image=self.images[item_index], bg="#ADD8E6")
                img_label.place(relx=0.5, rely=0.4, anchor="center")

                entry = tk.Entry(frame, width=6, justify="center")
                entry.insert(0, str(item.price))
                entry.place(relx=0.35, rely=0.55, anchor="center")
                self.entries.append((item_name, entry))

                save_btn = tk.Button(frame, text="저장", width=2,
                                     command=lambda name=item_name, e=entry: self.save_price(name, e))
                save_btn.place(relx=0.8, rely=0.55, anchor="center")

                plus_btn = tk.Button(frame, text="+", width=2, command=lambda name=item_name: self.increase_stock(name))
                plus_btn.place(relx=0.25, rely=0.85, anchor="center")

                minus_btn = tk.Button(frame, text="-", width=2,
                                      command=lambda name=item_name: self.decrease_stock(name))
                minus_btn.place(relx=0.75, rely=0.85, anchor="center")

                self.frames.append(frame)

    def increase_stock(self, name):
        if self.Machine.items[name].stock < self.Machine.items[name].maxStock:
            self.Machine.items[name].stock += 1
            self.cur_log.set(f"{name} 재고 +1 → 현재: {self.Machine.items[name].stock}")
        else:
            self.cur_log.set(f"{name}은 최대 재고입니다!")

    def decrease_stock(self, name):
        if self.Machine.items[name].stock > 0:
            self.Machine.items[name].stock -= 1
            self.cur_log.set(f"{name} 재고 -1 → 현재: {self.Machine.items[name].stock}")
        else:
            self.cur_log.set(f"{name} 재고는 이미 0입니다.")

    def save_price(self, name, entry_widget):
        try:
            new_price = int(entry_widget.get())
            if new_price < 0:
                self.cur_log.set("가격은 0 이상이어야 합니다.")
                return
            self.Machine.items[name].price = new_price
            self.cur_log.set(f"{name} 가격이 {new_price}원으로 변경되었습니다.")
            self.sales_page.update_ui()
            self.update_ui()
        except ValueError:
            self.cur_log.set("유효한 숫자를 입력해주세요.")

    def update_ui(self):
        for name, entry in self.entries:
            entry.delete(0, tk.END)
            entry.insert(0, str(self.Machine.items[name].price))

    def init_image(self):
        for i in range(30):
            img = Image.open(load_files[i])
            img = img.resize((70, 70))
            self.images.append(ImageTk.PhotoImage(img))


if __name__ == "__main__":
    root = tk.Tk()
    app = VendingMachineUI(root)
    root.mainloop()
