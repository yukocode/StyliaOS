from tkinter import *
from tkinter import filedialog
import os

desktopOs = Tk()
desktopOs.title("StyliaOS - Desktop")
desktopOs.geometry("1000x500")
desktopOs.iconbitmap("")
desktopOs.maxsize(1000, 500)
desktopOs.minsize(800, 500)
desktopOs.bind('<Escape>',lambda e: desktopOs.destroy())

def browseFiles(): 
    filename = filedialog.askopenfilename(initialdir="/")


def fileexplorerEvent():
	fileexplorerGui = Toplevel()
	fileexplorerGui.geometry()
	fileexplorerGui.geometry("1000x500")
	fileexplorerGui.maxsize(1000, 500)
	fileexplorerGui.minsize(800, 500)
	fileexplorerGui.title("StyliaOS - File explorer")
	openAfile = Button(fileexplorerGui, text="Ouvrir un fichier", command=browseFiles).pack()


def executeProgram():
	nameProgram = input("Enter a name of program or command: ")
	if nameProgram == "options":
		optionClickEvent()
	elif nameProgram == "shutdown":
		desktopOs.destroy()
	elif nameProgram == "reload":
		reloadStyliaOS() 

def optionClickEvent():
	print("[StyliaOS] Launching options.")
	optionsGui = Toplevel()
	optionsGui.geometry("800x500")
	optionsGui.minsize(800, 500)
	optionsGui.maxsize(800, 500)
	optionsGui.title("StyliaOS - Options")

def reloadStyliaOS():
	desktopOs.destroy()
	os.system('ping localhost>nul')
	os.system('py start_styliaos.py')
	os.system('cls')

menu = Menu(desktopOs)

options = Menu(menu, tearoff=0)
startStyliaOSWindow = Menu(menu, tearoff=0)

startStyliaOSWindow.add_command(label="Eteindre StyliaOS.", command=desktopOs.quit)
startStyliaOSWindow.add_command(label="Redémarrer StyliaOS.", command=reloadStyliaOS)
startStyliaOSWindow.add_command(label="Executer un programme.", command=executeProgram)

options.add_command(label="Accédez au options.", command=optionClickEvent)

menu.add_cascade(label="Démarrer", menu=startStyliaOSWindow)
menu.add_cascade(label="Outils", menu=options)

fileexplorer = Button(desktopOs, text="Ouvrir l'explorateur de fichiers", command=fileexplorerEvent)

fileexplorer.pack()

desktopOs.config(menu=menu)
desktopOs.mainloop()