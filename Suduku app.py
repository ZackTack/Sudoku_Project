import tkinter as tk

class Application:
    def __init__(self,master):
        self.master = master
        master.geometry("500x500")
        master.title("Sudoku App")
        self.entry1 = tk.Entry(master,text="hello").pack()



if __name__ == '__main__':
    root = tk.Tk()
    sudoku = Application(root)
    root.mainloop()
