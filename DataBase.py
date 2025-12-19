import json
import os
import uuid

DATA_FILE = "DataFile.json"


# ---------- 基礎 I/O ----------

def load_data():
    """讀取所有資料"""
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def save_data(data_list):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data_list, f, indent=4, ensure_ascii=False)


# ---------- 新增資料 ----------

def add_data(date, value, category):
    data_list = load_data()

    data = {
        "id": str(uuid.uuid4()),
        "date": date,
        "category": category,
        "value": float(value),
    }

    data_list.append(data)
    save_data(data_list)
    print("Data added successfully.")


# ---------- 修改資料 ----------

def update_data(data_id, date=None, value=None):
    data_list = load_data()

    for d in data_list:
        if d["id"] == data_id:
            if date is not None:
                d["date"] = date
            if value is not None:
                d["value"] = float(value)

            save_data(data_list)
            print("Data updated successfully.")
            return

    print("Data ID not found.")


# ---------- 刪除資料 ----------

def delete_data(data_id):
    data_list = load_data()
    new_data_list = [d for d in data_list if d["id"] != data_id]

    if len(data_list) == len(new_data_list):
        print("Data ID not found.")
        return

    save_data(new_data_list)
    print("Data deleted successfully.")


# ---------- 查詢資料 ----------

def list_data():
    data_list = load_data()

    if not data_list:
        print("No data found.")
        return

    for d in data_list:
        print(
            f"ID: {d['id']}\n"
            f"Date: {d['date']}\n"
            f"Category: {d['category']}\n"
            f"Value: {d['value']}\n"
        )


# ---------- main（主程式） ----------

def main():
    while True:
        print("\nData Manager")
        print("1. Add data")
        print("2. List data")
        print("3. Update data")
        print("4. Delete data")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            date = input("Date (YYYY-MM-DD): ")
            category = input("Category: ")
            value = input("Value: ")
            add_data(date, value, category)

        elif choice == "2":
            print("\nThe data list：")
            list_data()

        elif choice == "3":
            data_id = int(input("Data ID to update: "))
            date = input("New date (leave blank to keep): ")
            value = input("New value (leave blank to keep): ")

            update_data(
                data_id,
                date if date else None,
                value if value else None
            )

        elif choice == "4":
            data_id = int(input("Data ID to delete: "))
            delete_data(data_id)

        elif choice == "5":
            print("Bye.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
