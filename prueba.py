import tkinter

ventana = tkinter.Tk()
ventana.title("test")
ventana.geometry("100x50")
ventana.resizable(0,0)

cabezera = tkinter.Label(ventana, text="Test").pack()

ventana.mainloop()

