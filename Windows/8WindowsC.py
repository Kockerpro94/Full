import psutil
from datetime import datetime

boot_timestamp = psutil.boot_time()
boot_time = datetime.fromtimestamp(boot_timestamp)

print("System boot time:", boot_time.strftime("%Y-%m-%d %H:%M:%S"))
