import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Mértékegység Átváltó")
title_label = tk.Label(root, text="Mértékegység Átváltó", font=("Arial", 16))
title_label.pack(pady=20)
def open_length_conversion():
    length_window = tk.Toplevel(root)
    length_window.title("Hossz Átváltás")
    entry_label = tk.Label(length_window, text="Adja meg az értéket:")
    global entry_l
    entry_label.pack(pady=5)
    entry_l = tk.Entry(length_window)
    entry_l.pack(pady=5)
    global from_unit_var_l
    from_unit_var_l = tk.StringVar(value="Méter")
    from_unit_label = tk.Label(length_window, text="Kezdő mértékegység:")
    from_unit_label.pack(pady=5)
    from_unit_menu = tk.OptionMenu(length_window, from_unit_var_l, "Méter", "Kilométer", "Yard", "Mérföld")
    from_unit_menu.pack(pady=5)
    global to_unit_var_l
    to_unit_var_l = tk.StringVar(value="Kilométer")
    to_unit_label = tk.Label(length_window, text="Cél mértékegység:")
    to_unit_label.pack(pady=5)
    to_unit_menu = tk.OptionMenu(length_window, to_unit_var_l, "Méter", "Kilométer", "Yard", "Mérföld")
    to_unit_menu.pack(pady=5)
    convert_button = tk.Button(length_window, text="Számolás", command=convert_length)
    convert_button.pack(pady=10)
    global result_label_l
    result_label_l = tk.Label(length_window, text="Eredmény:")
    result_label_l.pack(pady=5)
    close_button = tk.Button(length_window, text="Bezárás", command=length_window.destroy)
    close_button.pack(pady=5)
def open_weight_conversion():
    weight_window = tk.Toplevel(root)
    weight_window.title("Tömeg Átváltás")
    entry_label = tk.Label(weight_window, text="Adja meg az értéket:")
    entry_label.pack(pady=5)
    global entry_w
    entry_w = tk.Entry(weight_window)
    entry_w.pack(pady=5)
    global from_unit_var_w
    from_unit_var_w = tk.StringVar(value="Kilogramm")
    from_unit_label = tk.Label(weight_window, text="Kezdő mértékegység:")
    from_unit_label.pack(pady=5)
    from_unit_menu = tk.OptionMenu(weight_window, from_unit_var_w, "Kilogramm", "Gramm", "Font", "Ounce")
    from_unit_menu.pack(pady=5)
    global to_unit_var_w
    to_unit_var_w = tk.StringVar(value="Gramm")
    to_unit_label = tk.Label(weight_window, text="Cél mértékegység:")
    to_unit_label.pack(pady=5)
    to_unit_menu = tk.OptionMenu(weight_window, to_unit_var_w, "Kilogramm", "Gramm", "Font", "Ounce")
    to_unit_menu.pack(pady=5)
    convert_button = tk.Button(weight_window, text="Számolás", command=convert_weight)
    convert_button.pack(pady=10)
    global result_label_w
    result_label_w = tk.Label(weight_window, text="Eredmény:")
    result_label_w.pack(pady=5)
    close_button = tk.Button(weight_window, text="Bezárás", command=weight_window.destroy)
    close_button.pack(pady=5)
def open_time_conversion():
    time_window = tk.Toplevel(root)
    time_window.title("Idő Átváltás")
    entry_label = tk.Label(time_window, text="Adja meg az értéket:")
    entry_label.pack(pady=5)
    global entry_t
    entry_t = tk.Entry(time_window)
    entry_t.pack(pady=5)
    global from_unit_var_t
    from_unit_var_t = tk.StringVar(value="Másodperc")
    from_unit_label = tk.Label(time_window, text="Kezdő mértékegység:")
    from_unit_label.pack(pady=5)
    from_unit_menu = tk.OptionMenu(time_window, from_unit_var_t, "Másodperc", "Perc", "Óra", "Nap")
    from_unit_menu.pack(pady=5)
    global to_unit_var_t
    to_unit_var_t = tk.StringVar(value="Perc")
    to_unit_label = tk.Label(time_window, text="Cél mértékegység:")
    to_unit_label.pack(pady=5)
    to_unit_menu = tk.OptionMenu(time_window, to_unit_var_t, "Másodperc", "Perc", "Óra", "Nap")
    to_unit_menu.pack(pady=5)
    convert_button = tk.Button(time_window, text="Számolás", command=convert_time)
    convert_button.pack(pady=10)
    global result_label_t
    result_label_t = tk.Label(time_window, text="Eredmény:")
    result_label_t.pack(pady=5)
    close_button = tk.Button(time_window, text="Bezárás", command=time_window.destroy)
    close_button.pack(pady=5)
length_button = tk.Button(root, text="Hossz", command=open_length_conversion, width=20)
length_button.pack(pady=10)
weight_button = tk.Button(root, text="Tömeg", command=open_weight_conversion, width=20)
weight_button.pack(pady=10)
time_button = tk.Button(root, text="Idő", command=open_time_conversion, width=20)
time_button.pack(pady=10)
def quit_program():
    root.quit()
exit_button = tk.Button(root, text="Kilépés", command=quit_program)
exit_button.pack(pady=20)
def convert_length():
    try:
        value = float(entry_l.get())
        from_unit = from_unit_var_l.get()
        to_unit = to_unit_var_l.get()
        conversion_factors = {
            "Méter": 1,
            "Kilométer": 0.001,
            "Yard": 1.09361,
            "Mérföld": 0.000621371,
        }
        converted_value = value * (conversion_factors[to_unit] / conversion_factors[from_unit])
        result_label_l.config(text=f"Eredmény: {converted_value:.4f} {to_unit}")
    except ValueError:
        messagebox.showerror("Hiba", "Kérjük, adjon meg egy érvényes számot!")
def convert_weight():
    try:
        value = float(entry_w.get())
        from_unit = from_unit_var_w.get()
        to_unit = to_unit_var_w.get()
        conversion_factors = {
            "Kilogramm": 1,
            "Gramm": 1000,
            "Font": 2.20462,
            "Ounce": 35.274,
        }
        converted_value = value * (conversion_factors[to_unit] / conversion_factors[from_unit])
        result_label_w.config(text=f"Eredmény: {converted_value:.4f} {to_unit}")
    except ValueError:
        messagebox.showerror("Hiba", "Kérjük, adjon meg egy érvényes számot!")
def convert_time():
    try:
        value = float(entry_t.get())
        from_unit = from_unit_var_t.get()
        to_unit = to_unit_var_t.get()
        conversion_factors = {
            "Másodperc": 1,
            "Perc": 1/60,
            "Óra": 1/3600,
            "Nap": 1/86400,
        }    
        converted_value = value * (conversion_factors[to_unit] / conversion_factors[from_unit])
        result_label_t.config(text=f"Eredmény: {converted_value:.4f} {to_unit}")
    except ValueError:
        messagebox.showerror("Hiba", "Kérjük, adjon meg egy érvényes számot!")

root.mainloop()