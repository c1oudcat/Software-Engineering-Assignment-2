import json
import os
import matplotlib.pyplot as plt

DATA_FILE = "DataFile.json"


def load_data():
    if not os.path.exists(DATA_FILE):
        print("Data file not found.")
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def summarize_by_category(data_list):
    summary = {}

    for d in data_list:
        category = d["category"]
        value = d["value"]

        if category not in summary:
            summary[category] = 0
        summary[category] += value

    return summary


def show_pie_chart(summary):
    if not summary:
        print("No data to display.")
        return

    labels = list(summary.keys())
    values = list(summary.values())

    plt.figure()
    plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
    plt.title("Value Distribution by Category")
    plt.axis("equal")
    plt.show()


def main():
    data_list = load_data()
    summary = summarize_by_category(data_list)
    show_pie_chart(summary)


if __name__ == "__main__":
    main()
