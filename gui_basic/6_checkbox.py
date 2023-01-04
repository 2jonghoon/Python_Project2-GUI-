from tkinter import *

root = Tk()

root.title("Jh GUI")
root.geometry("640x480+300+100") # 가로 x 세로 + x 좌표 + y 좌표

chkvar = IntVar() # chkvar에 int 형으로 값 저장
chkbox = Checkbutton(root, text="오루 하루 보지 않기", variable=chkvar)
chkbox.select() # 자동 선택 처리
chkbox.deselect() # 선택 해제 처리
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
chkbox2.pack()


def btncmd():
  print(chkvar.get()) # 0: 체크 해제, 1: 체크
  print(chkvar2.get())
  
btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()