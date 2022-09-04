import tkinter
from tkinter import *
from tkinter import ttk

def main():
    opcion = None
    def reiniciar():
        window.destroy()
        main()

    window = tkinter.Tk()

    frame = ttk.Frame(window, padding= 30)
    frame.grid()

    ttk.Radiobutton(frame, padding=10, value=1).grid(column=0, row=0)
    ttk.Label(frame, padding=10, text="Opción 1").grid(column=1, row=0)

    ttk.Radiobutton(frame, padding=10, value=2).grid(column=0, row=1)
    ttk.Label(frame, padding=10, text="Opción 1").grid(column=1, row=1)

    ttk.Radiobutton(frame, padding=10, value=3).grid(column=0, row=2)
    ttk.Label(frame, padding=10, text="Opción 1").grid(column=1, row=2)

    ttk.Button(frame, padding=10,text="Reiniciar", command= reiniciar).grid(column=0, row=3)

    window.mainloop()

if __name__ == '__main__':
    main()
