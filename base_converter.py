import tkinter as tk
import libdbc as rbc
window = tk.Tk()
window.title('Project Helix')
#window.geometry('400x300')
base = ['b','o','d','h']
#base = ['b','o','h']
label = {'b':'Binary', 'o':'Octal', 'd':'Decimal', 'h':'Hexa'}
symbol = {'b':'01',
          'o':'01234567',
          'd':'0123456789',
          'h':'0123456789abcdef'}
Smode = 0
def known(action, key, content, state):# tkinter treats all data as string, hence the value of action also in is prefered over == for char
    return True if not action == '1' or key in symbol[state] or key in symbol[state].upper() or (not '.' in content and key in '.') else False
vcmd = window.register(known)
def sync(c):
    global Smode
    Smode = base.index(c)
    for b in base:
        btn[b].config(state = tk.NORMAL)
        txt[b].config(state = tk.DISABLED)
    btn[base[Smode]].config(state = tk.DISABLED)
    txt[base[Smode]].config(state = tk.NORMAL)
    txt[base[Smode]].focus()

def tabed(event = None):
    c = (Smode+1) if Smode < 3 else 0
    sync(base[c])
    return('break')
    
def calc(event = 'none'):
    number = {i:'0.0' for i in base}
    C = txt[base[Smode]].get()
    if not C in ['']:
        number[base[Smode]] = C.lower() + ('.0' if not '.' in C else '0')
    number = rbc.generate(number)
    for i in base:
        txt[i].config(validate = 'none', state = tk.NORMAL)
        txt[i].delete(0, tk.END)
        txt[i].insert(0, number[i].upper())
        txt[i].config(validate = 'key', state = tk.DISABLED if not i == base[Smode] else tk.NORMAL)
window.bind('<Tab>',tabed)
window.bind('<space>',tabed)
window.bind('<Return>', calc)
# lambda is compiled after for loop, by then value of i is the last value in dictionary
btn = {i : tk.Button(window, text = j, width = 10, height = 2, command = lambda c = i: sync(c), font = ('default', 12)) for i,j in label.items()}
tk.Button(window, text = 'Calculate', width = 90, height = 2, font = ('default', 12), command = calc).grid(column = 0, row = 4, columnspan = 2, sticky = 'news')
txt = {i : tk.Entry(window, width = 100, font = ('default', 12), justify = 'right', validate = 'key', validatecommand = (vcmd, '%d', '%S', '%s', i)) for i,j in label.items()}
for i in base:
    btn[i].grid(column = 0, row = base.index(i), sticky = 'news')
    txt[i].grid(column = 1, row = base.index(i), sticky = 'news')
sync(base[Smode])
window.mainloop()
