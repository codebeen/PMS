import customtkinter as ctk
from PIL import Image, ImageTk
from datetime import datetime

def clear_content_frame():
    main_content_frame.clear()

def change_inventory_option(option):
    clear_content_frame()
    inventory_frame = ctk.CTkFrame(main_content_frame, bg='white')
    inventory_frame.place(relx=0.5, rely=0.5, anchor='center')
    if option == "List of Medicine":
        label = ctk.CTkLabel(inventory_frame, text="List of Medicine Page", font=custom_font_dashboard, fg='black', bg='white')
    elif option == "Medicine Category":
        label = ctk.CTkLabel(inventory_frame, text="Medicine Category Page", font=custom_font_dashboard, fg='black', bg='white')
    label.pack(pady=20)

def show_inventory_menu(event):
    inventory_menu.tk_popup(event.x_root, event.y_root)

def on_enter(event):
    event.widget.config(bg='#222B38', font=("", 15))  # Change background color on hover

def on_leave(event):
    event.widget.config(bg=sidebar_menu_colour, font=("", 10))  # Change background color back on leave

def show_dashboard_page():
    clear_content_frame()
    dashboard_frame = ctk.CTkFrame(main_content_frame, bg='white')
    dashboard_frame.place(relx=0.5, rely=0.5, anchor='center')
    label = ctk.CTkLabel(dashboard_frame, text="Dashboard Page", font=custom_font_dashboard, fg='black', bg='white')
    label.pack(pady=20)

def show_inventory_page():
    clear_content_frame()
    inventory_frame = ctk.CTkFrame(main_content_frame, bg='white')
    inventory_frame.place(relx=0.5, rely=0.5, anchor='center')
    label = ctk.CTkLabel(inventory_frame, text="Default Inventory Page", font=custom_font_dashboard, fg='black', bg='white')
    label.pack(pady=20)

def show_report_page():
    clear_content_frame()
    report_frame = ctk.CTkFrame(main_content_frame, bg='white')
    report_frame.place(relx=0.5, rely=0.5, anchor='center')
    label = ctk.CTkLabel(report_frame, text="Report Page", font=custom_font_dashboard, fg='black', bg='white')
    label.pack(pady=20)

def show_cashier_page():
    clear_content_frame()

    pos_label = ctk.CTkLabel(main_content_frame, text="Point of Sale", font=(custom_font_pos), fg='black')
    pos_label.place(x=20, y=80)
    cashier_scndlabel = ctk.CTkLabel(main_content_frame, text="Process payment for purchased medicines.", font=(custom_font_dashboard, 10), fg='black')
    cashier_scndlabel.place(x=20, y=110)

    # Header Frame
    header_frame = ctk.CTkFrame(main_content_frame, bg='white', height=60)
    header_frame.pack(fill=ctk.X, side=ctk.TOP)

    # Greeting icon
    global greeting_icon
    greeting_icon = Image.open('icons8-sun-20.png')
    resized_greeting_icon = greeting_icon.resize((20, 20), Image.LANCZOS)
    greeting_icon = ImageTk.PhotoImage(resized_greeting_icon)

    search_var = ctk.CTkStringVar()
    search_entry = ctk.CTkEntry(header_frame, textvariable=search_var, font=("Poppins", 8), bg='light gray', fg='black', relief='flat')
    search_entry.place(x=40, y=15, width=250, height=30)

    # Placeholder text configuration
    search_entry.insert(0, 'Search for anything here...')
    search_entry.config(fg='gray')  # Initial placeholder text color

    def on_entry_click(event):
        if search_var.get() == 'Search for anything here...':
            search_entry.delete(0, ctk.END)
            search_entry.config(fg='black')

    def on_focusout(event):
        if search_var.get() == '':
            search_entry.insert(0, 'Search for anything here...')
            search_entry.config(fg='gray')

    # Bind events to handle placeholder text behavior
    search_entry.bind('<FocusIn>', on_entry_click)
    search_entry.bind('<FocusOut>', on_focusout)

    # Greeting and Date/Time Frame
    datetime_frame = ctk.CTkFrame(header_frame, bg='white')
    datetime_frame.place(x=870, y=10)

    greeting_label = ctk.CTkLabel(
        datetime_frame, text="Good Day, Cashier!", font=("Poppins", 10),
        fg='black', bg='white', padx=5, image=greeting_icon, compound=ctk.LEFT
    )
    greeting_label.pack(anchor='w')

    date_time_label = ctk.CTkLabel(datetime_frame, text="", font=("Poppins", 10), bg='white', fg='black')
    date_time_label.pack(anchor='w')

    # Function to update date and time
    def update_time():
        current_time = datetime.now().strftime('%d %B %Y · %I:%M:%S %p')
        date_time_label.config(text=current_time)
        root.after(1000, update_time)  # Update every 1 second

    update_time()  # Initial call to start the update loop

    # Cashier Content
    products_frame = ctk.CTkFrame(main_content_frame, bg='white', height=536, highlightbackground='gray', highlightthickness=1)
    products_frame.place(x=20, y=150, width=566, height=536)

    order_frame = ctk.CTkFrame(main_content_frame, bg='white', height=536, highlightbackground='gray', highlightthickness=1)
    order_label = ctk.CTkLabel(order_frame, text='Order', font='Poppins-Black.ttf', fg='black', bg='white')
    order_label.place(x=20, y=10)
    order_frame.place(x=600, y=150, width=460)


root = ctk.CTk()
root.geometry('1280x720')
root.title('Pharmacy Management System')

sidebar_menu_colour = '#222B38'

# Load and resize the icon using PIL
original_icon = Image.open('logo.png')
resized_icon = original_icon.resize((30, 30), Image.LANCZOS)
logo_image = ImageTk.PhotoImage(resized_icon)

# Dashboard icon
original_dashboard_icon = Image.open('icons8-dashboard-50.png')
resized_dashboard_icon = original_dashboard_icon.resize((20, 20), Image.LANCZOS)
dashboard_image = ImageTk.PhotoImage(resized_dashboard_icon)

# Inventory icon
original_inventory_icon = Image.open('icons8-inventory-48.png')
resized_inventory_icon = original_inventory_icon.resize((20, 20), Image.LANCZOS)
inventory_image = ImageTk.PhotoImage(resized_inventory_icon)

# Report icon
original_report_icon = Image.open('icons8-report-50.png')
resized_report_icon = original_report_icon.resize((20, 20), Image.LANCZOS)
report_image = ImageTk.PhotoImage(resized_report_icon)

# Cashier icon
original_cashier_icon = Image.open('icons8-receipt-50.png')
resized_cashier_icon = original_cashier_icon.resize((20, 20), Image.LANCZOS)
cashier_image = ImageTk.PhotoImage(resized_cashier_icon)

# Create the sidebar menu frame with the desired color
sidebar_menu_frame = ctk.CTkFrame(root, bg=sidebar_menu_colour)
sidebar_menu_frame.pack(side=ctk.LEFT, fill=ctk.Y)
sidebar_menu_frame.pack_propagate(False)
sidebar_menu_frame.configure(width=200)

# Create the main content frame
main_content_frame = ctk.CTkFrame(root, bg='#F0F0F0')
main_content_frame.pack(side=ctk.RIGHT, fill=ctk.BOTH, expand=True)

# Load the custom font
custom_font_purehealth = ctk.CTkFont(family="Poppins", size=14, weight="bold")
custom_font_dashboard = ctk.CTkFont(family="Poppins", size=10)
custom_font_pos = ctk.CTkFont(family="Poppins", size=18, weight='bold')

# Add the logo to the sidebar frame
logo_menu_label = ctk.CTkLabel(
    sidebar_menu_frame, image=logo_image, bg=sidebar_menu_colour, borderwidth=0,
    activebackground=sidebar_menu_colour, text='PureHealth', font=custom_font_purehealth,
    compound=ctk.LEFT, padx=10, fg='white'
)
logo_menu_label.place(x=16, y=20)

# Add the dashboard menu button
dashboard_menu_btn = ctk.CTkButton(
    sidebar_menu_frame, image=dashboard_image, text='Dashboard',
    font=custom_font_dashboard, fg='white', bg=sidebar_menu_colour, corner_radius=0,
    compound=ctk.LEFT, padx=10,
    command=show_dashboard_page
)
dashboard_menu_btn.place(x=20, y=230)

# Add hover effect to dashboard button around the text area
dashboard_menu_btn.bind("<Enter>", lambda event: on_enter(event))
dashboard_menu_btn.bind("<Leave>", lambda event: on_leave(event))

# Dropdown options for inventory
inventory_options = ["List of Medicine", "Medicine Category"]

# Create a Menu widget for custom dropdown
inventory_menu = tk.Menu(sidebar_menu_frame, bg=sidebar_menu_colour, fg='white', borderwidth=0,
                        activebackground=sidebar_menu_colour, font=custom_font_dashboard)

# Add options to the custom dropdown menu
for option in inventory_options:
    inventory_menu.add_command(label=option, command=lambda opt=option: change_inventory_option(opt))

# Button to show the inventory menu
inventory_button = tk.Button(
    sidebar_menu_frame, image=inventory_icon, text='Inventory',
    font=custom_font_dashboard, fg='white', bg=sidebar_menu_colour, borderwidth=0,
    activebackground=sidebar_menu_colour, compound=tk.LEFT, padx=10,
    command=show_inventory_page
)
inventory_button.place(x=20, y=300)
inventory_button.bind("<Button-3>", show_inventory_menu)  # Right-click to show dropdown menu

# Add hover effect to inventory button around the text area
inventory_button.bind("<Enter>", lambda event: on_enter(event))
inventory_button.bind("<Leave>", lambda event: on_leave(event))

# Add the sales report button
report_button = tk.Button(
    sidebar_menu_frame, image=report_icon, text='Report',
    font=custom_font_dashboard, fg='white', bg=sidebar_menu_colour, borderwidth=0,
    activebackground=sidebar_menu_colour, compound=tk.LEFT, padx=10,
    command=show_report_page
)
report_button.place(x=20, y=370)

# Add hover effect to report button around the text area
report_button.bind("<Enter>", lambda event: on_enter(event))
report_button.bind("<Leave>", lambda event: on_leave(event))

# Add the cashier button
cashier_button = tk.Button(
    sidebar_menu_frame, image=cashier_icon, text='Cashier',
    font=custom_font_dashboard, fg='white', bg=sidebar_menu_colour, borderwidth=0,
    activebackground=sidebar_menu_colour, compound=tk.LEFT, padx=10,
    command=show_cashier_page
)
cashier_button.place(x=20, y=430)

# Add hover effect to cashier button around the text area
cashier_button.bind("<Enter>", lambda event: on_enter(event))
cashier_button.bind("<Leave>", lambda event: on_leave(event))


root.mainloop()
