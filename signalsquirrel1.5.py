import tkinter as tk
import base64

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ', ': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-'
}

MORSE_CODE_DICT_REVERSED = {value: key for key, value in MORSE_CODE_DICT.items()}


def text_to_morse(text):
    morse_code = ""
    for char in text.upper():
        if char != " ":
            morse_code += MORSE_CODE_DICT[char] + " "
        else:
            morse_code += " "
    return morse_code.strip()


def morse_to_text(morse_code):
    morse_code += " "
    text = ""
    i = 0
    while i < len(morse_code):
        if morse_code[i] == " ":
            text += " "
        else:
            code = ""
            while morse_code[i] != " ":
                code += morse_code[i]
                i += 1
            text += MORSE_CODE_DICT_REVERSED.get(code, "")
        i += 1
    return text


def text_to_base64(text):
    return base64.b64encode(text.encode("utf-8")).decode("utf-8")


def base64_to_text(base64_text):
    return base64.b64decode(base64_text).decode("utf-8")


def text_to_binary(text):
    binary_code = ""
    for char in text:
        binary_code += "{:08b}".format(ord(char)) + " "
    return binary_code.strip()


def binary_to_text(binary_code):
    text = ""
    binary_list = binary_code.split()
    for binary in binary_list:
        try:
            decimal = int(binary, 2)
            text += chr(decimal)
        except ValueError:
            text += "[Invalid Binary] "
    return text


def convert():
    input_text = text_input.get("1.0", tk.END).strip()
    output_text = ""
    if input_type.get() == "Text":
        output_text = text_to_morse(input_text)
    elif input_type.get() == "Morse Code":
        output_text = morse_to_text(input_text)
    elif input_type.get() == "Base64":
        try:
            output_text = base64_to_text(input_text)
        except:
            try:
                output_text = text_to_base64(input_text)
            except:
                output_text = "Invalid Base64 input"
    elif input_type.get() == "Binary":
        output_text = binary_to_text(input_text)
    output_text_widget.delete("1.0", tk.END)
    output_text_widget.insert("1.0", output_text)
    window.clipboard_clear()
    window.clipboard_append(output_text)


def change_input_type():
    if input_type.get() == "Text":
        input_label.config(text="Input:")
        output_label.config(text="Output:")
    elif input_type.get() == "Base64":
        input_label.config(text="Input (Base64):")
        output_label.config(text="Output (Text):")
    else:
        input_label.config(text="Input:")
        output_label.config(text="Output:")


def clear_fields():
    text_input.delete("1.0", tk.END)
    output_text_widget.delete("1.0", tk.END)


# create the main window
window = tk.Tk()
window.title("Signal Squirrel")

# create input and output widgets
input_type = tk.StringVar(value="Text")
input_label = tk.Label(window, text="Input:", font=("Arial", 14))
text_input = tk.Text(window, height=8, width=50, font=("Arial", 14))
output_label = tk.Label(window, text="Output:", font=("Arial", 14))
convert_button = tk.Button(window, text="Convert", command=convert, font=("Arial", 14))
output_text_widget = tk.Text(window, height=8, width=50, font=("Arial", 14))
copy_button = tk.Button(window, text="Copy to Clipboard", command=lambda: window.clipboard_append(output_text_widget.get("1.0", tk.END)), font=("Arial", 14))
clear_button = tk.Button(window, text="Clear", command=clear_fields, font=("Arial", 14))

# pack the widgets into the window
input_label.pack(pady=10)
text_input.pack(pady=10)
input_type_radio_text = tk.Radiobutton(window, text="Text", variable=input_type, value="Text", font=("Arial", 14), command=change_input_type)
input_type_radio_morse = tk.Radiobutton(window, text="Morse Code", variable=input_type, value="Morse Code", font=("Arial", 14), command=change_input_type)
input_type_radio_base64 = tk.Radiobutton(window, text="Base64", variable=input_type, value="Base64", font=("Arial", 14), command=change_input_type)
input_type_radio_binary = tk.Radiobutton(window, text="Binary", variable=input_type, value="Binary", font=("Arial", 14), command=change_input_type)
input_type_radio_text.pack()
input_type_radio_morse.pack()
input_type_radio_base64.pack()
input_type_radio_binary.pack()
convert_button.pack(pady=10)
output_label.pack(pady=10)
output_text_widget.pack(pady=10)
copy_button.pack(pady=10)
clear_button.pack(pady=10)

# start the main event loop
window.mainloop()


