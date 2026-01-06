import pickle

class Emp:
    def __init__(self, eid, ename, basic):
        self.eid = eid
        self.ename = ename
        self.basic = basic

# ---------------- LOAD DATA ----------------
def load_data():
    try:
        f = open("emp.txt", "rb")
        data = pickle.load(f)
        f.close()
    except:
        data = []
    return data

# ---------------- SAVE DATA ----------------
def save_data(data):
    f = open("emp.txt", "wb")
    pickle.dump(data, f)
    f.close()

# ---------------- ADD ----------------
def add_record():
    data = load_data()
    eid = int(input("Enter ID: "))
    ename = input("Enter Name: ")
    basic = float(input("Enter Salary: "))
    data.append(Emp(eid, ename, basic))
    save_data(data)
    print("Record Added")

# ---------------- SEARCH ----------------
def search_record():
    data = load_data()
    id = int(input("Enter ID to search: "))
    for e in data:
        if e.eid == id:
            print(e.eid, e.ename, e.basic)
            return
    print("Record not found")

# ---------------- DELETE ----------------
def delete_record():
    data = load_data()
    id = int(input("Enter ID to delete: "))
    for e in data:
        if e.eid == id:
            data.remove(e)
            save_data(data)
            print("Record Deleted")
            return
    print("Record not found")

# ---------------- EDIT ----------------
def edit_record():
    data = load_data()
    id = int(input("Enter ID to edit: "))
    for e in data:
        if e.eid == id:
            e.ename = input("Enter new name: ")
            e.basic = float(input("Enter new salary: "))
            save_data(data)
            print("Record Updated")
            return
    print("Record not found")

# ---------------- DISPLAY ----------------
def display_all():
    data = load_data()
    if not data:
        print("No records found")
    for e in data:
        print(e.eid, e.ename, e.basic)

# ---------------- MENU ----------------
while True:
    print("""
1. Add Record
2. Search Record
3. Delete Record
4. Edit Record
5. Display All
6. Exit
""")
    ch = int(input("Enter choice: "))

    if ch == 1:
        add_record()
    elif ch == 2:
        search_record()
    elif ch == 3:
        delete_record()
    elif ch == 4:
        edit_record()
    elif ch == 5:
        display_all()
    elif ch == 6:
        break
    else:
        print("Invalid choice")
