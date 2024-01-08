import tkinter as tk

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
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
                   '0': '-----', ',': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', ' ': '/ '}


def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
        else:
            morse_code += ' '
    return morse_code


def morse_to_text(morse_code):
    text = ''
    morse_code_split = morse_code.split(' ')
    for code in morse_code_split:
        if code == '/':
            text += ' '
        else:
            for key, value in MORSE_CODE_DICT.items():
                if code == value:
                    text += key
    return text


def on_submit():
    input_text = entry.get()
    if mode.get() == "encode":
        result_label.config(text=f"Morse Code: {text_to_morse(input_text)}")
    elif mode.get() == "decode":
        result_label.config(text=f"Text: {morse_to_text(input_text)}")


root = tk.Tk()
root.title("Morse Code Converter")

label = tk.Label(root, text="Enter text or Morse Code:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

mode = tk.StringVar()
encode_radio = tk.Radiobutton(root, text="Encode to Morse Code", variable=mode, value="encode")
encode_radio.pack(pady=5)
decode_radio = tk.Radiobutton(root, text="Decode from Morse Code", variable=mode, value="decode")
decode_radio.pack(pady=5)
mode.set("encode")

submit_button = tk.Button(root, text="Process", command=on_submit)
submit_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 20))
result_label.pack(pady=10)

root.mainloop()
