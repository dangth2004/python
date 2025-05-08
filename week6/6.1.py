class Employee:
    def __init__(self, eid, name, year, basicSalary):
        self.eid = eid
        self.name = name
        self.year = year
        self.basicSalary = basicSalary

    def getSalary(self):
        return self.basicSalary

    def __str__(self):
        return f"{self.eid}, {self.name}, {self.year}, {self.getSalary():.2f}"


class Manager(Employee):
    def getSalary(self):
        return self.basicSalary + self.basicSalary * 0.25


class DataScientist(Employee):
    def __init__(self, eid, name, year, basicSalary, project):
        super().__init__(eid, name, year, basicSalary)
        self.project = project

    def getSalary(self):
        return self.basicSalary + self.basicSalary * 0.20 + self.project * 1500


class Developer(DataScientist):
    def getSalary(self):
        return self.basicSalary + self.project * 1000


def loadEmploysFromFile(filename):
    employees = []

    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    i = 0
    while i < len(lines):
        # Đọc 4 thông tin cơ bản
        eid = lines[i].strip()
        name = lines[i + 1].strip()
        year = int(lines[i + 2].strip())
        basicSalary = float(lines[i + 3].strip())

        # Xác định loại nhân viên
        if eid.startswith('E'):
            employees.append(Employee(eid, name, year, basicSalary))
            i += 4
        elif eid.startswith('M'):
            employees.append(Manager(eid, name, year, basicSalary))
            i += 4
        elif eid.startswith('DS'):
            project = int(lines[i + 4].strip())
            employees.append(DataScientist(eid, name, year, basicSalary, project))
            i += 5
        elif eid.startswith('DV'):
            project = int(lines[i + 4].strip())
            employees.append(Developer(eid, name, year, basicSalary, project))
            i += 5
        else:
            i += 4  # Bỏ qua nếu không xác định được loại

    return employees


class EmployeeManager:
    def __init__(self):
        self.employees = []

    def load_employees(self, filename):
        self.employees = loadEmploysFromFile(filename)

    def add_employee(self, employee):
        self.employees.append(employee)

    def calculate_total_salary(self):
        return sum(emp.getSalary() for emp in self.employees)

    def print_employee_list(self):
        for emp in self.employees:
            print(emp)

    def save_to_file(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            for emp in self.employees:
                file.write(f"{emp.eid}\n")
                file.write(f"{emp.name}\n")
                file.write(f"{emp.year}\n")
                file.write(f"{emp.basicSalary}\n")
                if isinstance(emp, (DataScientist, Developer)):
                    file.write(f"{emp.project}\n")
