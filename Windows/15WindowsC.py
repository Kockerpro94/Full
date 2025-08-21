import psutil

name = input("Enter the process name (like explorer.exe): ")

found = []
for proc in psutil.process_iter(['pid', 'name']):
    if proc.info['name'] and proc.info['name'].lower() == name.lower():
        found.append(proc.info['pid'])

if found:
    print(f"Yes, {name} is running with PID(s): {', '.join(map(str, found))}")
else:
    print(f"No, I couldn’t find {name} running right now.")
