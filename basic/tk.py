import tkinter as tk

def showInfo():
    s1 = e1.get()
    s2 = e2.get()
    print("作品：{}\n作者：{}".format(s1, s2))

master = tk.Tk()

tk.Label(master, text="作品：").grid(row=0)
tk.Label(master, text="作者：").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)

s = e1.get()
print(s)

tk.Button(master, text="获取信息", width=10, command=showInfo).grid(row=3, column=0, sticky="w", padx=10, pady=5)
tk.Button(master, text="退出", width=10, command=master.quit).grid(row=3, column=1, sticky="e", padx=10, pady=5)

master.mainloop()
