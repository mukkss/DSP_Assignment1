import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from colorama import init as colorama_init
from caesar.cipher import encrypt, decrypt, validate_ascii_text
from caesar.file_handler import read_text_file, write_text_file
from caesar.ui_utils import ask_open_file, ask_save_file, show_error, show_info

# Initialize colorama for console logs (if needed)
colorama_init(autoreset=True)

APP_TITLE = "Caesar Cipher — Stylish GUI"
WINDOW_SIZE = "760x520"


class CaesarApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(APP_TITLE)
        self.geometry(WINDOW_SIZE)
        self.resizable(False, False)
        self._create_widgets()

    def _create_widgets(self):
        # Top frame: title
        title_frame = ttk.Frame(self, padding=(12, 10))
        title_frame.pack(fill=tk.X)

        title_label = ttk.Label(title_frame, text=APP_TITLE, font=("Segoe UI", 16, "bold"))
        title_label.pack(side=tk.LEFT)

        # Middle frame: inputs and controls
        mid = ttk.Frame(self, padding=(12, 8))
        mid.pack(fill=tk.BOTH, expand=True)

        # Left: input text
        left = ttk.Frame(mid)
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        ttk.Label(left, text="Input:").pack(anchor=tk.W)
        self.input_text = scrolledtext.ScrolledText(left, width=40,height=8, wrap=tk.WORD)
        self.input_text.pack(fill=tk.BOTH, expand=True, padx=(0, 8), pady=(4, 10))

        # Right: output text
        right = ttk.Frame(mid)
        right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        ttk.Label(right, text="Output:").pack(anchor=tk.W)
        self.output_text = scrolledtext.ScrolledText(
            right,
            width=50,
            height=8,
            wrap=tk.WORD,
            bg="#f7faff",  # light hint background
            font=("Segoe UI", 10),
            state=tk.DISABLED  # start read-only
        )
        self.output_text.pack(fill=tk.BOTH, expand=True, padx=(8, 0), pady=(4, 10))

        # Controls
        ctrl = ttk.Frame(self, padding=(12, 6))
        ctrl.pack(fill=tk.X)

        ttk.Label(ctrl, text="Shift (0-25):").pack(side=tk.LEFT)
        self.shift_var = tk.IntVar(value=3)
        self.shift_spin = ttk.Spinbox(ctrl, from_=0, to=25, width=5, textvariable=self.shift_var)
        self.shift_spin.pack(side=tk.LEFT, padx=(6, 12))

        self.mode_var = tk.StringVar(value="encrypt")
        encrypt_radio = ttk.Radiobutton(ctrl, text="Encrypt", variable=self.mode_var, value="encrypt")
        decrypt_radio = ttk.Radiobutton(ctrl, text="Decrypt", variable=self.mode_var, value="decrypt")
        encrypt_radio.pack(side=tk.LEFT)
        decrypt_radio.pack(side=tk.LEFT, padx=(6, 12))

        run_btn = ttk.Button(ctrl, text="Run", command=self.on_run)
        run_btn.pack(side=tk.LEFT, padx=(6, 6))

        copy_btn = ttk.Button(ctrl, text="Copy Output", command=self.copy_output)
        copy_btn.pack(side=tk.LEFT)

        ttk.Separator(self, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=8)

        # File action buttons
        file_frame = ttk.Frame(self, padding=(12, 6))
        file_frame.pack(fill=tk.X)

        load_in_btn = ttk.Button(file_frame, text="Load Input File", command=self.load_input_file)
        load_in_btn.pack(side=tk.LEFT)

        save_out_btn = ttk.Button(file_frame, text="Save Output File", command=self.save_output_file)
        save_out_btn.pack(side=tk.LEFT, padx=(8, 0))

        clear_btn = ttk.Button(file_frame, text="Clear", command=self.clear_all)
        clear_btn.pack(side=tk.RIGHT)

    def on_run(self):
        text = self.input_text.get("1.0", tk.END).rstrip("\n")
        if text.strip() == "":
            show_error(self, "Input required", "Please enter or load text to transform.")
            return

        try:
            validate_ascii_text(text)
        except ValueError as exc:
            show_error(self, "Invalid text", str(exc))
            return

        shift = int(self.shift_var.get())
        mode = self.mode_var.get()

        try:
            if mode == "encrypt":
                out = encrypt(text, shift)
            else:
                out = decrypt(text, shift)
        except Exception as exc:
            show_error(self, "Error", str(exc))
            return

        # ✅ Enable temporarily to update
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, out)
        # ✅ Lock it again
        self.output_text.config(state=tk.DISABLED)


    def copy_output(self):
        out = self.output_text.get("1.0", tk.END)
        self.clipboard_clear()
        self.clipboard_append(out)
        show_info(self, "Copied", "Output copied to clipboard.")

    def load_input_file(self):
        path = ask_open_file(self)
        if not path:
            return
        try:
            text = read_text_file(path)
        except Exception as exc:
            show_error(self, "File error", str(exc))
            return
        self.input_text.delete("1.0", tk.END)
        self.input_text.insert(tk.END, text)

    def save_output_file(self):
        suggested = "output.txt"
        path = ask_save_file(self, suggested_name=suggested)
        if not path:
            return
        out = self.output_text.get("1.0", tk.END)
        try:
            write_text_file(path, out)
        except Exception as exc:
            show_error(self, "Save error", str(exc))
            return
        show_info(self, "Saved", f"Output saved to {path}")

    def clear_all(self):
        self.input_text.delete("1.0", tk.END)
        self.output_text.delete("1.0", tk.END)


def main():
    app = CaesarApp()
    app.mainloop()


if __name__ == "__main__":
    main()