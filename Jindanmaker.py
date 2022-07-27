import tkinter as tk

def click_btn():
      pts=0
      for i in range(7):
            if bvar[i].get()==True:
                  pts=pts+1
      godsaeng=int(100*pts/7)
      txt.delete('1.0',tk.END)
      txt.insert('1.0','<진단 결과>\n 당신의 갓생지수는'+str(godsaeng)+ '%입니다.\n'+results[pts])


def want2_exit():
    r.destroy()

r=tk.Tk()
r.title('갓생 지수 진단 게임')
r.resizable(False,False) #윈도우 사이즈 변경 불가!
cvs=tk.Canvas(r,width=800,height=700,bg='white')
cvs.pack()
#cvs['bg']으로 cvs에서 설정한 배경 색을 가져올 수 있다! 와 놀라운 파이썬세상~~
title=tk.Label(r,text='당신은 갓생을 살고 있나요?',font=('둥근모꼴',30),fg='Gray',bg=cvs['bg'])
title.place(x=150,y=30)

figio=tk.PhotoImage(file='Assets/화이팅죠르디.png')
cvs.create_image(150,200,image=figio)
pugio=tk.PhotoImage(file='Assets/뿌듯죠르디.png')
cvs.create_image(150,400,image=pugio)

#체크박스 아이콘들
chip=tk.PhotoImage(file='Assets/감자칩.png')
cvs.create_image(300,150,image=chip)
gampad=tk.PhotoImage(file='Assets/게임기.png')
cvs.create_image(300,200,image=gampad)
halfap=tk.PhotoImage(file='Assets/베어문사과.png')
cvs.create_image(300,250,image=halfap)
book=tk.PhotoImage(file='Assets/책.png')
cvs.create_image(300,300,image=book)
rose=tk.PhotoImage(file='Assets/장미.png')
cvs.create_image(300,350,image=rose)
samgim=tk.PhotoImage(file='Assets/삼김.png')
cvs.create_image(300,400,image=samgim)
apple=tk.PhotoImage(file='Assets/통사과.png')
cvs.create_image(300,450,image=apple)

#주석 리스트들
results=[
      'Seriously?',
      'Terrible',
      'Awful',
      '열심히 했군요',
      'Good',
      'Great',
      'Awesome',
      '당신이 프로갓생러!',
      ]

#버튼
btn=tk.Button(text='갓생 가보자고!',font=('둥근모꼴',17),bg='#BDE7C8',command=click_btn)
btn.place(x=400,y=500)
txt=tk.Text(width=30,height=3,font=('둥근모꼴',16),bg='#BDE7C8',fg='Gray')
txt.place(x=350,y=550)

btn_exit=tk.Button(text='나가기',font=('둥근모꼴',17),command=want2_exit,bg='Gray',fg='#BDE7C8')
btn_exit.place(x=600,y=500)

#None은 아무것도 존재하지 않음을 의미하는 값.
bvar=[None]*7  #bvar는 booleanvar 객체를 담기 위한 리스트!
cbtn=[None]*7 #체크박스 담기 위한 리스트. 아무것도 담겨 있지 않은 상태~
ITEM=['책을 읽었다.',
      '스크린타임이 5시간 미만이다.',
      '1일 1깃을 했다.',
      '블로그 챌린지를 완료했다.',
      '하고 싶은 일을 다 하지 않았다.',
      '지출을 하지 않았다.','부스트코스 강의를 들었다.'] #체크박스용 리스트,질문 넣어둠
for i in range(7):
      bvar[i]=tk.BooleanVar() #bvar의 0~6번에 불린 값 들어감
      bvar[i].set(False) #bvar의 기본값은 false
      cbtn[i]=tk.Checkbutton(text=ITEM[i],font=('둥근모꼴',15),variable=bvar[i],bg='#BDE7C8') #체크버튼의 글씨는 ITEM의 i번째에서 따옴.
      cbtn[i].place(x=330,y=130+50*i)
#git 업로드 확인용
r.mainloop()