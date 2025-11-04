



from endecode import encode, decode
import tkinter as tk
from tkinter import filedialog, messagebox

def browse_input():
    fn = filedialog.askopenfilename(title="Select input file")
    if fn:
        entry_input.delete(0, tk.END)
        entry_input.insert(0, fn)

def browse_output():
    fn = filedialog.asksaveasfilename(title="Select output file", defaultextension="")
    if fn:
        entry_output.delete(0, tk.END)
        entry_output.insert(0, fn)

def do_encode():
    inp = entry_input.get().strip()
    out = entry_output.get().strip()
    if not inp or not out:
        messagebox.showwarning("Missing", "Please provide input and output filenames.")
        return
    try:
        encode(inp, out)
        messagebox.showinfo("Done", f"Encoded:\n{inp}\n→ {out}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def do_decode():
    inp = entry_input.get().strip()
    out = entry_output.get().strip()
    if not inp or not out:
        messagebox.showwarning("Missing", "Please provide input and output filenames.")
        return
    try:
        decode(inp, out)
        messagebox.showinfo("Done", f"Decoded:\n{inp}\n→ {out}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("SENSELESS BY UNUTK4N")

frame = tk.Frame(root, padx=12, pady=12)
frame.pack(fill="both", expand=True)

tk.Label(frame, text="Input file:").grid(row=0, column=0, sticky="w")
entry_input = tk.Entry(frame, width= fifty) if False else tk.Entry(frame, width=50)
entry_input.grid(row=0, column=1, padx=6, pady=6)
tk.Button(frame, text="Browse", command=browse_input).grid(row=0, column=2, padx=4)

tk.Label(frame, text="Output file:").grid(row=1, column=0, sticky="w")
entry_output = tk.Entry(frame, width=50)
entry_output.grid(row=1, column=1, padx=6, pady=6)
tk.Button(frame, text="Browse", command=browse_output).grid(row=1, column=2, padx=4)

btn_frame = tk.Frame(frame)
btn_frame.grid(row=2, column=0, columnspan=3, pady=10)

tk.Button(btn_frame, text="Encode", width=12, command=do_encode).pack(side="left", padx=6)
tk.Button(btn_frame, text="Decode", width=12, command=do_decode).pack(side="left", padx=6)

root.mainloop()
