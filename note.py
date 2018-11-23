import tkinter as tk
from tkinter.messagebox import showinfo
import tkinter.filedialog as filedialog
import os


fileName = ''


def author():
    showinfo('作者信息', '该Note是由Yanbin完成')


def copyRight():
    showinfo('版权信息', '该Note归属于Yanbin\n个人博客：blog.luoyanbin.cn')


def open_file():
    global fileName
    fileName = filedialog.askopenfilename(defaultextension='.txt')
    if fileName == '':
        fileName = None
    else:
        root.title('File Name: ' + os.path.basename(fileName))
        textPad.delete(1.0, 'end')
        f = open(fileName, 'r')
        textPad.insert(1.0, f.read())
        f.close()


def new_file():
    global fileName
    root.title('未命名文件')
    fileName = None
    textPad.delete(1.0, 'end')


def save():
    global fileName
    try:
        f = open(fileName, 'w')
        text2write = textPad.get(1.0, 'end')
        f.write(text2write)
        f.close()
    except:
        save_as()


def save_as():
    f = filedialog.asksaveasfilename(initialfile='未命名.txt', defaultextension='.txt')
    global fileName
    fileName = f
    fw = open(f, 'w')
    text2write = textPad.get(1.0, 'end')
    fw.write(text2write)
    fw.close()
    root.title('File Name: ' + os.path.basename(fileName))


def cut():
    textPad.event_generate('<<Cut>>')


def copy():
    textPad.event_generate('<<Copy>>')


def paste():
    textPad.event_generate('<<Paste>>')


def redo():
    textPad.event_generate('<<Redo>>')


def undo():
    textPad.event_generate('<<Undo>>')


def select_all():
    textPad.tag_add('sel', '1.0', 'end')


def search():
    def execute_search():
        pass

    topSearch = tk.Toplevel(root)
    topSearch.geometry('300x30+200+250')
    label1 = tk.Label(topSearch, text='Find')
    label1.grid(row=0, column=0, padx=5)
    entry1 = tk.Entry(topSearch, width=20)
    entry1.grid(row=0, column=1, padx=5)
    button1 = tk.Button(topSearch, text='查找', command=execute_search)
    button1.grid(row=0, column=2)


root = tk.Tk()
root.title('Little Note')
root.geometry("500x500+100+100")

# Create Menu
menuBar = tk.Menu(root)
root.config(menu=menuBar)

fileMenu = tk.Menu(menuBar)
fileMenu.add_command(label='新建', accelerator='Ctrl + N', command=new_file)
fileMenu.add_command(label='打开', accelerator='Ctrl + O', command=open_file)
fileMenu.add_command(label='保存', accelerator='Ctrl + S', command=save)
fileMenu.add_command(label='另存为', accelerator='Ctrl + Shift + N', command=save_as)
menuBar.add_cascade(label='文件', menu=fileMenu)

editMenu = tk.Menu(menuBar)
editMenu.add_command(label='撤销', accelerator='Ctrl + Z', command=undo)
editMenu.add_command(label='重做', accelerator='Ctrl + y', command=redo)
editMenu.add_separator()
editMenu.add_command(label='剪切', accelerator='Ctrl + X', command=cut)
editMenu.add_command(label='复制', accelerator='Ctrl + C', command=copy)
editMenu.add_command(label='粘贴', accelerator='Ctrl + V', command=paste)
editMenu.add_separator()
editMenu.add_command(label='查找', accelerator='Ctrl + F', command=search)
editMenu.add_command(label='全选', accelerator='Ctrl + A', command=select_all)
menuBar.add_cascade(label='编辑', menu=editMenu)

aboutMenu = tk.Menu(menuBar)
aboutMenu.add_command(label='作者', command=author)
aboutMenu.add_command(label='版权', command=copyRight)
menuBar.add_cascade(label='关于', menu=aboutMenu)


# Create toolBar
toolBar = tk.Frame(root, height=25, bg='light sea green')

shortButton = tk.Button(toolBar, text='打开', command=open_file)
shortButton.pack(side='left', padx=5, pady=5)

shortButton = tk.Button(toolBar, text='保存', command=save)
shortButton.pack(side='left')

toolBar.pack(side='top', fill='x', expand='no')


# Create Status Bar
status = tk.Label(root, text='Ln20', bd=1, relief='sunken', anchor='w')
status.pack(side='bottom', fill='x')


# Create Line Number & Text
lineLable = tk.Label(root, width=2, bg='antique white')
lineLable.pack(side='left', fill='y')

textPad = tk.Text(root, undo=True)
textPad.pack(expand='yes', fill='both')

scroll = tk.Scrollbar(textPad)
textPad.config(yscrollcommand=scroll.set)
scroll.config(command=textPad.yview)
scroll.pack(side='right', fill='y')


root.mainloop()
