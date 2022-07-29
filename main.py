from tkinter import ttk
import customtkinter
from races import get_races_data
from drivers import get_drivers_data
from teams import get_teams_data


def build_tree(data):
    tree["columns"] = tuple(data[0])
    tree['show'] = 'headings'
    # Create columns
    for each in data[0]:
        tree.column(each, anchor='w')
    # Create column headings
    for each in data[0]:
        tree.heading(each, text=each)
    # Create rows
    for each in data[1:]:
        tree.insert(parent="", index='end', text="", values=tuple(each))


def delete_tree_data():
    for each in tree.get_children():
        tree.delete(each)


def drivers_button_fun():
    delete_tree_data()
    build_tree(get_drivers_data())


def teams_button_fun():
    delete_tree_data()
    build_tree(get_teams_data())


def races_button_fun():
    delete_tree_data()
    build_tree(get_races_data())


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# Main window
window = customtkinter.CTk()
window.title("F1 2022 Results")
window.minsize(1000, 670)
window.config(padx=20, pady=50)

# Outer Frame
outer_frame = customtkinter.CTkFrame(master=window, fg_color="gray28", width=900, height=565, corner_radius=40)
outer_frame.grid(row=0, column=0, columnspan=6)
outer_frame.pack()

# Treeview frame
tree_frame = customtkinter.CTkFrame(master=outer_frame, fg_color="gray34", width=850, height=470, corner_radius=20)
tree_frame.place(x=450, y=260, anchor="center")

# Treeview
tree = ttk.Treeview(master=tree_frame, height=22)
tree.place(x=425, y=233, anchor="center")

# Buttons
drivers_button = customtkinter.CTkButton(master=outer_frame, text="Driver Standings", width=130, command=drivers_button_fun)
drivers_button.place(x=247, y=530, anchor="center")
teams_button = customtkinter.CTkButton(master=outer_frame, text="Team Standings", width=130, command=teams_button_fun)
teams_button.place(x=449, y=530, anchor="center")
races_button = customtkinter.CTkButton(master=outer_frame, text="Race Results", width=130, command=races_button_fun)
races_button.place(x=650, y=530, anchor="center")

# Show standings after launch
build_tree(get_drivers_data())

window.mainloop()
