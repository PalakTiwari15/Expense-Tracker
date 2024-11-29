import mysql.connector

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="root",  # Replace with your MySQL username
    password="",  # Replace with your MySQL password
    database="expense_tracker"  # Ensure this database exists
)

cursor = db.cursor()

# Function to add an expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Travel): ")
    description = input("Enter description: ")
    amount = input("Enter amount: ")

    try:
        query = "INSERT INTO expenses (date, category, description, amount) VALUES (%s, %s, %s, %s)"
        values = (date, category, description, float(amount))
        cursor.execute(query, values)
        db.commit()
        print("Expense added successfully!")
    except Exception as e:
        print("Error:", e)

# Function to view all expenses
def view_expenses():
    try:
        query = "SELECT * FROM expenses"
        cursor.execute(query)
        results = cursor.fetchall()

        if results:
            print("\nExpenses:")
            print(f"{'ID':<5} {'Date':<12} {'Category':<15} {'Description':<30} {'Amount':<10}")
            print("-" * 80)
            for row in results:
                print(f"{row[0]:<5} {str(row[1]):<12} {row[2]:<15} {row[3]:<30} {row[4]:<10.2f}")
        else:
            print("No expenses found.")
    except Exception as e:
        print("Error:", e)

# Function to search expenses
def search_expenses():
    print("\nSearch Expenses:")
    print("1. By Date")
    print("2. By Category")
    choice = input("Choose an option: ")

    if choice == "1":
        date = input("Enter date (YYYY-MM-DD): ")
        query = "SELECT * FROM expenses WHERE date = %s"
        values = (date,)
    elif choice == "2":
        category = input("Enter category: ")
        query = "SELECT * FROM expenses WHERE category = %s"
        values = (category,)
    else:
        print("Invalid choice.")
        return

    try:
        cursor.execute(query, values)
        results = cursor.fetchall()

        if results:
            print(f"\n{'ID':<5} {'Date':<12} {'Category':<15} {'Description':<30} {'Amount':<10}")
            print("-" * 80)
            for row in results:
                print(f"{row[0]:<5} {str(row[1]):<12} {row[2]:<15} {row[3]:<30} {row[4]:<10.2f}")
        else:
            print("No matching records found.")
    except Exception as e:
        print("Error:", e)

# Function to delete an expense
def delete_expense():
    expense_id = input("Enter the ID of the expense to delete: ")

    try:
        query = "DELETE FROM expenses WHERE id = %s"
        values = (expense_id,)
        cursor.execute(query, values)
        db.commit()

        if cursor.rowcount > 0:
            print("Expense deleted successfully.")
        else:
            print("Expense not found.")
    except Exception as e:
        print("Error:", e)

# Main menu function
def main_menu():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expenses")
        print("4. Delete Expense")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            search_expenses()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the program
main_menu()

# Close the database connection when the program exits
cursor.close()
db.close()
