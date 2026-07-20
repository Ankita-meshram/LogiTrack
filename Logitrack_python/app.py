import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("LogiTrack Project")
root.geometry("1200x250")
root.configure(bg="#edf2ff")

style = ttk.Style()
style.theme_use("clam")

# Header Style
style.configure(
    "Treeview.Heading",
    background="#5b3df5",
    foreground="white",
    font=("Segoe UI", 11, "bold"),
    relief="flat"
)

# Table Style
style.configure(
    "Treeview",
    font=("Segoe UI", 10),
    rowheight=60,
    background="white",
    fieldbackground="white",
    borderwidth=0
)

columns = (
    "Roll No",
    "Project Name",
    "Subtitle",
    "Domain",
    "U1 - Fundamentals"
)

tree = ttk.Treeview(root, columns=columns, show="headings", height=1)

# Headings
for col in columns:
    tree.heading(col, text=col)

tree.column("Roll No", width=80, anchor="center")
tree.column("Project Name", width=180, anchor="center")
tree.column("Subtitle", width=320, anchor="w")
tree.column("Domain", width=150, anchor="center")
tree.column("U1 - Fundamentals", width=450, anchor="w")

tree.insert(
    "",
    "end",
    values=(
        "36",
        "🚚 LogiTrack",
        "Parcel tracking & delivery\nstatus notification system",
        "📦 Logistics",
        "• Lists for status stages\n• Dicts for parcel data\n• Conditionals for next-stage logic"
    )
)

tree.pack(padx=20, pady=30)

root.mainloop()