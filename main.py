import tkinter as tk
from PIL import Image,ImageTk
root = tk.Tk()
#Main Code
root.title("MarcoEditor")
root.wm_iconbitmap('icons/icon.png')
#Imorting icons and images
new_icon=ImageTk.PhotoImage(Image.open("menu_icons/new.png"))
save_icon=ImageTk.PhotoImage(Image.open("menu_icons/save.png"))
open_icon=ImageTk.PhotoImage(Image.open("menu_icons/open.png"))
saveas_icon=ImageTk.PhotoImage(Image.open("menu_icons/saveas.png"))
exit_icon=ImageTk.PhotoImage(Image.open("menu_icons/exit.png"))
cut_icon=ImageTk.PhotoImage(Image.open("menu_icons/cut.png"))
copy_icon=ImageTk.PhotoImage(Image.open("menu_icons/copy.png"))
paste_icon=ImageTk.PhotoImage(Image.open("menu_icons/paste.png"))
undo_icon=ImageTk.PhotoImage(Image.open("menu_icons/undo.png"))
redo_icon=ImageTk.PhotoImage(Image.open("menu_icons/redo.png"))

#Making Menu Bar
menu_bar=tk.Menu(root)
#Making File Menu
file_menu=tk.Menu(menu_bar,tearoff=0)

file_menu.add_command(label="New",accelerator='Ctrl+N',compound='left',image=new_icon)
file_menu.add_separator()
file_menu.add_command(label="Open",accelerator='Ctrl+O',compound='left',image=open_icon)
file_menu.add_command(label="Save",accelerator='Ctrl+S',compound='left',image=save_icon)
file_menu.add_command(label="SaveAs",accelerator='Shift+Ctrl+S',compound='left',image=saveas_icon)
file_menu.add_separator()
file_menu.add_command(label="Exit",accelerator='Alt+F4',compound='left',image=exit_icon)
#Cascading File menu in the menu Bar
menu_bar.add_cascade(label="File",menu=file_menu)


#making Edit menu
edit_menu=tk.Menu(menu_bar,tearoff=0)

edit_menu.add_command(label="Undo",accelerator='Ctrl+Z',compound='left',image=undo_icon)
edit_menu.add_separator()
edit_menu.add_command(label="Redo",accelerator='Ctrl+Y',compound='left',image=redo_icon)
edit_menu.add_separator()
edit_menu.add_command(label="Cut",accelerator='Ctrl+X',compound='left',image=cut_icon)
edit_menu.add_command(label="Copy",accelerator='Ctrl+C',compound='left',image=copy_icon)
edit_menu.add_command(label="Paste",accelerator='Ctrl+V',compound='left',image=paste_icon)
edit_menu.add_command(label="Find",accelerator='Ctrl+F')
edit_menu.add_command(label="SelectAll",accelerator='Ctrl+A')
#Cascading Edit Menu in the Menu Bar
menu_bar.add_cascade(label="Edit",menu=edit_menu)


#making View Menu
view_menu=tk.Menu(menu_bar,tearoff=0)
#TODO -Add View Menu Items


#Cascading VIew Menu in the Menu Bar
menu_bar.add_cascade(label="View",menu=view_menu)



#making Help Menu
about_menu=tk.Menu(menu_bar,tearoff=0)

about_menu.add_command(label="About")
about_menu.add_command(label="Help")
#Cascading VIew Menu in the Menu Bar
menu_bar.add_cascade(label="About",menu=about_menu)

#Adding Menu_bar in root
root.config(menu=menu_bar)
root.mainloop()