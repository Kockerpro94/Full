import subprocess

def manage_service(service_name, action):
    if action not in ["start", "stop", "restart"]:
        print("Invalid action. Use start, stop, or restart.")
        return
    
    if action == "restart":
        print(f"Restarting {service_name} service...")
        subprocess.run(f'net stop {service_name}', shell=True)
        subprocess.run(f'net start {service_name}', shell=True)
    else:
        print(f"{action.capitalize()}ing {service_name} service...")
        subprocess.run(f'net {action} {service_name}', shell=True)

service = input("Enter the service name (e.g., Spooler): ")
choice = input("Do you want to start, stop, or restart it? ").lower()

manage_service(service, choice)
