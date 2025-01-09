import tkinter as tk
from tkinter import messagebox
import pymysql

# MySQL connection setup
def get_db_connection():
    return pymysql.connect(
        host="localhost",
        user="root",          
        password="passward",  
        database="vehicle_management"
    )

class VehicleManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Vehicle Management System")
        self.root.geometry("600x600")
        self.root.config(bg="#f2f2f2")
        self.current_frame = None  # To keep track of the current frame
        self.vehicles = []

        self.show_home_page()

    def show_home_page(self):
        """Display the home page where user can choose actions."""
        self.clear_current_frame()

        home_frame = tk.Frame(self.root, bg="#f2f2f2")
        home_frame.pack(fill="both", expand=True)

        title_label = tk.Label(home_frame, text="Vehicle Management System", font=("Arial", 24, "bold"), bg="#f2f2f2", fg="#4CAF50")
        title_label.pack(pady=20)

        add_vehicle_button = tk.Button(home_frame, text="Register a Vehicle", width=25, height=2, command=self.show_register_page, bg="#4CAF50", fg="white", font=("Arial", 14, "bold"))
        add_vehicle_button.pack(pady=15)

        view_all_button = tk.Button(home_frame, text="View All Vehicles", width=25, height=2, command=self.show_view_all_vehicles_page, bg="#2196F3", fg="white", font=("Arial", 14, "bold"))
        view_all_button.pack(pady=15)

        search_button = tk.Button(home_frame, text="Search for a Vehicle", width=25, height=2, command=self.show_search_page, bg="#FF9800", fg="white", font=("Arial", 14, "bold"))
        search_button.pack(pady=15)

        exit_button = tk.Button(home_frame, text="Exit", width=25, height=2, command=self.root.quit, bg="#f44336", fg="white", font=("Arial", 14, "bold"))
        exit_button.pack(pady=15)

        self.current_frame = home_frame

    def show_register_page(self):
        """Show the vehicle registration page."""
        self.clear_current_frame()

        register_frame = tk.Frame(self.root, bg="#f2f2f2")
        register_frame.pack(fill="both", expand=True)

        title_label = tk.Label(register_frame, text="Register a Vehicle", font=("Arial", 24, "bold"), bg="#f2f2f2", fg="#4CAF50")
        title_label.pack(pady=20)

        # Vehicle registration form
        tk.Label(register_frame, text="License Plate:", bg="#f2f2f2", font=("Arial", 12)).pack(pady=5)
        self.license_plate_entry = tk.Entry(register_frame, font=("Arial", 12))
        self.license_plate_entry.pack(pady=5)

        tk.Label(register_frame, text="Make:", bg="#f2f2f2", font=("Arial", 12)).pack(pady=5)
        self.make_entry = tk.Entry(register_frame, font=("Arial", 12))
        self.make_entry.pack(pady=5)

        tk.Label(register_frame, text="Model:", bg="#f2f2f2", font=("Arial", 12)).pack(pady=5)
        self.model_entry = tk.Entry(register_frame, font=("Arial", 12))
        self.model_entry.pack(pady=5)

        tk.Label(register_frame, text="Year:", bg="#f2f2f2", font=("Arial", 12)).pack(pady=5)
        self.year_entry = tk.Entry(register_frame, font=("Arial", 12))
        self.year_entry.pack(pady=5)

        add_button = tk.Button(register_frame, text="Add Vehicle", command=self.add_vehicle, bg="#4CAF50", fg="white", font=("Arial", 14, "bold"))
        add_button.pack(pady=20)

        back_button = tk.Button(register_frame, text="Back to Home", command=self.show_home_page, bg="#9E9E9E", fg="white", font=("Arial", 14, "bold"))
        back_button.pack(pady=20)

        self.current_frame = register_frame

    def add_vehicle(self):
        """Add vehicle to the system."""
        license_plate = self.license_plate_entry.get()
        make = self.make_entry.get()
        model = self.model_entry.get()
        year = self.year_entry.get()

        if not (license_plate and make and model and year):
            messagebox.showerror("Input Error", "Please fill in all fields.")
            return

        # Save to DB
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO vehicles (license_plate, make, model, year) VALUES (%s, %s, %s, %s)",
                       (license_plate, make, model, year))
        connection.commit()
        cursor.close()
        connection.close()

        messagebox.showinfo("Success", "Vehicle registered successfully!")
        self.show_home_page()

    def show_view_all_vehicles_page(self):
        """Show all vehicles."""
        self.clear_current_frame()

        view_frame = tk.Frame(self.root, bg="#f2f2f2")
        view_frame.pack(fill="both", expand=True)

        title_label = tk.Label(view_frame, text="All Vehicles", font=("Arial", 24, "bold"), bg="#f2f2f2", fg="#4CAF50")
        title_label.pack(pady=20)

        # Fetch vehicles from DB
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM vehicles")
        rows = cursor.fetchall()

        for row in rows:
            vehicle_info = f"License Plate: {row[0]}\nMake: {row[1]}\nModel: {row[2]}\nYear: {row[3]}"
            vehicle_label = tk.Label(view_frame, text=vehicle_info, bg="#f2f2f2", font=("Arial", 12))
            vehicle_label.pack(pady=5)

        # Add a delay before returning to the home page
        self.root.after(3000, self.show_home_page)  # 3000 milliseconds (3 seconds)

        self.current_frame = view_frame

    def show_search_page(self):
        """Show the search page to search for vehicles."""
        self.clear_current_frame()

        search_frame = tk.Frame(self.root, bg="#f2f2f2")
        search_frame.pack(fill="both", expand=True)

        title_label = tk.Label(search_frame, text="Search for Vehicle", font=("Arial", 24, "bold"), bg="#f2f2f2", fg="#4CAF50")
        title_label.pack(pady=20)

        tk.Label(search_frame, text="Enter License Plate:", bg="#f2f2f2", font=("Arial", 12)).pack(pady=5)
        self.search_plate_entry = tk.Entry(search_frame, font=("Arial", 12))
        self.search_plate_entry.pack(pady=5)

        search_button = tk.Button(search_frame, text="Search", command=self.search_vehicle, bg="#FF9800", fg="white", font=("Arial", 14, "bold"))
        search_button.pack(pady=20)

        back_button = tk.Button(search_frame, text="Back to Home", command=self.show_home_page, bg="#9E9E9E", fg="white", font=("Arial", 14, "bold"))
        back_button.pack(pady=20)

        self.current_frame = search_frame

    def search_vehicle(self):
        """Search a vehicle by license plate."""
        license_plate = self.search_plate_entry.get()

        if not license_plate:
            messagebox.showerror("Input Error", "Please enter a license plate.")
            return

        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM vehicles WHERE license_plate = %s", (license_plate,))
        row = cursor.fetchone()

        if row:
            vehicle_info = f"License Plate: {row[0]}\nMake: {row[1]}\nModel: {row[2]}\nYear: {row[3]}"
            messagebox.showinfo("Vehicle Found", vehicle_info)
        else:
            messagebox.showinfo("No Vehicle Found", "No vehicle found with that license plate.")

        cursor.close()
        connection.close()

    def clear_current_frame(self):
        """Clear the current frame."""
        if self.current_frame:
            self.current_frame.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = VehicleManagementApp(root)
    root.mainloop()
