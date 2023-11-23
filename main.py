import tkinter as tk
from googletrans import Translator


def translate_text():
    source_text = source_text_entry.get()
    target_language = target_language_entry.get()

    try:
        translator = Translator()
        translated = translator.translate(source_text, dest=target_language)
        translated_text.set(translated.text)
    except ValueError as e:
        translated_text.set("Error: " + str(e))


def exit_program(event):
    root.quit()


root = tk.Tk()
root.title("Text Translator")

source_text_label = tk.Label(root, text="Enter the text to translate:")
source_text_label.pack()

source_text_entry = tk.Entry(root, width=40)
source_text_entry.pack()

target_language_label = tk.Label(
    root, text="Enter the target language (e.g., 'fr' for French):")
target_language_label.pack()

target_language_entry = tk.Entry(root, width=5)
target_language_entry.pack()

translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack()

translated_text = tk.StringVar()
translated_text_label = tk.Label(
    root, textvariable=translated_text, wraplength=300)
translated_text_label.pack()

root.bind('<Escape>', exit_program)  # Bind 'Esc' key to exit the program

root.mainloop()
