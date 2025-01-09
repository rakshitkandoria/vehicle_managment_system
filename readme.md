# 🚗 Vehicle Management System 🏎️

Welcome to the **Vehicle Management System**! 🚙 This simple yet powerful Python application uses **Tkinter** for its graphical user interface (GUI) and **MySQL** for storing and managing vehicle data. You can easily register, view, and search for vehicles, all with a user-friendly and intuitive interface. 

---

## 📌 Features

- **📝 Register a Vehicle**: Add a new vehicle by providing its details such as license plate, make, model, and year.
- **👀 View All Vehicles**: See all the vehicles registered in the system, displaying their details.
- **🔍 Search for a Vehicle**: Search for a specific vehicle by its license plate number.
- **🚶‍♂️ Easy Navigation**: Navigate through a simple and intuitive interface, ensuring a smooth user experience.

---

## 🔧 Requirements

To run this project, you will need:

- **Python 3.x** (Download [here](https://www.python.org/downloads/))
- **Tkinter** (Pre-installed with Python)
- **MySQL** (Download [here](https://dev.mysql.com/downloads/))

### 🛠 Installing Dependencies

1. **Python**: Install Python 3.x on your system.
2. **MySQL**: Ensure MySQL is installed on your machine.
3. **PyMySQL**: This library is required to connect Python with MySQL. Install it via pip:

    ```bash
    pip install pymysql
    ```

---

## 📥 Setup Instructions

### 1. **Create a MySQL Database**:
    - Create a MySQL database called `vehicle_management` (or modify the connection string in the code).
    - Create a `vehicles` table using this SQL schema:

    ```sql
    CREATE TABLE vehicles (
        license_plate VARCHAR(50) PRIMARY KEY,
        make VARCHAR(100),
        model VARCHAR(100),
        year INT
    );
    ```

### 2. **Running the Application**:
    - Start your MySQL server.
    - Open a terminal or command prompt and navigate to the folder where the Python script is located.
    - Run the script using:

    ```bash
    python vehicle_management.py
    ```

---

## 🖥️ Usage Guide

1. **🏠 Home Page**: When you launch the application, you will be presented with a home page that includes:
    - **Register a Vehicle**: Click to add a new vehicle.
    - **View All Vehicles**: Click to see all registered vehicles.
    - **Search for a Vehicle**: Click to find a vehicle by its license plate.
    - **🚪 Exit**: Click to close the application.

2. **📝 Register a Vehicle**:
    - Click on "Register a Vehicle".
    - Fill in the required details (license plate, make, model, year).
    - Press "Add Vehicle" to store the vehicle in the database.

3. **👀 View All Vehicles**:
    - Click on "View All Vehicles" to display all registered vehicles.
    - After viewing, the system will automatically redirect you back to the home page.

4. **🔍 Search for a Vehicle**:
    - Click on "Search for a Vehicle".
    - Enter a vehicle's license plate number to view its details.
    - If found, the vehicle's information will be displayed; if not, a "No Vehicle Found" message will appear.

---

## 📸 Screenshots

Here are some screenshots of the application in action:

[Home Page] 

<img width="391" alt="image" src="https://github.com/user-attachments/assets/a6cb7483-1702-4b64-afd9-0ef286f28fcd" />

*The home screen with options to register, view, or search vehicles.*

[Register Vehicle]

<img width="278" alt="image" src="https://github.com/user-attachments/assets/32f79448-cd1c-4cea-a009-89a66ed85efb" />

*The form to register a new vehicle.*

[View All Vehicles]

<img width="269" alt="image" src="https://github.com/user-attachments/assets/a6dd2276-0811-4279-a8fd-b944344634df" />

*Displaying all registered vehicles.*



