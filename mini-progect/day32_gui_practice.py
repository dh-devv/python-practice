import tkinter as tk

window = tk.Tk()

window.title("GUI 연습하기")
window.geometry("500x500")
window.resizable(False, False)

label = tk.Label(window, text="2026-5-10", font = ("궁서체", 20)).grid( row = 0, column = 0)
button = tk.Button(window, text="버튼", font = ("굴림", 20)).grid( row = 1, column = 0)

window.mainloop()
