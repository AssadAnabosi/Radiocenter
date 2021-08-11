from tkinter import *
from tkinter import ttk

# Global vars
modes = [
    "Case",
    "Trade"
]
with open("name.cfg", 'r', encoding="utf-8") as name_file:
    name = name_file.read()
    name_file.close()
victim = "Player"
item = "Karambit"
paint_kit = "Autotronic"

# rarity = "Covert (Red)"
rarity_data = [
    "Covert (Red)",
    "Classified (Pink)",
    "Mil-Spec (Blue)"
]

rarity_codes = {
    "Covert (Red)": '',
    "Classified (Pink)": '',
    "Mil-Spec (Blue)": ''}

x_label = 10
x_entry = 105
w_entry = 30
fg = '#F2AA4C'
bg = '#101820'


def save():
    with open("name.cfg", 'w', encoding="utf-8") as name_file:
        name_file.write(name_entry.get())
        name_file.close()


def copy():
    result = ""
    if my_notebook.tab(my_notebook.select(), "text") == "Case/Trade":
        global name, item, paint_kit
        name = name_entry.get()
        item = item_entry.get()
        paint_kit = paint_kit_entry.get()
        if starred.get():
            star = "★"
        else:
            star = ""
        if stat_tracked.get():
            stat_track = " StatTrak™ "
        else:
            stat_track = ""
        if mode.get() == "Case":
            result = 'playerradio Radio.Cheer "Cheer!\u2028\x03\x03' + name + ' \x01has opened a container and found: ' + \
                     rarity_codes[rarity.get()] + star + stat_track + item + " | " + paint_kit + '"'
        elif mode.get() == "Trade":
            result = 'playerradio Radio.Cheer "Cheer!\u2028\x03\x03' + name + ' \x01has received in trade: ' + \
                     rarity_codes[rarity.get()] + star + stat_track + item + " | " + paint_kit + '"'
    elif my_notebook.tab(my_notebook.select(), "text") == "Ban":
        global victim
        victim = victim_entry.get()
        result = 'playerradio Radio.Cheer "Cheer! ' + victim + ' has been permanently banned from official CS:GO servers."'
    root.clipboard_clear()
    root.clipboard_append(result)
    root.update()
    print(result)


root = Tk()

root.geometry('450x400+150+150')
root.title('CS:GO Radio Center By Err0R')
root.resizable(width=FALSE, height=FALSE)
root.iconbitmap('csgo.ico')
root.configure(bg=bg)

my_notebook = ttk.Notebook(root)
my_notebook.pack()

fake_inv = Frame(my_notebook, width=450, height=500, bg=bg)
fake_ban = Frame(my_notebook, width=450, height=500, bg=bg)

fake_inv.pack(fill="both", expand=1)
fake_ban.pack(fill="both", expand=1)

my_notebook.add(fake_inv, text="Case/Trade")
my_notebook.add(fake_ban, text="Ban")

# Fake Case / Trade..!

# Case/Trade Drop Down Menu
mode_label = Label(fake_inv, fg=fg, bg=bg, text="Case/Trade")
mode_label.place(x=x_label, y=15)

mode = StringVar(root)
mode.set(modes[0])  # default value

mode_drop_menu = OptionMenu(fake_inv, mode, *modes)
mode_drop_menu.config(bg=bg, fg=fg, width=5)
mode_drop_menu["menu"].config(bg=bg, fg=fg)
mode_drop_menu.place(x=x_entry, y=10)

# name label, entry and save button
name_label = Label(fake_inv, fg=fg, bg=bg, text="Your Name")
name_label.place(x=x_label, y=45)

name_entry = Entry(fake_inv, width=w_entry)
name_entry.insert(0, name)
name_entry.place(x=x_entry, y=45, height=25)

save_button = Button(fake_inv, text="Save", fg=bg, bg=fg, width='8', command=save).place(x=x_entry + 200, y=45)

# item label and entry
item_label = Label(fake_inv, fg=fg, bg=bg, text="Item")
item_label.place(x=x_label, y=75)

item_entry = Entry(fake_inv, width=w_entry)
item_entry.insert(0, item)
item_entry.place(x=x_entry, y=75, height=25)

# starred label and check box
starred_label = Label(fake_inv, fg=fg, bg=bg, text="Knife or gloves?")
starred_label.place(x=x_label, y=105)

starred = BooleanVar(value=True)
starred_button = Checkbutton(fake_inv, variable=starred, onvalue=True, offvalue=False, bg=bg, fg=fg).place(x=x_entry,
                                                                                                           y=105)

# item label and entry
paint_kit_label = Label(fake_inv, fg=fg, bg=bg, text="Paint Kit")
paint_kit_label.place(x=x_label, y=135)

paint_kit_entry = Entry(fake_inv, width=w_entry)
paint_kit_entry.insert(0, paint_kit)
paint_kit_entry.place(x=x_entry, y=135, height=25)

# starred label and check box
stat_tracked_label = Label(fake_inv, fg=fg, bg=bg, text="StatTrack™")
stat_tracked_label.place(x=x_label, y=165)

stat_tracked = BooleanVar(value=True)
stat_tracked_button = Checkbutton(fake_inv, variable=stat_tracked, onvalue=True, offvalue=False, bg=bg, fg=fg).place(
    x=x_entry,
    y=165)

# Rarity Drop Down Menu
rarity_label = Label(fake_inv, fg=fg, bg=bg, text="Rarity")
rarity_label.place(x=x_label, y=200)

rarity = StringVar(root)
rarity.set(rarity_data[0])  # default value

rarity_drop_menu = OptionMenu(fake_inv, rarity, *rarity_data)
rarity_drop_menu.config(bg=bg, fg=fg, width=15)
rarity_drop_menu["menu"].config(bg=bg, fg=fg)
rarity_drop_menu.place(x=x_entry, y=195)

# buttons..
copy_button = Button(fake_inv, text="Copy", fg=bg, bg=fg, width='12', command=copy).place(x=x_entry, y=235)

# Fake Ban..!

# name label and entry
victim_label = Label(fake_ban, fg=fg, bg=bg, text="Victim's Name")
victim_label.place(x=x_label, y=10)

victim_entry = Entry(fake_ban, width=w_entry)
victim_entry.insert(0, name)
victim_entry.place(x=x_entry, y=10, height=25)

# buttons..
copy_button = Button(fake_ban, text="Copy", fg=bg, bg=fg, width='12', command=copy).place(x=x_entry, y=50)

# CR MARK
follow_label = Label(fg=fg, bg=bg, text="Steam: /iiErr0R").place(x=5, y=375)

root.mainloop()
