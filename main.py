"""
IT Dashboard — COP1034C Python for IT
Jorden Stafford | 4/7/26

Description: A simple IT monitoring tool that evaluates server disk usage.
"""

# ── Application Metadata ──────────────────────────────────
APP_NAME = "IT Dashboard"
VERSION = "0.1.0"

def main():
    # --- 1. Variable Declarations (Req 1, 2, & 3) ---
    server_name = "Not entered"    # str
    ip_address  = "Not entered"    # str
    department  = "Not entered"    # str
    total_disk_gb = 0              # int
    used_disk_gb  = 0              # int
    usage_pct     = 0.0            # float
    report_ready  = False          # bool

    # --- 2. Main Menu Loop (Req 6) ---
    while True:
        print("\n--- IT Report Generator ---")
        print("1) Enter server info")
        print("2) View report")
        print("3) Exit")

        choice = input("\nSelect an option: ")

        # --- 3. Input and Validation (Req 3 & 9) ---
        if choice == "1":
            print("\n--- Enter Server Details ---")
            server_name = input("Server Name : ")
            ip_address  = input("IP Address  : ")
            department  = input("Department  : ")
            
            # Casting numeric inputs (Req 3)
            total_disk_gb = int(input("Total Disk (GB): "))
            used_disk_gb  = int(input("Used Disk (GB) : "))

            # Edge Case Handling (Req 9)
            if total_disk_gb <= 0:
                print("\n[!] Error: Total disk must be greater than 0.")
                report_ready = False
            elif used_disk_gb > total_disk_gb:
                print("\n[!] Error: Used disk cannot exceed total disk.")
                report_ready = False
            elif used_disk_gb < 0:
                print("\n[!] Error: Values cannot be negative.")
                report_ready = False
            else:
                # Logic & Calculation
                usage_pct = (used_disk_gb / total_disk_gb) * 100
                report_ready = True
                print("\nData saved successfully!")

        # --- 4. Logic & Report Output (Req 4, 5, & 7) ---
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

                # Formatted Output (Req 4 & 7)
                print("\n====================================")
                print(f"{'IT SYSTEM STATUS REPORT':^36}")
                print("====================================")
                print(f"{'Server Name':<12}: {server_name}")
                print(f"{'IP Address':<12}: {ip_address}")
                print(f"{'Department':<12}: {department}")
                print("-" * 36)
                print(f"{'Total Disk':<12}: {total_disk_gb} GB")
                print(f"{'Used Disk':<12}: {used_disk_gb} GB")
                print(f"{'Free Disk':<12}: {total_disk_gb - used_disk_gb} GB")
                print(f"{'Usage':<12}: {usage_pct:.2f}%")
                print(f"{'Status':<12}: {status}")
                print("====================================")

                # Requirement 7: For Loop
                # Printing simulated health checks below the report
                checks = ["Ping response", "DNS resolution", "Firewall active"]
                print("\nSystem Health Checks:")
                for check in checks:
                    print(f"  - {check:<18}: PASS")

        # --- 5. Exit Option ---
        elif choice == "3":
            print(f"Exiting {APP_NAME}. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# ── Run the program ───────────────────────────────────────
if __name__ == "__main__":
    main()