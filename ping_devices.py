import os
import platform
import datetime

def ping_device(host):
    """
    Pings a host once to check if it's reachable.
    Works on both Windows and Linux/macOS.
    """
    # -n for Windows, -c for Unix-based
    param = "-n" if platform.system().lower() == "windows" else "-c"
    # Run the ping command silently
    command = f"ping {param} 1 {host}"
    response = os.system(command + (" >nul 2>&1" if platform.system().lower() == "windows" else " >/dev/null 2>&1"))
    return response == 0

def main():
    # Timestamp for log file
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = f"ping_results_{timestamp}.txt"

    # Read host list
    try:
        with open("hosts.txt", "r") as file:
            hosts = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print("❌ hosts.txt not found! Please create one with IPs or hostnames.")
        return

    # Create and write log
    with open(log_file, "w") as log:
        log.write("Ping Test Results\n")
        log.write(f"Date: {timestamp}\n")
        log.write("="*40 + "\n")

        print("🔍 Starting ping test...\n")
        for host in hosts:
            status = "✅ Online" if ping_device(host) else "❌ Offline"
            print(f"{host} -> {status}")
            log.write(f"{host} -> {status}\n")

        print("\n📄 Results saved to:", log_file)

if __name__ == "__main__":
    main()
