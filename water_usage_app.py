import sqlite3
import datetime
import matplotlib.pyplot as plt


# ================================
# Database Setup
# ================================
def init_db():
    conn = sqlite3.connect("water_usage.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS water_usage (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            liters REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()


# ================================
# Add Daily Usage
# ================================
def add_water_usage(liters):
    conn = sqlite3.connect("water_usage.db")
    cursor = conn.cursor()
    today = datetime.date.today().isoformat()
    cursor.execute("INSERT INTO water_usage (date, liters) VALUES (?, ?)", (today, liters))
    conn.commit()
    conn.close()
    print(f"✅ Recorded {liters} liters for {today}")


# ================================
# Fetch Usage Data
# ================================
def get_all_usage():
    conn = sqlite3.connect("water_usage.db")
    cursor = conn.cursor()
    cursor.execute("SELECT date, liters FROM water_usage ORDER BY date ASC")
    rows = cursor.fetchall()
    conn.close()
    return rows


# ================================
# Summary Statistics
# ================================
def usage_summary():
    data = get_all_usage()
    if not data:
        print("⚠ No data available yet.")
        return

    liters = [row[1] for row in data]
    total = sum(liters)
    avg = sum(liters) / len(liters)
    max_usage = max(liters)
    min_usage = min(liters)

    print("\n📊 Water Usage Summary:")
    print(f" - Total Usage: {total:.2f} liters")
    print(f" - Average Daily Usage: {avg:.2f} liters")
    print(f" - Maximum Daily Usage: {max_usage:.2f} liters")
    print(f" - Minimum Daily Usage: {min_usage:.2f} liters")


# ================================
# Visualization
# ================================
def plot_usage():
    data = get_all_usage()
    if not data:
        print("⚠ No data available for plotting.")
        return

    dates = [row[0] for row in data]
    liters = [row[1] for row in data]

    plt.figure(figsize=(8, 5))
    plt.bar(dates, liters, color="skyblue")
    plt.xlabel("Date")
    plt.ylabel("Water Usage (Liters)")
    plt.title("Daily Household Water Usage")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# ================================
# Alert System
# ================================
def check_alert(threshold=100):
    data = get_all_usage()
    if not data:
        return
    today = data[-1]
    if today[1] > threshold:
        print(f"🚨 ALERT: {today[1]} liters used on {today[0]} (exceeds {threshold} liters)!")
    else:
        print(f"✅ Usage for {today[0]} is within limit ({today[1]} liters).")


# ================================
# Main Program
# ================================
if __name__ == "__main__":
    init_db()

    while True:
        print("\n=== 🌊 Water Usage Tracking App ===")
        print("1. Add Water Usage")
        print("2. View Summary")
        print("3. Plot Usage Chart")
        print("4. Check Alert")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            liters = float(input("Enter water usage (liters): "))
            add_water_usage(liters)
        elif choice == "2":
            usage_summary()
        elif choice == "3":
            plot_usage()
        elif choice == "4":
            threshold = float(input("Enter alert threshold (liters): "))
            check_alert(threshold)
        elif choice == "5":
            print("👋 Exiting... Stay water conscious!")
            break
        else:
            print("⚠ Invalid choice. Please try again.")
