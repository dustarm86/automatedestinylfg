import Tkinter
import tkMessageBox

window = Tkinter.Tk()
window.title("The Slightly Annoying Prog (v.1)")
window.geometry("350x250")

def scripts():
    import loop_scriptslfgnet

button = Tkinter.Button(window, text = "Click here to start", command = scripts)

button.pack()
window.mainloop()
