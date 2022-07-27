import tkinter as tk
import random as rd
from PIL import Image,ImageTk

numbers=[]
def roll_lotto():
    cvs.delete(lotto_img)
    lotto_num=sorted(list(rd.sample(range(1,46),k=6)))
    button['text']=lotto_num
    button.place(x=305,y=500) #클릭 후 위치도 바꾸니 훨씬 깔끔쓰~~
    button.update()
    title_label.place(x=290, y=20)
    numbers.append(lotto_num)
    lotto_pap = tk.PhotoImage(file="lotto.png")
    lotto_paper = cvs.create_image(150, 180, image=lotto_pap)





def want2_exit():
    r.destroy()

r=tk.Tk()
r.title('로또 번호 추첨기')
r.geometry('900x600')
cvs=tk.Canvas(r,width=900,height=600,bg='white')
cvs.pack()
lotto_icon=tk.PhotoImage(file='lottery_img.png')
lotto_img=cvs.create_image(450,180,image=lotto_icon)
title_label=tk.Label(r,text='이번주 당첨번호는?',font=('둥근모꼴',28),background='white',borderwidth=10)
title_label.place(x=290,y=300)
button=tk.Button(r,text='눌러보세요!',font=('둥근모꼴',24),command=roll_lotto,bg='white',fg='GREEN')
button.place(x=360,y=500)
btn_exit=tk.Button(r,text='나가기',font=('둥근모꼴',22),command=want2_exit,bg='Green',fg='White')
btn_exit.place(x=700,y=500)

cvs.create_line(450,600,450,0)
cvs.create_line(0,300,900,300)
r.mainloop()
