import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from pandastable import Table, TableModel

def make_calculator(tab):
    def click_button(value):
        current = str(display.get())
        display.set(current + value)

    def clear_display():
        display.set("")

    def calculate():
        try:
            result = eval(display.get())
            display.set(str(result))
        except Exception as e:
            display.set("Error")

    display = tk.StringVar()
    entry_display = tk.Entry(tab, textvariable=display, font=("Arial", 16), bd=10, insertwidth=4, width=20, borderwidth=4, justify='right')
    entry_display.grid(row=0, column=0, columnspan=4)

    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ]

    for (text, row, col) in buttons:
        action = lambda text=text: calculate() if text == '=' else clear_display() if text == 'C' else click_button(text)
        tk.Button(tab, text=text, padx=20, pady=20, font=("Arial", 12), command=action).grid(row=row, column=col, sticky="nsew")

def make_plotter(tab):
    sub_tab_control = ttk.Notebook(tab)
    plot_tab = ttk.Frame(sub_tab_control)
    table_tab = ttk.Frame(sub_tab_control)

    sub_tab_control.add(plot_tab, text='Graph')
    sub_tab_control.add(table_tab, text='Value Table')

    display = tk.StringVar()
    entry_function = tk.Entry(plot_tab, textvariable=display, font=("Arial", 16), width=15)
    entry_function.grid(row=0, column=0, columnspan=3)
    
    entry_start = tk.Entry(plot_tab, width=5)
    entry_start.grid(row=1, column=1)
    entry_stop = tk.Entry(plot_tab, width=5)
    entry_stop.grid(row=1, column=3)
    entry_step = tk.Entry(plot_tab, width=5)
    entry_step.grid(row=1, column=5)

    tk.Label(plot_tab, text="Start:").grid(row=1, column=0)
    tk.Label(plot_tab, text="Stop:").grid(row=1, column=2)
    tk.Label(plot_tab, text="Step:").grid(row=1, column=4)

    def plot():
        func = display.get()
        start = float(entry_start.get())
        stop = float(entry_stop.get())
        step = float(entry_step.get())
        x = np.arange(start, stop, step)
        y = eval(func)
        fig, ax = plt.subplots()
        ax.plot(x, y)
        canvas = FigureCanvasTkAgg(fig, master=plot_tab)
        canvas.draw()
        canvas.get_tk_widget().grid(row=2, column=0, columnspan=6)

    tk.Button(plot_tab, text="Plot", command=plot).grid(row=0, column=3)

    def update_table():
        func = display.get()
        start = float(entry_start.get())
        stop = float(entry_stop.get())
        step = float(entry_step.get())
        x = np.arange(start, stop, step)
        y = [eval(func) for x in x]
        df = pd.DataFrame({'X': x, 'Y': y})
        frame = tk.Frame(table_tab)
        frame.pack(fill='both', expand=True)
        pt = Table(frame, dataframe=df, showtoolbar=True, showstatusbar=True)
        pt.show()

    tk.Button(table_tab, text="Update Table", command=update_table).pack()

    sub_tab_control.pack(expand=1, fill='both')

def make_app():
    root = tk.Tk()
    root.title("Advanced Scientific Calculator")

    tab_control = ttk.Notebook(root)

    tab1 = ttk.Frame(tab_control)
    tab2 = ttk.Frame(tab_control)

    tab_control.add(tab1, text='Calculator')
    tab_control.add(tab2, text='Plotter')

    make_calculator(tab1)
    make_plotter(tab2)

    tab_control.pack(expand=1, fill='both')
    root.mainloop()

make_app()
