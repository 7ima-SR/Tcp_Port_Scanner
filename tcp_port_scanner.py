import socket
import argparse
import time
import termcolor
import pyfiglet
import sys

print(termcolor.colored(pyfiglet.figlet_format("TCP Port Scanner"), "red"))
print(termcolor.colored("Powered by Hima", "yellow"))

parser = argparse.ArgumentParser(description="TCP Port Scanner")
parser.add_argument('-t', '--target', help='Target IP address', required=True)
parser.add_argument('-p', '--ports', help='Ports range (e.g., 20-80)', default='1-1024')
parser.add_argument('-T', '--timeout', type=int, default=1, help='Socket timeout in seconds')
parser.add_argument('-o', '--output', help='Output file to save results', default= 'results_tcp_scanner.txt')

args = parser.parse_args()
target = args.target

ports_to_scan = []
if ',' in args.ports:
    ports_to_scan = [int(p.strip()) for p in args.ports.split(',')]
elif '-' in args.ports:
    start_port, end_port = map(int, args.ports.split('-'))
    ports_to_scan = list(range(start_port, end_port +1))
else:
    ports_to_scan = [int(args.ports)]

start_time = time.time()

print(f"[+] Scanning Target: {target}")
print(f"[+] Scanning ports: {start_port} to {end_port}")

def fake_progress():
    for i in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.3)
    print()

print("[*] Initializing scan", end="")
fake_progress()

open_ports = []

try:
    for port in ports_to_scan:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(args.timeout)
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "Unknown"
                print(termcolor.colored(f"[+] Port {port} is open, service: {service}", "green"))
            else:
                pass

except KeyboardInterrupt:
    print("\n[-] Scan interrupted by user")
except socket.gaierror:
    print(f"[-] Could not resolve {target}")
except socket.error:
    print(f"[-] Could not connect to {target}")

end_time = time.time()
total_time = end_time - start_time
print(termcolor.colored(f"\n[✓] Scan completed in {total_time:.2f} seconds", "cyan"))

if args.output:
    with open(args.output, 'w') as f:
        f.write(f"Scan result for {target}:\n")
        for port in open_ports:
            f.write(f"Port {port} is open\n")

    print(f"Results saved to {args.output}")