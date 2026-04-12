"""
IT Dashboard — COP1034C Python for IT
Jorden Stafford | 4/7/26

Description: A simple IT monitoring tool that evaluates server disk usage.
"""

# ── Application Metadata & Imports ───────────────────────
from datetime import datetime  

APP_NAME = "IT Dashboard"
VERSION = "0.1.0"

def main():
    # --- Variable Declarations (Req 1, 2) ---
    # Using descriptive snake_case and all four basic types
    server_name = "Not entered"    # str
    ip_address  = "Not entered"    # str
    department  = "Not entered"    # str
    total_disk_gb = 0              # int
    used_disk_gb  = 0              # int
    usage_pct     = 0.0            # float
    report_ready  = False          # bool

    # --- Main Menu Loop (Req 6) ---
    while True:
        print(f"\n--- {APP_NAME} v{VERSION} ---")
        print("1) Enter server info")
        print("2) View report")
        print("3) Student Info (Lab #1)")
        print("4) Exit")

        choice = input("\nSelect an option: ")

        # --- Input and Validation (Req 3 and 9) ---
        if choice == "1":
            print("\n--- Enter Server Details ---")
            server_name = input("Server Name : ")
            ip_address  = input("IP Address  : ")
            department  = input("Department  : ")
            
            # Casting numeric inputs (Req 3)
            try:
                total_disk_gb = int(input("Total Disk (GB): "))
                used_disk_gb  = int(input("Used Disk (GB) : "))

                # Edge Case Handling (Req 9)
                if total_disk_gb <= 0:
                    print("\n[!] Error: Total disk must be greater than 0.")
                    report_ready = False
                elif used_disk_gb > total_disk_gb:
                    print("\n[!] Error: Used disk cannot exceed total disk.")
                    report_ready = False
                elif used_disk_gb < 0 or total_disk_gb < 0:
                    print("\n[!] Error: Values cannot be negative.")
                    report_ready = False
                else:
                    # Logic and Calculation
                    usage_pct = (used_disk_gb / total_disk_gb) * 100
                    report_ready = True
                    print("\nData saved successfully!")
            except ValueError:
                print("\n[!] Error: Please enter valid numeric whole numbers.")

        # --- Logic and Report Output (Req 4, 5, and 7) ---
        elif choice == "2":
            if not report_ready:
                print("\n[!] Please enter data first (Option 1).")
            else:
                # Classification Logic (Req 5)
                if usage_pct > 90:
                    status = "CRITICAL - Immediate action required"
                elif usage_pct > 75:
                    status = "WARNING - Disk usage is elevated"
                else:
                    status = "OK - Disk usage is normal"

                # Formatted Output (Req 4)
                print("\n" + "="*40)
                print(f"{'IT SYSTEM STATUS REPORT':^40}")
                print("="*40)
                print(f"{'Server Name':<15}: {server_name}")
                print(f"{'IP Address':<15}: {ip_address}")
                print(f"{'Department':<15}: {department}")
                print("-" * 40)
                print(f"{'Total Disk':<15}: {total_disk_gb} GB")
                print(f"{'Used Disk':<15}: {used_disk_gb} GB")
                print(f"{'Free Disk':<15}: {total_disk_gb - used_disk_gb} GB")
                print(f"{'Usage':<15}: {usage_pct:.2f}%")
                print(f"{'Status':<15}: {status}")
                print("="*40)

                # Requirement 7: For Loop
                checks = ["Ping response", "DNS resolution", "Firewall active"]
                print("\nSystem Health Checks:")
                for check in checks:
                    print(f"  - {check:<18}: PASS")

        # --- In-Class Lab #1 Requirement ---
        elif choice == "3":
            # Data for Lab #1
            name = "Jorden Stafford"
            course = "Programming for IT Professionals"
            instructor = "Professor Mora"
            assignment = "Week 1 in class lab"
            # Requirement: Use datetime for current date
            today = datetime.now().strftime("%m/%d/%Y")

            print("\n" + "~"*50)
            print(f"{'STUDENT & COURSE INFORMATION':^50}")
            print("~"*50)
            print(f"{'Name':<15}: {name}")
            print(f"{'Course':<15}: {course}")
            print(f"{'Instructor':<15}: {instructor}")
            print(f"{'Assignment':<15}: {assignment}")
            print(f"{'Date':<15}: {today}")
            print("~"*50)

        # --- Exit Option ---
        elif choice == "4":
            print(f"\nExiting {APP_NAME}. Goodbye!")
            break

        else:
            print("\n[!] Invalid choice. Please enter 1, 2, 3, or 4.")

# ── Run the program ───────────────────────────────────────
if __name__ == "__main__":
    main()