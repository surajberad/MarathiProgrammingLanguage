
import shell
from tkinter import *



#file1.write("tesssmp")

# \n is placed to indicate EOL (End of Line)

root = Tk()
menu=Menu(root)

def run():
    txt1.delete('0.0', END)

    temp = txt.get("1.0", "end-1c")
    result=shell.getText(temp)

    txt1.insert(0.0, result)
    
File=Menu(menu,tearoff=0)
File.add_command(label='New Project',)
File.add_command(label='New File',)
File.add_command(label='Open',)
File.add_command(label='Save as..',)
File.add_command(label='Exit',)
menu.add_cascade(label='File',menu=File)

Edit=Menu(menu,tearoff=0)
Edit.add_command(label='Cut')
Edit.add_command(label='Copy')
Edit.add_command(label='Paste')
Edit.add_command(label='Undo')
Edit.add_command(label='Redo')
menu.add_cascade(label='Edit',menu=Edit)

Compile=Menu(menu,tearoff=0)
Compile.add_command(label='Comiple',command=run)
Compile.add_command(label='Run',command=run)
menu.add_cascade(label='Compile',menu=Compile)
root.config(menu=menu)
temp = StringVar()



txt=Text(root,width=100,height=13,wrap=WORD,font=('arial',17))
txt1=Text(root,width=100,height=13,wrap=WORD,font=('arial',17))
txt.grid(row=1,sticky=W)
txt1.grid(row=3,sticky=W)
















root.mainloop()