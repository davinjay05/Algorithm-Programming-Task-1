import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime, timedelta
# mapping an airline using dictionaries.
airline_mapping = {
    "BG": "Biman Bangladesh Airlines",
    "SQ": "Singapore Airlines",
    "GA": "Garuda Indonesia",
    "ID": "Batik Air",
    "CI": "China Airlines",
    "NZ": "Air New Zealand",
    "VN": "Vietnam Airlines",
    "NH": "All Nippon Airways",
    "BA": "British Airways",
    "KE": "Korean Air",
    "AF": "Air France",
    "TR": "Scoot",
    "8M": "Myanmar Airways",
    "FD": "Thai AirAsia",
    "AK": "AirAsia",
    "QZ": "Indonesia AirAsia",
    "IX": "Air India Express",
    "SL": "Thai Lion Air",
    "UA": "United Airlines",
    "AI": "Air India",
    "QR": "Qatar Airways",
    "EY" : "Etihad",
    "EK" : "Emirates",
    "QG": "Citilink",
    }

# Example flight data by using dictionaries.
departure_flight_data = [
    {"Flight Number": "UA 2", "Destination": "San Francisco", "Gate": "F42", "Departure Time": "10:15", "Status": "Will be Updated Soon", "Type": "Departure"},
    {"Flight Number": "QZ 659", "Destination": "Yogyakarta", "Gate": "G4", "Departure Time": "11:15", "Status": "Will be Updated Soon", "Type": "Departure"},
    {"Flight Number": "QZ 505", "Destination": "Bali", "Gate": "G6", "Departure Time": "12:15", "Status": "Will be Updated Soon", "Type": "Departure"},
    {"Flight Number": "BG 585", "Destination":"Dhaka", "Gate": "A10", "Departure Time": "16:15", "Status": "Will be Updated Soon", "" "Type": "Departure"},
    {"Flight Number": "GA 833", "Destination": "Jakarta", "Gate": "B1", "Departure Time": "16:30", "Status": "Will be Updated Soon","Type": "Departure"},
    {"Flight Number": "SQ 406", "Destination":"New Delhi", "Gate": "A7", "Departure Time": "16:45", "Status": "Will be Updated Soon","Type": "Departure"},
    {"Flight Number": "ID 7134", "Destination":"Denpasar", "Gate": "C13", "Departure Time": "16:45", "Status": "Will be Updated Soon", "Type": "Departure"},
    {"Flight Number": "SQ 836", "Destination": "Shanghai (上海) ", "Gate": "F9", "Departure Time": "17:05", "Status": "Will be Updated Soon", "Type": "Departure"},
    {"Flight Number": "ID 7150", "Destination": "Jakarta", "Gate": "A4", "Departure Time": "17:05", "Status": "Will be Updated Soon", "Type": "Departure"},
    {"Flight Number": "SQ 215", "Destination": "Perth", "Gate": "F9", "Departure Time": "17:05", "Status": "Will be Updated Soon", "Type": "Departure"},
    {"Flight Number": "CI 758", "Destination": "Taipei", "Gate":"B3", "Departure Time":"18:10", "Status": "Will be Updated Soon", "Type": "Departure"},
    {"Flight Number": "VN 654", "Destination": "Ho Chi Minh City", "Gate": "D20", "Departure Time": "18:25", "Status": "Will be Updated Soon", "Type": "Departure"},
    {"Flight Number": "NZ 283", "Destination": "Auckland", "Gate": "C19", "Departure Time": "18:30", "Status": "Will be Updated Soon", "Type": "Departure"},
    {"Flight Number": "SQ 215", "Destination": "Perth", "Gate": "D14", "Departure Time": "18:40", "Status": "Will be Updated Soon", "Type": "Departure"},
    {"Flight Number": "SQ 261", "Destination": "Sydney", "Gate": "D32", "Departure Time": "17:05", "Status": "Will be Updated Soon", "Type": "Departure"},
    {"Flight Number": "SQ 247", "Destination": "Melbourne", "Gate":"D20", "Departure Time": "19:20", "Status": "Will be Updated Soon", "Type": "Departure"},
    {"Flight Number": "SQ 898", "Destination": "Hong Kong（香港）", "Gate": "F12", "Departure Time": "18:55", "Status": "Will be Updated Soon", "Type": "Departure"},
    {"Flight Number": "GA 855", "Destination": "Surabaya", "Gate": "A1", "Departure Time": "19:00", "Status": "Will be Updated Soon", "Type": "Departure"},
    {"Flight Number": "EY 497", "Destination": "Abu Dhabi", "Gate": "F40", "Departure Time": "19:25", "Status": "Will be Updated Soon.", "Type": "Departure"},
    {"Flight Number": "GA 837", "Destination": "Jakarta", "Gate": "A2", "Departure Time": "19:30", "Status": "Will be Updated Soon", "Type": "Departure"},
    {"Flight Number": "SQ 297", "Destination": "Christchurch", "Gate": "C17", "Departure Time": "19:50", "Status": "Will be Updated Soon", "Type": "Departure"},
    {"Flight Number": "SQ 34",  "Destination": "San Francisco", "Gate":"D37", "Departure Time": "19:55", "Status": "Will be Updated Soon", "Type": "Departure"},
    {"Flight Number": "8M 5309", "Destination": "Colombo", "Gate": "A6", "Departure Time": "19:55", "Status": "Will be Updated Soon", "Type": "Departure"},
    {"Flight Number": "QG 527", "Destination": "Jakarta", "Gate": "A12", "Departure Time": "20:30", "Status": "Will be Updated Soon","Type": "Departure"},
    {"Flight Number": "SQ 221", "Destination": "Sydney", "Gate": "D35", "Departure Time": "20:40", "Status": "Will be Updated Soon", "Type": "Departure"},
    {"Flight Number": "SQ 38", "Destination": "Los Angeles", "Gate":"D20", "Departure Time": "20:45", "Status": "Will be Updated Soon", "Type": "Departure"},
    {"Flight Number": "ID 7158", "Destination": "Jakarta", "Gate": "A3", "Departure Time": "22:05", "Status": "Will be Updated Soon","Type": "Departure"},
    {"Flight Number": "AK 1726", "Destination": "Penang", "Gate": "G7", "Departure Time": "22:10", "Status": "Will be Updated Soon", "Type": "Departure"},
    {"Flight Number": "FD 352", "Destination": "Bangkok-DMK", "Gate": "G10", "Departure Time": "22:10", "Status": "Will be Updated Soon", "Type": "Departure"},
    {"Flight Number": "NH 844", "Destination": "Tokyo-HND", "Gate": "D41", "Departure Time": "22:10", "Status": "Will be Updated Soon", "Type": "Departure"},
    {"Flight Number": "IX 681", "Destination": "Tiruchirappalli", "Gate": "F30", "Departure Time": "22:15", "Status": "Will be Updated Soon", "Type": "Departure"},
    {"Flight Number": "TR 808", "Destination": "Tokyo-NRT", "Gate": "E28", "Departure Time": "22:15", "Status": "Will be Updated Soon", "Type": "Departure"},
    {"Flight Number": "BA 16", "Destination": "London Heathrow", "Gate": "D47", "Departure Time": "22:35", "Status": "Will be Updated Soon", "Type": "Departure"},
    {"Flight Number": "KE 644", "Destination": "Seoul", "Gate": "G20", "Departure Time": "22:35", "Status": "Will be Updated Soon","Type": "Departure"},
    {"Flight Number": "AF 257", "Destination": "Paris-CDG", "Gate": "C15", "Departure Time": "22:40", "Status": "Will be Updated Soon","Type": "Departure"},
    {"Flight Number": "SL 105", "Destination": "Bangkok-DMK", "Gate": "A9", "Departure Time": "22:40", "Status": "Will be Updated Soon","Type": "Departure"},
    {"Flight Number": "SQ 536", "Destination": "Kochi", "Gate": "A18", "Departure Time": "22:25", "Status": "Will be Updated Soon.", "Type": "Departure"},
]

arrival_flight_data = [
    {"Flight Number": "SQ 469", "Origin": "Colombo", "Gate": "D47", "Arrival Time": "07:10", "Status": "Will be Updated Soon", "Type": "Arrival"},
    {"Flight Number": "UA 1", "Origin": "San Francisco", "Gate": "F53", "Arrival Time": "08:00", "Status": "Will be Updated Soon", "Type": "Arrival"},
    {"Flight Number": "AI 392", "Origin": "Bengaluru", "Gate": "F34", "Arrival Time": "09:40", "Status": "Will be Updated Soon", "Type": "Arrival"},
    {"Flight Number": "SQ 305", "Origin": "London Heathrow", "Gate": "A2", "Arrival Time": "10:15", "Status": "Will be Updated Soon", "Type": "Arrival"}, 
    {"Flight Number": "GA 732", "Origin": "Bali", "Gate": "B3", "Arrival Time": "10:30", "Status": "Will be Updated Soon", "Type": "Arrival"}, 
    {"Flight Number": "QR 948", "Origin": "Doha", "Gate": "D34", "Arrival Time": "14:55", "Status": "Will be Updated Soon", "Type": "Arrival"},
    {"Flight Number": "EK 354", "Origin": "Dubai", "Gate": "C27", "Arrival Time": "14:40", "Status": "Will be Updated Soon", "Type": "Arrival"},
] 
#Login page
def login():
    print(f"Username: {username_entry.get()}")
    print(f"Password: {password_entry.get()}")

    if username_entry.get().strip() == "admin" and password_entry.get().strip() == "password1234":
        messagebox.showinfo("Login Successful", "Welcome!")
        login_window.destroy()
        show_main_window()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")
#Submit feedback
def submit_feedback():
    feedback = feedback_text.get("1.0", tk.END)
    if feedback.strip():
        messagebox.showinfo("Feedback Sent", "Thank You For Your Feedback!")
        feedback_window.destroy()
    else:
        messagebox.showerror("Error", "Please enter your feedback before submitting!")

#Feedback Form
def show_feedback_form():
    global feedback_window, feedback_text
    feedback_window = tk.Toplevel(root)
    feedback_window.title("Feedback")
    feedback_window.geometry("400x300")

    feedback_label = ttk.Label(feedback_window, text="Enter your Feedback:", font=("Helvetica", 12))
    feedback_label.pack(pady=10)

    feedback_text = tk.Text(feedback_window, width=50, height=10)
    feedback_text.pack(pady=10)

    submit_button = ttk.Button(feedback_window, text="Submit", command=submit_feedback)
    submit_button.pack(pady=10)

#Make a realtime flight status.
def update_flight_status():
    now = datetime.now()
    midnight = datetime.combine(now.date() + timedelta(days=1), datetime.min.time())
    
    # Update Departure Flights
    for flight in departure_flight_data:
        if "Departure Time" in flight:
            time = datetime.strptime(flight["Departure Time"], "%H:%M").replace(year=now.year, month=now.month, day=now.day)
            time_diff = (time - now).total_seconds() / 60

            if 45 >= time_diff > 20:
                flight["Status"] = "Gate Open"
            elif 20 >= time_diff > 10:
                flight["Status"] = "Boarding Passengers"
            elif 10 >= time_diff > 0:
                flight["Status"] = "Last Call"
            elif 0 >= time_diff > -10:
                flight["Status"] = "Gate Closed"
            elif time_diff <= -10 and now < midnight:
                flight["Status"] = "Departed"
            elif now >= midnight:
                flight["Status"] = "Will be Updated Soon"  # Reset to normal at midnight

        prefix = flight["Flight Number"].split()[0]
        flight["Airline"] = airline_mapping.get(prefix, "Unknown Airline")

    # Update Arrival Flights
    for flight in arrival_flight_data:
        if "Arrival Time" in flight:
            time = datetime.strptime(flight["Arrival Time"], "%H:%M").replace(year=now.year, month=now.month, day=now.day)
            time_diff = (time - now).total_seconds() / 60

            if 45 >= time_diff > 30: 
                flight["Status"] = "Approaching" 
            elif 30 >= time_diff > 10: 
                flight["Status"] = "Landing Soon" 
            elif 10 >= time_diff > 0: 
                flight["Status"] = "Landed" 
            elif 0 >= time_diff > -10: 
                flight["Status"] = "At Gate" 
            elif time_diff <= -10 and now < midnight: 
                flight["Status"] = "Arrived" 
            elif now >= midnight:
                flight["Status"] = "Will be Updated Soon" 

        prefix = flight["Flight Number"].split()[0]
        flight["Airline"] = airline_mapping.get(prefix, "Unknown Airline")

    # Refresh the Treeview
    refresh_table(flight_tree, departure_flight_data + arrival_flight_data)

def refresh_table(tree, flights):

    for row in tree.get_children():
        tree.delete(row)
        
    for flight in flights:
        tree.insert(
            "", 
            "end", 
            values=(
                flight.get("Flight Number"), 
                flight.get("Destination",flight.get("Origin")), 
                flight.get("Gate"), 
                flight.get("Departure Time", ""), 
                flight.get("Arrival Time", ""), 
                flight.get("Status"), 
                flight.get("Airline", ""),
                flight.get("Type", ""), 
            ),
        )

def show_flight_details(flight):
    # Create a new window for flight details
    detail_window = tk.Toplevel(root)
    detail_window.title(f"Details for Flight {flight.get('Flight Number', 'N/A')}")
    detail_window.geometry("400x300")

    # Display Flight Number
    flight_number_label = ttk.Label(
        detail_window, text=f"Flight Number: {flight.get('Flight Number', 'N/A')}", font=("Helvetica", 12)
    )
    flight_number_label.pack(pady=5)

    # Display Gate
    gate_label = ttk.Label(
        detail_window, text=f"Gate: {flight.get('Gate', 'N/A')}", font=("Helvetica", 12)
    )
    gate_label.pack(pady=5)

    # Display Destination or Origin
    if "Destination" in flight:
        destination_label = ttk.Label(
            detail_window, text=f"Destination: {flight.get('Destination', 'N/A')}", font=("Helvetica", 12)
        )
        destination_label.pack(pady=5)
    elif "Origin" in flight:
        origin_label = ttk.Label(
            detail_window, text=f"Origin: {flight.get('Origin', 'N/A')}", font=("Helvetica", 12)
        )
        origin_label.pack(pady=5)

    # Display Departure or Arrival Time
    if "Departure Time" in flight:
        departure_time_label = ttk.Label(
            detail_window, text=f"Departure Time: {flight.get('Departure Time', 'N/A')}", font=("Helvetica", 12)
        )
        departure_time_label.pack(pady=5)
    elif "Arrival Time" in flight:
        arrival_time_label = ttk.Label(
            detail_window, text=f"Arrival Time: {flight.get('Arrival Time', 'N/A')}", font=("Helvetica", 12)
        )
        arrival_time_label.pack(pady=5)

    # Display Status
    status_label = ttk.Label(
        detail_window, text=f"Status: {flight.get('Status', 'N/A')}", font=("Helvetica", 12)
    )
    status_label.pack(pady=5)

    # Display Airline
    airline_label = ttk.Label(
        detail_window, text=f"Airline: {flight.get('Airline', 'N/A')}", font=("Helvetica", 12)
    )
    airline_label.pack(pady=5)

def on_flight_select(event):
    selected_item = flight_tree.selection()
    if selected_item:
        item = selected_item[0]
        flight_number = flight_tree.item(item, 'values')[0]
        flight = next((flight for flight in departure_flight_data + arrival_flight_data if flight["Flight Number"] == flight_number))
        if flight:
            show_flight_details(flight)

def show_arrival_flights(): 
    refresh_table(flight_tree, arrival_flight_data)

def show_departure_flights():
     refresh_table(flight_tree, departure_flight_data)

def update_time():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    time_label.config(text=now)
    root.after(1000, update_time)

#Create a main window.
def show_main_window():
    global root, flight_tree, time_label
    root = tk.Tk()
    root.title("Advanced Flight Information")
    root.geometry("1280x800")

    bg_image = Image.open("C:\\Users\\My Laptop\\Downloads\\main\\1717002487808.jpg")
    bg_image = bg_image.resize((1280,800))
    bg_image = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(root, relief=tk.FLAT, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    arrival_button = ttk.Button(root, text="View Arrival Flights", command=show_arrival_flights)
    arrival_button.pack(pady=10)

    departure_button = ttk.Button(root, text="View Departure Flights", command=show_departure_flights)
    departure_button.pack(pady=10)

    title_frame = ttk.Frame(root)
    title_frame.pack(pady=10)

    title_label = ttk.Label(title_frame, text="Flight Information", font=("Helvetica", 18), background= '#87CEEB')
    title_label.pack()

    table_frame = ttk.Frame(root, style="TFrame")
    table_frame.pack(pady=10, padx=10)

    flight_columns = ("#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8")
    flight_tree = ttk.Treeview(table_frame, columns= flight_columns, show='headings', height=25)

    flight_tree.heading("#1", text="Flight Number")
    flight_tree.heading("#2", text="Destination/Origin")
    flight_tree.heading("#3", text="Gate")
    flight_tree.heading("#4", text="Departure Time")
    flight_tree.heading("#5", text="Arrival Time")
    flight_tree.heading("#6", text="Status")
    flight_tree.heading("#7", text="Airline")
    flight_tree.heading("#8", text="Type")

    flight_tree.column("#1", minwidth=0, width=200)
    flight_tree.column("#2", minwidth=0, width=250) 
    flight_tree.column("#3", minwidth=0, width=150)
    flight_tree.column("#4", minwidth=0, width=150)
    flight_tree.column("#5", minwidth=0, width=250)
    flight_tree.column("#6", minwidth=0, width=250)
    flight_tree.column("#7", minwidth=0, width=200)
    flight_tree.column("#8", minwidth=0, width=100)

    flight_tree.pack()
    flight_tree.pack()
    flight_tree.bind("<<TreeviewSelect>>", on_flight_select)
    button_frame = ttk.Frame(root)
    button_frame.pack(pady=10)
    refresh_button = ttk.Button(button_frame, text="Refresh", command=update_flight_status)
    refresh_button.pack(side=tk.LEFT, padx=10)
    feedback_button = ttk.Button(button_frame, text="Feedback", command=show_feedback_form)
    feedback_button.pack(side=tk.LEFT, padx=10)

    time_label = ttk.Label(root, text="Flight Information", font=("Times New Roman", 14))
    time_label.pack(pady=10)
    update_time()

    update_flight_status()  # Initial call to set status
    root.mainloop()


login_window = tk.Tk()
login_window.title("Login")

login_window.geometry(f"{login_window.winfo_screenwidth()}x{login_window.winfo_screenheight()}")

def resize_image(event):
    new_width = event.width

# Background image on login page.
bg_login_image = Image.open("C:\\Users\\My Laptop\\Downloads\\main\\1717002487808.jpg")
bg_login_image = bg_login_image.resize((1280,800)) # Just change the numbers to the window size
bg_login_image = ImageTk.PhotoImage(bg_login_image)
bg_login_label = tk.Label(login_window,relief=tk.FLAT, image=bg_login_image)
bg_login_label.pack(fill="both", expand=True)
bg_login_label.place(relwidth=1, relheight=1)

frame = tk.Frame(login_window, background="#87CEEB")
frame.pack(expand=True)

# Display a logo
logo_image_path = "C:\\Users\\My Laptop\\Downloads\\Changi_Airport_logo.svg.png"
logo_image = Image.open(logo_image_path)
logo_image = logo_image.resize((250, 150), Image.Resampling.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_image)

logo_label = ttk.Label(login_window, image=logo_photo, background="#87CEEB")
logo_label.image = logo_photo
logo_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

# Display a Username
username_label = ttk.Label(frame, text="Username", background="#87CEEB", width=9)
username_label.pack(pady=10)
username_entry = ttk.Entry(frame, width=30)
username_entry.pack(pady=10)

# display a Password 
password_label = ttk.Label(frame, text="Password", background="#87CEEB", width=9)
password_label.pack(pady=10)
password_entry = ttk.Entry(frame, show="*", width=30)
password_entry.pack(pady=10)

# Login button
login_button = ttk.Button(frame, text="Login", command=login)
login_button.pack(pady=10)
login_window.mainloop()