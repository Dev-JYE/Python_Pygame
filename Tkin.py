import tkinter as tk
import tkinter.messagebox

def click_btn():
    tk.messagebox.showinfo('자기소개','반갑습니다. '+entry.get()+' 님!')

def click_btn2():
    text.insert(tk.END,'대가리!')

def want2_exit():
    r.destroy()

r=tk.Tk()
r.title('tkinter 다 섞기')
r.geometry('600x400')
entry=tk.Entry(width=20)
entry.place(x=10,y=10)
btn=tk.Button(text='이름을 입력해주세요',command=click_btn)
btn.place(x=20,y=30)
btn_exit=tk.Button(text='나가기',command=want2_exit)
btn_exit.place(x=500,y=10)
button=tk.Button(text='종남파라면 눌러주세요',command=click_btn2)
button.place(x=470,y=10)
cbtn=tk.Checkbutton(text='화산파라면 눌러주세요')
cbtn.place(x=500,y=30)

cbtn.pack()
text=tk.Text()
text.place(x=20,y=70,width=400,height=200)
button.pack()
r.mainloop()