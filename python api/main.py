"""from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/armstrong/<int:n>')    
def armstrong(n):    
    sum = 0
    order = len(str(n))
    copy_n = n
    while(n>0):
        digit = n%10
        sum += digit**order
        n = n//10

    if(sum == copy_n):    
        print(f"{copy_n} is an Armstrong number")
        result = {
            "Number": copy_n,
            "Armstrong": True,
            "Server IP": "122.234.213.45"
        }
    else:    
        print(f"{copy_n} is not an Armstrong number")
        result = {
            "Number": copy_n,
            "Armstrong": False,
            "Server IP": "122.234.213.45"
        }

    return jsonify(result)

if __name__ == "__main__":    
    app.run(debug="True")

import tkinter as tk

def buy_clothing():
    selected_item = clothing_listbox.get(tk.ACTIVE)
    confirm_label.config(text=f"You have purchased: {selected_item}")

# संवाद बनाएं
root = tk.Tk()
root.title("Clothing Store")

# उपयोगकर्ता इंटरफेस तत्व बनाएं
clothing_label = tk.Label(root, text="Choose a clothing item:")
clothing_label.pack()

clothing_list = ["Shirt", "Pants", "Dress", "Jacket"]
clothing_listbox = tk.Listbox(root)
for item in clothing_list:
    clothing_listbox.insert(tk.END, item)
clothing_listbox.pack()

buy_button = tk.Button(root, text="Buy", command=buy_clothing)
buy_button.pack()

confirm_label = tk.Label(root, text="")
confirm_label.pack()

# इंटरफेस को रन करें
root.mainloop()"""
