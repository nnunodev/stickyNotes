import customtkinter as ctk
import tkinter as tk

app = ctk.CTk()
app.geometry("300x500")
app.title("Sticky")

ctk.set_appearance_mode("dark")  # Set dark mode

text_area = tk.Text(app)
text_area.pack(fill=tk.BOTH, expand=True)
text_area.config(bg="#1f1f1f", fg="white")


# save notes
def save_note():
    notes = text_area.get("1.0", tk.END)
    with open("notes.txt", "w") as file:
        file.write(notes)

#def add_note():

save_button = ctk.CTkButton(app, text="Save", command=save_note)
save_button.pack(pady=10)

add_button = ctk.CTkButton(app, text="+")
add_button.pack(pady=10)
app.mainloop()
