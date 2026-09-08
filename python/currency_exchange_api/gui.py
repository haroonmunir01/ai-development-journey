import tkinter as tk

from main import currencies, currency_converter


def convert_currency():
    amount = amount_entry.get()

    from_currency_value = from_currency.get()
    to_currency_value = to_currency.get()

    if not amount:
        result_label.config(text="Please enter an amount.")
        return

    try:
        amount = float(amount)
    except ValueError:
        result_label.config(text="Please enter a valid number.")
        return

    if amount <= 0:
        result_label.config(text="Amount must be greater than 0.")
        return

    if from_currency_value == to_currency_value:
        result_label.config(
            text="From and To currencies must be different."
        )
        return

    result = currency_converter(
        from_currency_value,
        to_currency_value
    )

    if isinstance(result, dict) and "error" in result:
        result_label.config(text=result["error"])
        return

    final_value = amount * result

    result_label.config(
        text=f"{amount:g} {from_currency_value} = "
             f"{final_value:.2f} {to_currency_value}"
    )


window = tk.Tk()

window.title("Currency Converter")
window.geometry("500x400")


title_label = tk.Label(
    window,
    text="Currency Converter",
    font=("Arial", 15, "bold")
)

title_label.grid(row=0, column=0, columnspan=2)


amount_label = tk.Label(
    window,
    text="Amount:"
)

amount_label.grid(row=1, column=0)


amount_entry = tk.Entry(window)

amount_entry.grid(row=1, column=1)


currency_list = currencies()


from_currency = tk.StringVar()
from_currency.set("USD")


from_label = tk.Label(
    window,
    text="From:"
)

from_label.grid(row=2, column=0)


from_currency_menu = tk.OptionMenu(
    window,
    from_currency,
    *currency_list
)

from_currency_menu.grid(row=2, column=1)


to_label = tk.Label(
    window,
    text="To:"
)

to_label.grid(row=3, column=0)


to_currency = tk.StringVar()
to_currency.set("PKR")


to_currency_menu = tk.OptionMenu(
    window,
    to_currency,
    *currency_list
)

to_currency_menu.grid(row=3, column=1)


convert_button = tk.Button(
    window,
    text="Convert",
    command=convert_currency
)

convert_button.grid(row=4, column=1)


result_label = tk.Label(
    window,
    text=""
)

result_label.grid(
    row=5,
    column=0,
    columnspan=2
)


window.mainloop()