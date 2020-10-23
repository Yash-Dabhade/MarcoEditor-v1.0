import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
# Main Code
root.title("MarcoEditor")
root.wm_iconbitmap('icons/icon.png')
root.geometry("450x450")
root.minsize(250,300)
# Imorting icons and images
new_icon = ImageTk.PhotoImage(Image.open("menu_icons/new.png"))
save_icon = ImageTk.PhotoImage(Image.open("menu_icons/save.png"))
open_icon = ImageTk.PhotoImage(Image.open("menu_icons/open.png"))
saveas_icon = ImageTk.PhotoImage(Image.open("menu_icons/saveas.png"))
exit_icon = ImageTk.PhotoImage(Image.open("menu_icons/exit.png"))
cut_icon = ImageTk.PhotoImage(Image.open("menu_icons/cut.png"))
copy_icon = ImageTk.PhotoImage(Image.open("menu_icons/copy.png"))
paste_icon = ImageTk.PhotoImage(Image.open("menu_icons/paste.png"))
undo_icon = ImageTk.PhotoImage(Image.open("menu_icons/undo.png"))
redo_icon = ImageTk.PhotoImage(Image.open("menu_icons/redo.png"))

#Defining Functions
def cut():
    content_text.event_generate("<<Cut>>")
    return 'break'

def copy():
    content_text.event_generate("<<Copy>>")
    return 'break'

def paste():
    content_text.event_generate("<<Paste>>")
    return 'break'

def undo():
    content_text.event_generate("<<Undo>>")
    return 'break'

def redo(event=None):
    content_text.event_generate("<<Redo>>")
    return 'break'

# Making Menu Bar
menu_bar = tk.Menu(root)
# Making File Menu
file_menu = tk.Menu(menu_bar, tearoff=0)

file_menu.add_command(underline=0, label="New", accelerator='Ctrl+N', compound='left', image=new_icon)
file_menu.add_separator()
file_menu.add_command(label="Open", accelerator='Ctrl+O', compound='left', image=open_icon)
file_menu.add_command(label="Save", accelerator='Ctrl+S', compound='left', image=save_icon)
file_menu.add_command(label="SaveAs", accelerator='Shift+Ctrl+S', compound='left', image=saveas_icon)
file_menu.add_separator()
file_menu.add_command(label="Exit", accelerator='Alt+F4', compound='left', image=exit_icon)
# Cascading File menu in the menu Bar
menu_bar.add_cascade(label="File", menu=file_menu)

# making Edit menu
edit_menu = tk.Menu(menu_bar, tearoff=0)

edit_menu.add_command(label="Undo", accelerator='Ctrl+Z', compound='left', image=undo_icon,command=undo)
edit_menu.add_separator()
edit_menu.add_command(label="Redo", accelerator='Ctrl+Y', compound='left', image=redo_icon,command=redo)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", accelerator='Ctrl+X', compound='left', image=cut_icon,command=cut)
edit_menu.add_command(label="Copy", accelerator='Ctrl+C', compound='left', image=copy_icon,command=copy)
edit_menu.add_command(label="Paste", accelerator='Ctrl+V', compound='left', image=paste_icon,command=paste)
edit_menu.add_command(label="Find", accelerator='Ctrl+F', underline=0)
edit_menu.add_command(label="SelectAll", accelerator='Ctrl+A', underline=7)
# Cascading Edit Menu in the Menu Bar
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# making View Menu
view_menu = tk.Menu(menu_bar, tearoff=0)
# TODO -Add View Menu Items
show_line_number = tk.IntVar()
show_line_number.set(1)
view_menu.add_checkbutton(label="Show Line Numbers", variable=show_line_number)
show_cursor_info = tk.IntVar()
show_cursor_info.set(1)
view_menu.add_checkbutton(label="Show Cursor Location At bottom", variable=show_cursor_info)
highlight_line = tk.IntVar()
view_menu.add_checkbutton(label="Highlight Current Line", onvalue=1, offvalue=0, variable=highlight_line)
# Making Themes Menu is View meny
themes_menu = tk.Menu(view_menu, tearoff=0)
view_menu.add_cascade(label="Themes", menu=themes_menu)
# Defining color scheme

"""
color scheme is defined with dictionary elements like -
        theme_name : foreground_color.background_color
"""
color_schemes = {
    'Default': '#000000.#FFFFFF',
    'Greygarious': '#83406A.#D1D4D1',
    'Aquamarine': '#5B8340.#D1E7E0',
    'Bold Beige': '#4B4620.#FFF0E1',
    'Cobalt Blue': '#ffffBB.#3333aa',
    'Olive Green': '#D1E7E0.#5B8340',
    'Night Mode': '#FFFFFF.#000000',
}
theme_choice=tk.StringVar()
theme_choice.set('Default')
for k in sorted(color_schemes):
    themes_menu.add_radiobutton(label=k,variable=theme_choice)
# Cascading VIew Menu in the Menu Bar
menu_bar.add_cascade(label="View", menu=view_menu)

# making Help Menu
about_menu = tk.Menu(menu_bar, tearoff=0)

about_menu.add_command(label="About")
about_menu.add_command(label="Help")
# Cascading VIew Menu in the Menu Bar
menu_bar.add_cascade(label="About", menu=about_menu)

# Adding Menu_bar in root
root.config(menu=menu_bar)

# Making Shortcut Bar
shorcut_bar = tk.Frame(root, height=25, background='light sea green')
shorcut_bar.pack(expand='no', fill='x')

# MakingLineNumberBar
linenumber_bar = tk.Text(root, width=4, padx=3, takefocus=0, border=0, background='khaki',state='disabled',  wrap='none')
linenumber_bar.pack(side='left', fill='y')

# Adding Text area
content_text = tk.Text(root, wrap='word',undo=1)
content_text.pack(expand='yes', fill='both')

# Adding ScrollBar
scroll_bar = tk.Scrollbar(content_text)
content_text.configure(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=content_text.yview)
scroll_bar.pack(side="right", fill='y')

#Handling Shortcuts
content_text.bind('<Control-y>',redo)
content_text.bind('<Control-Y>',redo)

# main Loop
root.mainloop()
