import customtkinter as ctk
from PIL import Image
from datetime import datetime

# Initialize customtkinter and set appearance mode
ctk.set_appearance_mode("light")

# PIL PICTURES
logo_image = ctk.CTkImage(Image.open("logo.png"))
dashboard_image = ctk.CTkImage(Image.open("icons8-dashboard-50.png"))
inventory_image = ctk.CTkImage(Image.open("icons8-inventory-48.png"))
sales_image = ctk.CTkImage(Image.open("icons8-report-50.png"))
cashier_Image = ctk.CTkImage(Image.open("icons8-receipt-50.png"))
profile_image = ctk.CTkImage(Image.open("icons8-test-account-50.png"))
search_image = ctk.CTkImage(Image.open("icons8-search-25.png"))

class SidebarMenu(ctk.CTkFrame):
    def __init__(self, master, width, header_font, regular_font, lower_font, **kwargs):
        super().__init__(master, width=width, **kwargs)
        
        # Initialize attributes
        self.master = master
        self.header_font = header_font
        self.regular_font = regular_font
        self.lower_font = lower_font

        # Configure grid layout to allow for flexible placement
        self.grid_rowconfigure(14, weight=1)  # Add a flexible spacer row
        
        # Add upper frame at the top
        self.upperframe = ctk.CTkFrame(self, width=256, height=80, fg_color='#1D242E', corner_radius=0)
        self.upperframe.grid(row=0, column=0, sticky="new")
        
        # Create a title label for the sidebar
        self.title_label = ctk.CTkLabel(self.upperframe, text="PureHealth", font=header_font, text_color='white',
                                        corner_radius=0, fg_color='#1D242E', image=logo_image, compound='left', padx=10, anchor='center')
        self.title_label.grid(row=0, column=0, padx=60, pady=15)
        
        # Create buttons for the sidebar menu
        self.dashboard = ctk.CTkButton(self, text="Dashboard", command=self.master.show_dashboard_page, 
                                       width=256, height=46, corner_radius=0, fg_color='#283342',
                                       font=regular_font, image=dashboard_image, compound='left', anchor='w')
        self.dashboard.grid(row=3, column=0, padx=20, pady=(70, 5), sticky="ew")
        
        self.inventory = ctk.CTkButton(self, text="Inventory", command=self.master.show_inventory_page,
                                       width=256, height=46, corner_radius=0, fg_color='#283342', 
                                       font=regular_font, image=inventory_image, compound='left', anchor='w')
        self.inventory.grid(row=5, column=0, padx=20, pady=5, sticky="ew")
        
        self.sales = ctk.CTkButton(self, text="Sales Report", command=self.master.show_report_page, width=256, height=46,
                                   corner_radius=0, fg_color='#283342', font=regular_font, image=sales_image, compound='left', anchor='w')
        self.sales.grid(row=6, column=0, padx=20, pady=5, sticky="ew")

        self.cashier = ctk.CTkButton(self, text="Cashier", command=self.master.show_cashier_page, width=256, height=46,
                                     corner_radius=0, fg_color='#283342', font=regular_font, image=cashier_Image, compound='left', anchor='w')
        self.cashier.grid(row=7, column=0, padx=20, pady=5, sticky="ew")

        # Add lower frame at the bottom
        self.lowerframe = ctk.CTkFrame(self, width=256, height=10, fg_color='#1D242E', corner_radius=0)
        self.lowerframe.grid(row=15, column=0, sticky="sew")
        
        self.lower_label = ctk.CTkLabel(self.lowerframe, text="Girlypop ft. Darben  v 1.1.2", font=lower_font, text_color='white',
                                        corner_radius=0, fg_color='#1D242E', padx=10)
        self.lower_label.grid(row=0, column=0, padx=50, sticky="sew")


class MainFrame(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('1280x720')
        self.title("Pharmacy Management System")
        
        # Initialize fonts after creating the main window
        self.initialize_fonts()

        # Configure grid layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=0)  # Column 0 fixed width for sidebar
        self.grid_columnconfigure(1, weight=1)  # Column 1 will expand to fill the window
        
        # Create and place the sidebar menu
        self.sidebar_menu = SidebarMenu(master=self, width=256, header_font=self.header_font, regular_font=self.regular_font,
                                        lower_font=self.lower_font, fg_color="#283342", corner_radius=0)
        self.sidebar_menu.grid(row=0, column=0, sticky="nsew")
        
        # Create and place a main content area
        self.main_content = ctk.CTkFrame(self, corner_radius=0)  # Optional: Set corner_radius to 0 for a flat look
        self.main_content.grid(row=0, column=1, sticky="nsew")
        
        # Create a header frame in the main content area
        self.header_mainframe = ctk.CTkFrame(self.main_content, fg_color='white', corner_radius=0, width=2000, height=60)
        self.header_mainframe.pack(fill=ctk.X, side=ctk.TOP)
        
        # Create a search bar in the header frame
        self.searchbar_frame = ctk.CTkFrame(self.header_mainframe, fg_color='white', 
                                            corner_radius=5)
        self.searchbar_frame.place(x=80, y=10, anchor="nw")
        
        # Add the search icon label
        self.search_icon_label = ctk.CTkLabel(self.searchbar_frame, image=search_image, text="", corner_radius=0)
        self.search_icon_label.grid(row=0, column=0, padx=(5, 0))
        
        # Add the search entry
        self.searchbar = ctk.CTkEntry(self.searchbar_frame, width=260, height=38, corner_radius=5, placeholder_text="Search anything here")
        self.searchbar.grid(row=0, column=1, padx=(0, 20), pady=0, sticky="ew")

        # Create the first "Good Day!" label
        self.header_label_1 = ctk.CTkLabel(self.header_mainframe, text="Good Day!", fg_color='white', text_color='black', font=self.regular_font)
        self.header_label_1.place(x=800, y=5)
        
        # Create the date and time label
        self.date_time_label = ctk.CTkLabel(self.header_mainframe, text="", font=self.lower_font, fg_color='white', text_color='black')
        self.date_time_label.place(x=800, y=25)
        
        # Update date and time function
        def update_time():
            current_time = datetime.now().strftime('%d %B %Y · %I:%M:%S %p')
            self.date_time_label.configure(text=current_time)
            self.date_time_label.after(1000, update_time)  # Update every 1 second
        
        update_time()  # Initial call to start updating
        
        # Center the main window on the screen
        self.center_window()

        # Create a main content frame
        self.main_content_frame = ctk.CTkFrame(self.main_content, corner_radius=0)
        self.main_content_frame.pack(fill=ctk.BOTH, expand=True)

        # Initialize pages
        self.pages = {
            'dashboard': self.show_dashboard_page,
            'inventory': self.show_inventory_page,
            'sales': self.show_report_page,
            'cashier': self.show_cashier_page
        }
        
        self.show_dashboard_page()  # Show dashboard page initially
        
    # Initialize header, regular, and lower fonts
    def initialize_fonts(self):
        self.header_font = ctk.CTkFont(family="Century Gothic", size=19, weight='bold', underline=False)
        self.regular_font = ctk.CTkFont(family="Century Gothic", size=14, weight="normal")
        self.lower_font = ctk.CTkFont(family="Century Gothic", size=10, weight="normal")
        
    def center_window(self):
        # Center the main window on the screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - 1280) // 2  # Calculate position x
        y = (screen_height - 720) // 4  # Calculate position y
        self.geometry(f'1280x720+{x}+{y}')  # Set the dimensions and position of the window

    def on_focus_out(self, event):
        # Reset search bar to placeholder text when focus is lost
        if event.widget == self.searchbar and not self.searchbar.get().strip():
            self.searchbar.delete(0, "end")
            self.searchbar.insert(0, "Search anything here")

    def clear_content_frame(self):
        # Clear the current content frame
        for widget in self.main_content_frame.winfo_children():
            widget.destroy()

    def show_dashboard_page(self):
        self.clear_content_frame()
        dashboard_frame = ctk.CTkFrame(self.main_content_frame, fg_color='white')
        dashboard_frame.place(x=20,y=20)
        label = ctk.CTkLabel(dashboard_frame, text="Dashboard Page", font=self.regular_font, fg_color='white', text_color='black')
        label.pack(pady=20)

    def show_inventory_page(self):
        self.clear_content_frame()
        inventory_frame = ctk.CTkFrame(self.main_content_frame, fg_color='white')
        inventory_frame.place(x=25, y=25)
        label = ctk.CTkLabel(inventory_frame, text="Default Inventory Page", font=self.regular_font, fg_color='white', text_color='black')
        label.pack(pady=20)

    def show_report_page(self):
        self.clear_content_frame()
        report_frame = ctk.CTkFrame(self.main_content_frame, fg_color='white')
        report_frame.place(x=25,y=25)
        label = ctk.CTkLabel(report_frame, text="Report Page", font=self.regular_font, fg_color='white', text_color='black')
        label.pack(pady=20)

    def show_cashier_page(self):
        self.clear_content_frame()
        pos_label = ctk.CTkLabel(self.main_content_frame, text="Point of Sale", font=self.regular_font, fg_color='white')
        pos_label.place(x=20, y=80)
        cashier_scndlabel = ctk.CTkLabel(self.main_content_frame, text="Process payment for purchased medicines.", font=(self.regular_font, 10), fg_color='white')
        cashier_scndlabel.place(x=20, y=110)

    def show_frame(self, frame_name):
        self.pages[frame_name]()


# Run the application
if __name__ == "__main__":
    app = MainFrame()
    app.mainloop()
