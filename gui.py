import tkinter as tk
import app
import json
import sys
from urllib import request, error

CHECKOUT_API_URL = "http://localhost:5000/checkout/score/"

def search_for_checkouts():
    """Sends GET request to local Flask servers and updates checkouts list"""
    try:
        response = request.urlopen(f"{CHECKOUT_API_URL}{score_value.get()}")
        data = json.load(response)

        combos = [combo['combo'] for combo in data]
        if combos:
            checkout_list.set(combos)
        else:
            checkout_list.set(['No checkout'])
            
    except tk.TclError as tclerr:
        print(tclerr)

    except error.URLError as urlerr:
        print(urlerr)
        sys.exit(1)
    

def on_checkout_selected(event):
    """Triggered everytime user selects checkout from the checkouts list"""
    w = event.widget
    try:
        value = w.get(w.curselection()[0])
        checkout_text.set(value)
    except IndexError as indexerr:
        print(indexerr)

root = tk.Tk()
root.title('Darts Checkout GUI Application')
root.resizable(0,0)

main_frame = tk.Frame(root, padx=5, pady=5)
main_frame.pack()

upper_frame = tk.Frame(main_frame, padx=3, pady=3)
upper_frame.pack(side='top', fill='x')

score_label = tk.Label(upper_frame, text="Wynik:", padx=3, pady=3)
score_label.pack(side='left')

search_btn = tk.Button(upper_frame, text="Szukaj", takefocus=True, padx=3, pady=3, command=lambda: search_for_checkouts())
search_btn.pack(side='right')

score_value = tk.IntVar()
score_entry = tk.Entry(upper_frame, takefocus=True, textvariable=score_value)
score_entry.pack(fill='x')

checkout_list = tk.StringVar()
checkouts_listbox = tk.Listbox(main_frame, height=5, takefocus=True, listvariable=checkout_list)
checkouts_listbox.pack(side='bottom', fill='x')
checkouts_listbox.bind('<<ListboxSelect>>', on_checkout_selected)

checkout_text = tk.StringVar()
checkout_label = tk.Label(main_frame, textvariable=checkout_text, font=('Courier', '24'))
checkout_label.pack(side='top')

root.mainloop()