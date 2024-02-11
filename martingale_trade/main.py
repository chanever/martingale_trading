import tkinter as tk
from ui_components import setup_ui, refresh_price

def main():
    root = tk.Tk()
    coin_selector_frame, coin_var, price_display_frame, price_var, entry_fields_frame, entry_price_var, amount_var, buttons_frame, long_button, short_button, martingale_display_frame, martingale_info_var = setup_ui(root)
    
    # Start the price refresh loop
    refresh_price(coin_var, price_var, root)

    root.mainloop()

if __name__ == "__main__":
    main()
