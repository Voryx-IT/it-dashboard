import os

# --- Part 1: Class Definition ---
class Employee:
    def __init__(self, emp_id, fname, lname, department, jobtitle):
        # Attributes as defined in the UML diagram [cite: 2, 3, 4, 5, 6]
        self.employee_id = str(emp_id)
        self.fname = str(fname)
        self.lname = str(lname)
        self.department = str(department)
        self.jobtitle = str(jobtitle)

    def getId(self): # [cite: 9]
        return self.employee_id

    def getName(self): # [cite: 13]
        return f"{self.fname} {self.lname}"

    def getDepartment(self): # [cite: 14]
        return self.department

    def getJobTitle(self): # [cite: 16]
        return self.jobtitle

# --- Part 2: Main Program Logic ---
def main():
    employee_list = []
    
    # Path handling to ensure file is found in the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'employees.txt')

    try:
        with open(file_path, 'r') as file:
            # Clean up lines and remove empty ones
            lines = [line.strip() for line in file if line.strip()]
            
            # Reads the information about each employee into an object [cite: 7]
            for i in range(0, len(lines), 4):
                if i + 3 < len(lines):
                    # Cleaning the ID line (handles "47899") 
                    raw_id = lines[i]
                    emp_id = raw_id.split(']')[-1].strip()
                    
                    # Splitting full name into fname and lname
                    name_parts = lines[i+1].split(maxsplit=1)
                    fname = name_parts[0]
                    lname = name_parts[1] if len(name_parts) > 1 else ""
                    
                    dept = lines[i+2]
                    title = lines[i+3]

                    # Add each object into a list
                    emp_obj = Employee(emp_id, fname, lname, dept, title)
                    employee_list.append(emp_obj)

        # --- Neat Visual Display ---
        print("\n" + "="*75)
        print(f"{'EMPLOYEE DIRECTORY':^75}")
        print("="*75)
        # Header with specific column widths
        print(f"{'ID':<10} | {'NAME':<20} | {'DEPARTMENT':<18} | {'JOB TITLE'}")
        print("-" * 75)
        
        # Loop through the list to print employee information
        for emp in employee_list:
            print(f"{emp.getId():<10} | {emp.getName():<20} | {emp.getDepartment():<18} | {emp.getJobTitle()}")
        
        print("="*75)
        print(f"Total Employees Processed: {len(employee_list)}")

    except FileNotFoundError:
        print(f"ERROR: Could not find 'employees.txt' at: {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    input("\nPress Enter to close...")

if __name__ == "__main__":
    main()