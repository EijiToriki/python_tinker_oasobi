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
        self.question_label.place(x=170, y=10)

        self.question_form = tk.Text()
        self.question_form.place(x=210, y=12, width=20, height=16)

        self.input_sample_label = tk.Label()
        self.input_sample_label["text"] = "入力例１"
        self.input_sample_label.place(x=10, y=40)

        self.input_sample_form = tk.Text()
        self.input_sample_form.place(x=20, y=60, width=150, height=50)

        self.output_sample_label = tk.Label()
        self.output_sample_label["text"] = "出力例１"
        self.output_sample_label.place(x=10, y=130)

        self.output_sample_form = tk.Text()
        self.output_sample_form.place(x=20, y=150, width=150, height=30)

        self.input_sample_label2 = tk.Label()
        self.input_sample_label2["text"] = "入力例２"
        self.input_sample_label2.place(x=180, y=40)

        self.input_sample_form2 = tk.Text()
        self.input_sample_form2.place(x=190, y=60, width=150, height=50)

        self.output_sample_label2 = tk.Label()
        self.output_sample_label2["text"] = "出力例２"
        self.output_sample_label2.place(x=180, y=130)

        self.output_sample_form2 = tk.Text()
        self.output_sample_form2.place(x=190, y=150, width=150, height=30)

        self.input_sample_label3 = tk.Label()
        self.input_sample_label3["text"] = "入力例３"
        self.input_sample_label3.place(x=350, y=40)

        self.input_sample_form3 = tk.Text()
        self.input_sample_form3.place(x=360, y=60, width=150, height=50)

        self.output_sample_label3 = tk.Label()
        self.output_sample_label3["text"] = "出力例３"
        self.output_sample_label3.place(x=350, y=130)

        self.output_sample_form3 = tk.Text()
        self.output_sample_form3.place(x=360, y=150, width=150, height=30)

        self.result_label = tk.Label()
        self.result_label["text"] = "実行結果１"
        self.result_label.place(x=10, y=200) 

        self.result_text = tk.Label()
        self.result_text["text"] = "実行ボタンを押してください"
        self.result_text["fg"] = "gray"
        self.result_text.place(x=20, y=220)

        self.result_label2 = tk.Label()
        self.result_label2["text"] = "実行結果２"
        self.result_label2.place(x=180, y=200) 

        self.result_text2 = tk.Label()
        self.result_text2["text"] = "実行ボタンを押してください"
        self.result_text2["fg"] = "gray"
        self.result_text2.place(x=190, y=220)

        self.result_label3 = tk.Label()
        self.result_label3["text"] = "実行結果３"
        self.result_label3.place(x=350, y=200) 

        self.result_text3 = tk.Label()
        self.result_text3["text"] = "実行ボタンを押してください"
        self.result_text3["fg"] = "gray"
        self.result_text3.place(x=360, y=220)

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
        self.scrap_btn.place(x=90, y=260, width=120, height=30)

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
        self.imp_btn.place(x=300, y=260, width=120, height=30)

    def implement_program(self):
        ## 入出力例１
        input_text = self.input_sample_form.get(0., tk.END).replace('\r\n', '\n').replace('\r', '\n').strip()
        with open(INPUT_FILE_NAME, mode='w') as input_file:
            input_file.write(input_text)

        result = subprocess.run('powershell -Command "Get-Content .\\input.txt | python .\\program.py"', 
                            shell=True, 
                            capture_output=True, 
                            text=True)
                
        ideal_output = self.output_sample_form.get(0., tk.END)

        if len(input_text) == 0:
            self.result_text["text"] = "未入力"
            self.result_text["fg"] = "gray"
            self.result_text["font"] = ("Helvetica", 12, "bold")
        elif ideal_output.strip() == result.stdout.strip():
            self.result_text["text"] = "OK"
            self.result_text["fg"] = "green"
            self.result_text["font"] = ("Helvetica", 16, "bold")
        else:
            self.result_text["text"] = "NG"
            self.result_text["fg"] = "red"
            self.result_text["font"] = ("Helvetica", 16, "bold")

        ## 入出力例２
        input_text = self.input_sample_form2.get(0., tk.END).replace('\r\n', '\n').replace('\r', '\n').strip()
        with open(INPUT_FILE_NAME, mode='w') as input_file:
            input_file.write(input_text)

        result = subprocess.run('powershell -Command "Get-Content .\\input.txt | python .\\program.py"', 
                            shell=True, 
                            capture_output=True, 
                            text=True)
                
        ideal_output = self.output_sample_form2.get(0., tk.END)

        if len(input_text) == 0:
            self.result_text2["text"] = "未入力"
            self.result_text2["fg"] = "gray"
            self.result_text2["font"] = ("Helvetica", 12, "bold")
        elif ideal_output.strip() == result.stdout.strip():
            self.result_text2["text"] = "OK"
            self.result_text2["fg"] = "green"
            self.result_text2["font"] = ("Helvetica", 16, "bold")
        else:
            self.result_text2["text"] = "NG"
            self.result_text2["fg"] = "red"
            self.result_text2["font"] = ("Helvetica", 16, "bold")

        ## 入出力例３
        input_text = self.input_sample_form3.get(0., tk.END).replace('\r\n', '\n').replace('\r', '\n').strip()
        with open(INPUT_FILE_NAME, mode='w') as input_file:
            input_file.write(input_text)

        result = subprocess.run('powershell -Command "Get-Content .\\input.txt | python .\\program.py"', 
                            shell=True, 
                            capture_output=True, 
                            text=True)
                
        ideal_output = self.output_sample_form3.get(0., tk.END)

        if len(input_text) == 0:
            self.result_text3["text"] = "未入力"
            self.result_text3["fg"] = "gray"
            self.result_text3["font"] = ("Helvetica", 12, "bold")
        elif ideal_output.strip() == result.stdout.strip():
            self.result_text3["text"] = "OK"
            self.result_text3["fg"] = "green"
            self.result_text3["font"] = ("Helvetica", 16, "bold")
        else:
            self.result_text3["text"] = "NG"
            self.result_text3["fg"] = "red"
            self.result_text3["font"] = ("Helvetica", 16, "bold")
    
    def scraping_in_out(self):
        contest_num = self.contest_num_form.get(0., tk.END).replace("\n", "")
        question = self.question_form.get(0., tk.END).replace("\n", "")
        URL = "https://atcoder.jp/contests/abc" + contest_num + "/tasks/abc" + contest_num + "_" + question

        res = requests.get(URL)
        soup = BeautifulSoup(res.text, 'html.parser')
        pre_contents = soup.find_all('pre')

        if(len(pre_contents) >= 10):
            self.input_sample_form.delete(1.0, tk.END)
            self.input_sample_form.insert(tk.END, pre_contents[1].text)

            self.output_sample_form.delete(1.0, tk.END)
            self.output_sample_form.insert(tk.END, pre_contents[2].text)
            
            self.input_sample_form2.delete(1.0, tk.END)
            self.input_sample_form2.insert(tk.END, pre_contents[3].text)

            self.output_sample_form2.delete(1.0, tk.END)
            self.output_sample_form2.insert(tk.END, pre_contents[4].text)

        if(len(pre_contents) >= 14):
            self.input_sample_form3.delete(1.0, tk.END)
            self.input_sample_form3.insert(tk.END, pre_contents[5].text)

            self.output_sample_form3.delete(1.0, tk.END)
            self.output_sample_form3.insert(tk.END, pre_contents[6].text)

            

        


root = tk.Tk()
root.title('競プロ 実行例テスト')
root.geometry("530x320+100+50")  # 画面サイズを設定と表示の初期位置を指定
app = Application(master=root)
app.mainloop()