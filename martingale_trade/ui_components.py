import tkinter as tk
from api_manager import get_sorted_coin_list, get_current_price
from trading_logic import calculate_martingale

def setup_ui(root):
    # Price display setup
    price_display_frame, price_var = create_price_display(root)
    price_display_frame.pack()

    # Coin selector setup with callback for updating the price
    coin_selector_frame, coin_var = create_coin_selector(root, lambda: refresh_price(coin_var, price_var, root))
    coin_selector_frame.pack()

    # Entry fields for entry price and amount setup
    entry_fields_frame, entry_price_var, amount_var = create_entry_fields(root)
    entry_fields_frame.pack()

    # Martingale display setup
    martingale_display_frame, martingale_info_var = create_martingale_display(root)
    martingale_display_frame.pack()

    # Position buttons setup with martingale calculation
    buttons_frame, long_button, short_button = create_position_buttons(root, entry_price_var, amount_var, martingale_info_var)
    buttons_frame.pack()

    # Initialize price display
    refresh_price(coin_var, price_var, root)

    return coin_selector_frame, coin_var, price_display_frame, price_var, entry_fields_frame, entry_price_var, amount_var, buttons_frame, long_button, short_button, martingale_display_frame, martingale_info_var

def create_coin_selector(root, update_price_callback):
    frame = tk.Frame(root)
    label = tk.Label(frame, text="Select Coin:")
    label.pack(side=tk.LEFT)

    coin_var = tk.StringVar(frame)
    coin_list = get_sorted_coin_list()
    coin_selector = tk.OptionMenu(frame, coin_var, *coin_list, command=lambda selection: update_price_callback())
    coin_selector.pack(side=tk.RIGHT)

    return frame, coin_var

def create_price_display(root):
    frame = tk.Frame(root)
    price_var = tk.StringVar(frame, value="Price will be displayed here")
    price_label = tk.Label(frame, textvariable=price_var)
    price_label.pack()

    return frame, price_var

def create_entry_fields(root):
    frame = tk.Frame(root)

    entry_price_frame = tk.Frame(frame)
    tk.Label(entry_price_frame, text="Entry Price ($) :").pack(side=tk.TOP)
    entry_price_var = tk.Entry(entry_price_frame)
    entry_price_var.pack(side=tk.TOP)
    entry_price_frame.pack(side=tk.TOP, fill=tk.X)

    amount_frame = tk.Frame(frame)
    tk.Label(amount_frame, text="Amount ($):").pack(side=tk.TOP)
    amount_var = tk.Entry(amount_frame)
    amount_var.pack(side=tk.TOP)
    amount_frame.pack(side=tk.TOP, fill=tk.X)

    return frame, entry_price_var, amount_var

def create_position_buttons(root, entry_price_var, amount_var, martingale_info_var):
    frame = tk.Frame(root)
    long_button = tk.Button(frame, text="Long", command=lambda: show_martingale_info(entry_price_var, amount_var, martingale_info_var, False))
    long_button.pack(side=tk.LEFT, padx=5)
    short_button = tk.Button(frame, text="Short", command=lambda: show_martingale_info(entry_price_var, amount_var, martingale_info_var, True))
    short_button.pack(side=tk.RIGHT, padx=5)

    return frame, long_button, short_button

def create_martingale_display(root):
    frame = tk.Frame(root)
    martingale_info_var = tk.StringVar(frame, value="Martingale info will be displayed here")
    martingale_info_label = tk.Label(frame, textvariable=martingale_info_var)
    martingale_info_label.pack()

    return frame, martingale_info_var

def show_martingale_info(entry_price_var, amount_var, info_var, is_short):
    try:
        entry_price = float(entry_price_var.get())
        amount = float(amount_var.get())
        
        martingale_info = calculate_martingale(entry_price, amount, is_short)
        info_var.set(martingale_info)
    except ValueError:
        info_var.set("Please enter valid numbers for entry price and amount.")
def refresh_price(coin_var, price_var, root):
    symbol = coin_var.get()
    price = get_current_price(symbol)
    price_var.set(f"Current price: {price} $")
    root.after(5000, lambda: refresh_price(coin_var, price_var, root))
