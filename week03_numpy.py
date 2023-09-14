import numpy as np
import random
import tkinter as tk  # Built in GUI

def click_button():
    try:

        n = int(en_number.get())
        l = [random.randint(1, 100) for i in range(n)]
        v = np.array(l, dtype='int16') #numpy 배열의 이름을 v로 정함
        lbl_result.config(text=v) #label 출력 변수를 만들었음 여기까지 백 쪽
    except ValueError as err:
        lbl_result.config(text=f"입력값이 없습니다.\n(err)")


window = tk.Tk() #여기서부터 프론트, 윈도우 생성자
window.title('numpy gui version v0.7') #제목에 들어갈 거
window.geometry('300x150') #수치 조절

# create widget
lbl_result = tk.Label(text="random numpy array") #임의의 그거다를 보여줌
en_number = tk.Entry() #별도의 객체는 없음 입력되는 값 넣을 거임
btn_click = tk.Button(text="click me!", command=click_button) #위에 있는 클릭 버튼으로 가서 숫자 넣어짐

# widget layout
lbl_result.pack()
en_number.pack(side='right')
btn_click.pack(side='right')

lbl_result.grid(row=0, column=0, columnspan=2)
en_number.grid(row=1, column=0)
btn_click.grid(row=1, column=1)

window.mainloop() #아두이누 loop처럼 끊기기 전까지 계속 실행