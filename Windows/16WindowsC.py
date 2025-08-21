import subprocess

service_name = input("Enter the Windows service name (e.g., Spooler): ")

print(f"Attempting to restart the {service_name} service...")

# Stop the service
stop = subprocess.run(f'net stop {service_name}', capture_output=True, text=True, shell=True)
print(stop.stdout.strip())

# Start the service
start = subprocess.run(f'net start {service_name}', capture_output=True, text=True, shell=True)
print(start.stdout.strip())

print(f"{service_name} service restart attempt completed.")
