from tkinter import *
import time
import threading

class Company:
    # main variables
    def __init__(self, money, workers, stock, worktime, capacity, w_capacity):
        self.money=money
        self.workers=workers
        self.stock=stock
        self.worktime=worktime
        self.capacity=capacity
        self.w_capacity=w_capacity
        
    def check_w_capacity(self):
        if self.workers>self.w_capacity:
            #minus=self.w_capacity-self.workers
            #self.workers-=minus
            self.workers=self.w_capacity # always reset to capacity
    
    def buy_t1(self):
        if self.workers<self.w_capacity:
            self.workers+=10
            self.money-=100
        # +10 workers -100$
    
    def buy_t2(self):
        if self.workers<self.w_capacity:
            self.workers+=20
            self.money-=200
        # +20 workers -200$
        
    def buy_t3(self):
        if self.workers<self.w_capacity:
            self.workers+=50
            self.money-=500  
        # +50 workers -500$
    
    def sell_t1(self):
        if self.stock>10:
            self.stock-=10
            self.money+=100
        # -10 products +100$
        
    def sell_t2(self):
        if self.stock>20:
            self.stock-=20
            self.money+=200
        # -20 products +200$
        
    def sell_t3(self):
        if self.stock>50:
            self.stock-=50
            self.money+=500
        # -20 products +500$
        
    def buy_new_property(self):
        if self.money>=10000:
            self.capacity+=500
            self.w_capacity+=50
            self.money-=10000
        
    def working(self):
        self.worktime=True
        while self.worktime is True:
            cp.check_w_capacity()
            if self.workers>0 and self.stock<=self.capacity:
                plus=self.workers*1
                if self.stock+plus < self.capacity:
                    self.stock+=plus

                else:
                    self.stock=self.capacity
            #else:
                #self.worktime=False
            
            time.sleep(1.5)
        
    def print_inventory(self):
        while True:
            label=Label(root, borderwidth=8, text="current status: \n{}$ \n{}\\{} workers \n{}\\{} products".format(self.money, self.workers, self.w_capacity, self.stock, self.capacity),fg='white',bg='black', bd=3, relief=SUNKEN)
            label.grid(row=3, column=1, pady=10)
            time.sleep(0.5)
        
cp=Company(1000, 5, 50, True, 2000, 100)

root=Tk()
root.title("Company game")
#root.geometry('500x500+650+220')

label=Label(root, text="Welcome",fg='orange', bg='black', bd=3, relief=SUNKEN)
label.grid(row=0,column=0, columnspan=3, sticky=W+E)

buy_l=Label(root, borderwidth=8, text="Buy\nTIER 1: +10 workers and -100$\nTIER 2: +20 workers and -200$\nTIER 3: +50 workers and -500$", fg='orange', bg='black', bd=3, relief=SUNKEN)
buy_l.grid(row=1,column=0, pady=5)
buy_b0=Button(root, borderwidth=8, fg='orange', bg='black', text="TIER 1", command=cp.buy_t1, width=8) # buy button tier 1
buy_b0.grid(row=2,column=0)
buy_b1=Button(root, borderwidth=8, fg='orange', bg='black', text="TIER 2", command=cp.buy_t2, width=8) # buy button tier 2
buy_b1.grid(row=3,column=0)
buy_b2=Button(root, borderwidth=8, fg='orange', bg='black', text="TIER 3", command=cp.buy_t3, width=8) # buy button tier 3
buy_b2.grid(row=4,column=0)

sell_l=Label(root, borderwidth=8, text="Sell\nTIER 1: -10 products and +100$\nTIER 2: -20 products and +200$\nTIER 3: -50 products and +500$", fg='orange', bg='black', bd=3, relief=SUNKEN)
sell_l.grid(row=1,column=2)
sell_b0=Button(root, borderwidth=8, fg='orange', bg='black', text="TIER 1", command=cp.sell_t1, width=8) # sell buton tier 1
sell_b0.grid(row=2,column=2)
sell_b1=Button(root, borderwidth=8, fg='orange', bg='black', text="TIER 2", command=cp.sell_t2, width=8) # sell button tier 2
sell_b1.grid(row=3,column=2)
sell_b2=Button(root, borderwidth=8, fg='orange', bg='black', text="TIER 3", command=cp.sell_t3, width=8) # sell button tier 3
sell_b2.grid(row=4,column=2)

exit_b=Button(root, text="EXIT", borderwidth=8, command=root.destroy, fg='orange', bg='black')
exit_b.grid(row=5, column=1, pady=10)

bnp=Button(root, borderwidth=8, fg='orange', bg='black', text="increase space", command=cp.buy_new_property, width=10)
bnp.grid(row=4, column=1)

root.configure(bg='black')

x=threading.Thread(target=cp.working) # working until worktime is True
x.start()

y=threading.Thread(target=cp.print_inventory) # printing inventory in while loop
y.start()

#root.iconbitmap() icon

root.mainloop()