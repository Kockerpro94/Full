import psutil
import getpass

username = input("Enter the username whose processes you want to terminate: ")

killed = []
failed = []

for proc in psutil.process_iter(['pid', 'name', 'username']):
    try:
        if proc.info['username'] and proc.info['username'].lower() == username.lower():
            proc.kill()
            killed.append((proc.info['pid'], proc.info['name']))
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        failed.append((proc.info['pid'], proc.info['name']))

print("\n🔎 Scan complete.")
if killed:
    print(f"✅ Terminated {len(killed)} process(es) for user '{username}':")
    for pid, name in killed:
        print(f"   • {name} (PID {pid})")
else:
    print(f"⚠️ No processes found for user '{username}'.")

if failed:
    print(f"\n⚠️ Could not terminate {len(failed)} process(es) due to permission issues.")
