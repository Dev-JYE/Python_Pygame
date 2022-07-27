import random as rd
import datetime as dt

alps=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
r=rd.choice(alps)
alp=''
for i in alps:
    if i!=r:
        alp+=i
print(alp)
st=dt.datetime.now()
ans=input('빠진 알파벳은 ? : ')
count=1
while True:
    if ans==r:
        print('정답입니다.')
        et=dt.datetime.now()
        print(str((et-st).seconds)+'초 걸렸습니다.')
        break
    else:
        print('틀렸습니다.')
        count+=1
        print(count,'회차')
        ans=input('빠진 알파벳은? : ')