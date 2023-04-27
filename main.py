

import random # 랜덤 모듈 사용

lotto_num = range(1,46) # 1-46까지 범위의 숫자를 사용하겠다.

for i in range(5): # 5번을 반복하겠다
    print(random.sample(lotto_num,6)) # 6개의 숫자를 출력하겠다.


import tkinter # tkinter 모듈 사용
import tkinter.font  #tkinter font를 사용
import random

lotto_num = range(1,46) #

def buttonClick(): # buttonClick 이라는 함수를 사용
    label = tkinter.Label(window, text=str(random.sample(lotto_num,6)))
    label.pack()
# 버튼을 클릭 했을때 나오는 문구를 설정 , lotto 번호를 6개 출력하겠다

window = tkinter.Tk()
window.title("lotto") # window 제목은 "lotto"
window.geometry("400x200") # window 크기는 400x200
window.resizable(False, False) # 크기 조절 x

button = tkinter.Button(window, overrelief="solid",text="번호확인",width=15, command=buttonClick,repeatdelay=1000, repeatinterval=100)
# tkinter.button 함수를 사용해 "번호확인" 이라는 버튼을 만들고 버튼을 클릭하는 시간은 1000, 누르고 있는 상태에서 메세지가 출력되는 간격은 100으로 한다)
button.pack()

window.mainloop() #행동이 끝나도 꺼지지 않고 켜져있도록 함



    
