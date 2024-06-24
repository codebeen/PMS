import customtkinter as ctk

ctk.set_appearance_mode("light")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('800x600')
        self.title("Nested Frames Example")
        
        # Outer frame (main_frame)
        self.main_frame = ctk.CTkFrame(self, width=600, height=400, bg_color="#f0f0f0")
        self.main_frame.pack(padx=20, pady=20)
        
        # Inner frame (sub_frame)
        self.sub_frame = ctk.CTkFrame(self.main_frame, width=400, height=300, bg_color="white")
        self.sub_frame.grid(row=0, column=0, padx=20, pady=20)
        
        # Adding a label inside the inner frame
        self.label = ctk.CTkLabel(self.sub_frame, text="This is inside the inner frame", font=("Arial", 16))
        self.label.pack(padx=20, pady=20)

        # Another frame inside the inner frame
        self.inner_inner_frame = ctk.CTkFrame(self.sub_frame, width=200, height=150, bg_color="#d9d9d9")
        self.inner_inner_frame.pack(padx=20, pady=20)

        # Adding a button inside the inner inner frame
        self.button = ctk.CTkButton(self.inner_inner_frame, text="Click me!", command=self.button_click)
        self.button.pack(padx=10, pady=10)

    def button_click(self):
        print("Button clicked!")

# Run the application
app = App()
app.mainloop()
