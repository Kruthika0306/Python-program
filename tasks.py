tasks = []

print("To-Do List App")

while True:
    task = input("Enter a task (or 'done' to stop): ")

    if task == "done":
        break

    tasks.append(task)

print("\nYour Tasks:")
for t in tasks:
    print("-", t)