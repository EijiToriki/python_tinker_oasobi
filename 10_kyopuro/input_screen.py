import tkinter as tk
import subprocess
import requests
from bs4 import BeautifulSoup

INPUT_FILE_NAME = "input.txt"

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        self.contest_num_label = tk.Label()
        self.contest_num_label["text"] = "コンテスト番号："
        self.contest_num_label.place(x=10, y=10)

        self.contest_num_form = tk.Text()
        self.contest_num_form.place(x=100, y=12, width=50, height=16)

        self.question_label = tk.Label()
        self.question_label["text"] = "問題："
        self.question_label.place(x=200, y=10)

        self.question_form = tk.Text()
        self.question_form.place(x=240, y=12, width=20, height=16)

        self.input_sample_label = tk.Label()
        self.input_sample_label["text"] = "入力例１"
        self.input_sample_label.place(x=10, y=50)

        self.input_sample_form = tk.Text()
        self.input_sample_form.place(x=20, y=70, width=320, height=50)

        self.output_sample_label = tk.Label()
        self.output_sample_label["text"] = "出力例１"
        self.output_sample_label.place(x=10, y=140)

        self.output_sample_form = tk.Text()
        self.output_sample_form.place(x=20, y=160, width=320, height=50)

        self.result_label = tk.Label()
        self.result_label["text"] = "実行結果"
        self.result_label.place(x=10, y=220) 

        self.result_text = tk.Label()
        self.result_text["text"] = "実行ボタンを押してください"
        self.result_text["fg"] = "gray"
        self.result_text.place(x=20, y=240)

        self.scrap_btn = tk.Button(self, text="入出力例取得", 
                  command=self.scraping_in_out,
                  bg="lightblue",  # 背景色
                  fg="darkblue",   # 文字色
                  font=("Helvetica", 12, "bold"),  # フォントスタイル
                  borderwidth=5,   # ボーダー幅
                  relief="raised",  # ボタンの立体的な見た目
                  activebackground="lightgreen",  # クリック中の背景色
                  activeforeground="white"  # クリック中の文字色
                  )
        self.scrap_btn.place(x=50, y=290, width=120, height=30)

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
        self.imp_btn.place(x=230, y=290, width=120, height=30)

    def implement_program(self):
        with open(INPUT_FILE_NAME, mode='w') as input:
            input.write(self.input_sample_form.get(0., tk.END))

        result = subprocess.run('powershell -Command "Get-Content .\\input.txt | python .\\program.py"', 
                            shell=True, 
                            capture_output=True, 
                            text=True)
                
        ideal_output = self.output_sample_form.get(0., tk.END)

        if ideal_output.strip() == result.stdout.strip():
            self.result_text["text"] = "OK"
            self.result_text["fg"] = "green"
            self.result_text["font"] = ("Helvetica", 16, "bold")
        else:
            self.result_text["text"] = "NG"
            self.result_text["fg"] = "red"
            self.result_text["font"] = ("Helvetica", 16, "bold")
    
    def scraping_in_out(self):
        contest_num = self.contest_num_form.get(0., tk.END).replace("\n", "")
        question = self.question_form.get(0., tk.END).replace("\n", "")
        URL = "https://atcoder.jp/contests/abc373/tasks/abc" + contest_num + "_" + question

        res = requests.get(URL)
        soup = BeautifulSoup(res.text, 'html.parser')
        ## 入力例2個：10 入力例が1,3, 出力例が2,4
        ## 入力例3個：14 入力例が1,3,5 出力例が2,4,6
        pre_contents = soup.find_all('pre')
        input_sample = pre_contents[1].text
        output_sample = pre_contents[2].text

        self.input_sample_form.delete(1.0, tk.END)
        self.input_sample_form.insert(tk.END, input_sample)

        self.output_sample_form.delete(1.0, tk.END)
        self.output_sample_form.insert(tk.END, output_sample)
        


root = tk.Tk()
root.title('競プロ 実行例テスト')
root.geometry("400x350+100+50")  # 画面サイズを設定と表示の初期位置を指定
app = Application(master=root)
app.mainloop()