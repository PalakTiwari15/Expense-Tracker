# Expense Tracker CLI Application

## **Overview**
The **Expense Tracker CLI Application** is a simple yet powerful tool to help you track your daily expenses. With this command-line interface, you can add, view, search, and delete your expenses seamlessly while storing all your data in a MySQL database for secure and efficient management.

This project is designed for beginners learning Python and MySQL integration, providing hands-on experience with database operations and Python programming.

---

## **Features**
- **Add Expenses**: Record your expenses with details like date, category, description, and amount.
- **View Expenses**: View all recorded expenses in a neatly formatted table.
- **Search Expenses**: Find specific expenses by date or category.
- **Delete Expenses**: Remove unwanted expense records using their unique ID.
- **Persistent Storage**: All data is securely stored in a MySQL database for future access.

---

## **How It Works**
1. The user interacts with a **menu-driven interface** to select various options.
2. Data is entered via the CLI and stored in the MySQL database.
3. Users can view their data in a formatted table or search for specific entries.
4. Data is manipulated (added, searched, or deleted) using **SQL queries** executed from Python.

---

## **Tech Stack**
- **Python**:
  - `mysql.connector` for database connection and operations.
  - CLI-based input/output for a simple, user-friendly experience.
- **MySQL**:
  - Database storage for expense records.
  - SQL queries for CRUD (Create, Read, Update, Delete) operations.

---

## **Setup Instructions**

### **Pre-Requisites**
1. **Python** (version 3.7 or higher): [Download Python](https://www.python.org/downloads/)
2. **MySQL** (server and client): [Download MySQL](https://dev.mysql.com/downloads/)
3. **Python Package**: Install the MySQL connector library by running:
   ```bash
   pip install mysql-connector-python
   ```

### **Database Setup**
1. Open MySQL Workbench or the MySQL CLI.
2. Create the database and table by running the following commands:
   ```sql
   CREATE DATABASE expense_tracker;

   USE expense_tracker;

   CREATE TABLE expenses (
       id INT AUTO_INCREMENT PRIMARY KEY,
       date DATE,
       category VARCHAR(50),
       description TEXT,
       amount DECIMAL(10, 2)
   );
   ```

### **Running the Application**
1. Clone or download the script.
2. Open the script in any Python IDE or terminal.
3. Update the `mysql.connector.connect` parameters in the script:
   ```python
   db = mysql.connector.connect(
       host="localhost",
       user="your_mysql_username",
       password="your_mysql_password",
       database="expense_tracker"
   )
   ```
4. Run the script:
   ```bash
   python expense_tracker.py
   ```

---

## **Usage**
1. Choose an option from the menu:
   ```
   Expense Tracker
   1. Add Expense
   2. View Expenses
   3. Search Expenses
   4. Delete Expense
   5. Exit
   ```
2. Follow the on-screen instructions to perform the desired action.
3. View formatted outputs for a clean and intuitive experience.

---

## **Example Outputs**
### Adding an Expense:
```
Enter date (YYYY-MM-DD): 2024-11-15
Enter category (e.g., Food, Travel): Food
Enter description: Lunch with friends
Enter amount: 500
Expense added successfully!
```

### Viewing Expenses:
```
Expenses:
ID    Date         Category        Description                    Amount
1     2024-11-15   Food            Lunch with friends             500.00
```

### Searching Expenses:
```
Search Expenses:
1. By Date
2. By Category
Choose an option: 1
Enter date (YYYY-MM-DD): 2024-11-15
ID    Date         Category        Description                    Amount
1     2024-11-15   Food            Lunch with friends             500.00
```

---

## **File Structure**
- **`expense_tracker.py`**: Main Python script that runs the application.

---

## **Key Learning Concepts**
- **Python Functions**: Modular design using functions like `add_expense()` and `view_expenses()`.
- **MySQL Integration**: Establishing a connection and executing SQL queries using `mysql.connector`.
- **Menu-Driven CLI**: Creating a user-friendly command-line interface.
- **Data Persistence**: Storing and retrieving data securely in a MySQL database.
- **Error Handling**: Graceful handling of invalid inputs and database errors.

---

## **Possible Enhancements**
- Add an **update expense** feature.
- Implement data visualization using libraries like `matplotlib` for expense trends.
- Create a web or GUI-based version for a more interactive experience.
- Add user authentication for secure access.

---

## **Conclusion**
The **Expense Tracker CLI Application** is an excellent starting project for Python beginners to explore database integration and practical software development. With a robust structure and clear functionality, this project not only helps in learning coding concepts but also serves as a handy personal tool to manage expenses effectively.

---

## **Contributors**
- **Palak Tiwari**: Developer and Python Enthusiast
