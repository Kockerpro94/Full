import random, time

target_ip = "192.168.1.10"
target_port = 80
count = 0
throttle = 0.1

print(f"Simulating SYN flood on {target_ip}:{target_port}")

try:
    while True:
        src_ip = ".".join(str(random.randint(1, 254)) for _ in range(4))
        src_port = random.randint(1024, 65535)
        seq = random.randint(0, 4294967295)
        print(f"SYN packet from {src_ip}:{src_port} -> {target_ip}:{target_port} seq={seq}")
        count += 1
        if count % 10 == 0:
            print(f"Simulated {count} packets")
        time.sleep(throttle)
except KeyboardInterrupt:
    print(f"Simulation stopped after {count} packets")
