import tkinter as tk
import subprocess

INPUT_FILE_NAME = "input.txt"

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        self.input_sample_label = tk.Label()
        self.input_sample_label["text"] = "入力例１"
        self.input_sample_label.place(x=10, y=10)

        self.input_sample_form = tk.Text()
        self.input_sample_form.place(x=20, y=30, width=320, height=50)

        self.output_sample_label = tk.Label()
        self.output_sample_label["text"] = "出力例１"
        self.output_sample_label.place(x=10, y=100)

        self.output_sample_form = tk.Text()
        self.output_sample_form.place(x=20, y=120, width=320, height=50)

        self.imp_btn = tk.Button(self, text="実行", 
                  command=self.implement_program,
                  bg="lightblue",  # 背景色
                  fg="darkblue",   # 文字色
                  font=("Helvetica", 14, "bold"),  # フォントスタイル
                  borderwidth=5,   # ボーダー幅
                  relief="raised",  # ボタンの立体的な見た目
                  activebackground="lightgreen",  # クリック中の背景色
                  activeforeground="white"  # クリック中の文字色
                  )
        self.imp_btn.place(x=150, y=200, width=100, height=30)

    def implement_program(self):
        with open(INPUT_FILE_NAME, mode='w') as input:
            input.write(self.input_sample_form.get(0., tk.END))

        result = subprocess.run('powershell -Command "Get-Content .\\input.txt | python .\\program.py"', 
                            shell=True, 
                            capture_output=True, 
                            text=True)
                
        ideal_output = self.output_sample_form.get(0., tk.END)

        if ideal_output.strip() == result.stdout.strip():
            print('OK')
        else:
            print('NG:' + result.stdout + " : " + ideal_output)


root = tk.Tk()
root.title('競プロ 実行例テスト')
root.geometry("400x300+100+50")  # 画面サイズを設定と表示の初期位置を指定
app = Application(master=root)
app.mainloop()