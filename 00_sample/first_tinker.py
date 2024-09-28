import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self, text="Hello World\n(click me)", 
                          command=self.say_hi,
                          bg="lightblue",  # 背景色
                          fg="darkblue",   # 文字色
                          font=("Helvetica", 14, "bold"),  # フォントスタイル
                          borderwidth=5,   # ボーダー幅
                          relief="raised",  # ボタンの立体的な見た目
                          activebackground="lightgreen",  # クリック中の背景色
                          activeforeground="white"  # クリック中の文字色
                          )
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        # self.hi_there.pack(side="top")
        self.hi_there.place(x=50, y=50, width=150, height=50)

        self.quit = tk.Button(self, text="QUIT", fg="gray", command=root.destroy)
        # self.quit.pack(side="bottom")
        self.quit.place(x=50, y=120, width=100, height=50)

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
root.geometry("400x300+100+50")  # 画面サイズを設定と表示の初期位置を指定
app = Application(master=root)
app.mainloop()