# =================================================================
# ASSIGNMENT 5: EMPLOYEE HIERARCHY (INHERITANCE)
# =================================================================

# --- PART 1: BASE CLASS ---
class Employee:
    def __init__(self, employee_id, fname, lname, department, jobtitle):
        # Attributes as defined in the UML [cite: 2, 3, 4, 5, 6]
        self.employee_id = str(employee_id)
        self.fname = str(fname)
        self.lname = str(lname)
        self.department = str(department)
        self.jobtitle = str(jobtitle)

    # Required methods from UML [cite: 9, 10, 11, 12, 13, 14, 15, 16, 17]
    def getId(self): return self.employee_id
    def getFirstName(self): return self.fname
    def getLastName(self): return self.lname
    def setName(self, first, last): 
        self.fname = first
        self.lname = last
    def getName(self): return f"{self.fname} {self.lname}"
    def getDepartment(self): return self.department
    def setDepartment(self, dept): self.department = dept
    def getJobTitle(self): return self.jobtitle
    def setJobTitle(self, title): self.jobtitle = title

    def __str__(self):
        # Aligned formatting for a neat directory display
        return f"{self.employee_id:<8} | {self.getName():<18} | {self.department:<15} | {self.jobtitle:<15}"


# --- PART 2: PRODUCTION WORKER SUBCLASS ---
class ProductionWorker(Employee): 
    def __init__(self, employee_id, fname, lname, department, jobtitle, shift, hourlyPayRate):
        # Initialize parent attributes [cite: 7]
        super().__init__(employee_id, fname, lname, department, jobtitle)
        # Specific attributes [cite: 20, 22]
        self.shift = int(shift)
        self.hourlyPayRate = float(hourlyPayRate)

    # Specific methods [cite: 30, 31, 32]
    def getShift(self): return self.shift
    def getRate(self): return self.hourlyPayRate
    def setShift(self, value): self.shift = int(value)

    def __str__(self):
        details = f"Shift: {self.shift} | Rate: ${self.hourlyPayRate:>6.2f}/hr"
        return f"{super().__str__()} | {details}"


# --- PART 3: SHIFT SUPERVISOR SUBCLASS ---
class ShiftSupervisor(Employee): 
    def __init__(self, employee_id, fname, lname, department, jobtitle, annualSalary, yearlybonus):
        # Initialize parent attributes [cite: 7]
        super().__init__(employee_id, fname, lname, department, jobtitle)
        # Specific attributes [cite: 21, 23]
        self.annualSalary = float(annualSalary)
        self.yearlybonus = float(yearlybonus)

    # Specific methods [cite: 33, 34, 35]
    def getSalary(self): return self.annualSalary
    def getBonus(self): return self.yearlybonus
    def setBonus(self, value): self.yearlybonus = float(value)

    def __str__(self):
        details = f"Salary: ${self.annualSalary:>9,.2f} | Bonus: ${self.yearlybonus:>8,.2f}"
        return f"{super().__str__()} | {details}"


# --- PART 4: MAIN DEMONSTRATION ---
def main():
    # Instantiate objects
    emp = Employee("E101", "Sarah", "Connor", "Admin", "Manager")
    worker = ProductionWorker("W202", "Kyle", "Reese", "Assembly", "Technician", 1, 28.50)
    supervisor = ShiftSupervisor("S303", "Ellen", "Ripley", "Logistics", "Supervisor", 85000.0, 5000.0)

    # Neat Tabular Display
    print("\n" + "="*115)
    print(f"{'EMPLOYEE MANAGEMENT SYSTEM':^115}")
    print("="*115)
    
    # Header Row
    header = f"{'ID':<8} | {'NAME':<18} | {'DEPARTMENT':<15} | {'JOB TITLE':<15} | {'PAY/BONUS DETAILS'}"
    print(header)
    print("-" * 115)

    # Print objects
    print(f"{emp} | ---")
    print(f"{worker}")
    print(f"{supervisor}")
    
    print("="*115)
    input("\nDemonstration complete. Press Enter to exit...")

if __name__ == "__main__":
    main()