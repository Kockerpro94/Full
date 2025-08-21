import platform
import psutil

# Get CPU name
cpu_name = platform.processor()

# Get number of physical cores
physical_cores = psutil.cpu_count(logical=False)

# Get number of logical cores (includes hyper-threading)
logical_cores = psutil.cpu_count(logical=True)

print(f"CPU Name: {cpu_name}")
print(f"Physical Cores: {physical_cores}")
print(f"Logical Cores: {logical_cores}")