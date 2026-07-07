"""Main entrypoint for networking tools."""

from __future__ import annotations

import argparse
import json
import os
import socket
import sys
import urllib.error
import urllib.parse
import urllib.request


def run(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Networking Tools CLI")
    parser.add_argument("--version", action="store_true", help="Show package version")
    args = parser.parse_args(argv)

    if args.version:
        print("networking-tools 0.1.0")
        return 0

    print("Networking Tools starter package")
    return 0


def ip_config():
    os.system("ipconfig" if os.name == "nt" else "ifconfig")
    

def ping():
    host = input("Enter host (e.g google.com): ").strip()
    if host:
        os.system(f"ping {host}")
    else:
        print("No host entered.")


def traceroute():
    host = input("Enter host (e.g google.com): ").strip()
    if host:
        os.system(f"tracert {host}")
    else:
        print("No host entered.")


def nslookup():
    domain = input("Enter domain: ").strip()
    if domain:
        os.system(f"nslookup {domain}")
    else:
        print("No domain entered.")


def iplookup():
    target = input("Enter domain or IP: ").strip()
    if not target:
        print("No target entered.")
        return

    url = f"http://ip-api.com/json/{urllib.parse.quote(target)}"
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            if response.status != 200:
                print("IP Lookup failed with status:", response.status)
                return
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.URLError as exc:
        print("Network error during IP lookup:", exc)
        return
    except json.JSONDecodeError:
        print("Unable to parse IP lookup response.")
        return

    if data.get("status") != "success":
        print("IP lookup failed:", data.get("message", "Unknown error"))
        return  

    print("\n--- IP INFORMATION ---")
    print("IP:", data.get("query"))
    print("Country:", data.get("country"))
    print("Region:", data.get("regionName"))
    print("City:", data.get("city"))
    print("ISP:", data.get("isp"))


def port_checker():
    host = input("Enter host (e.g google.com): ").strip()
    if not host:
        print("No host entered.")
        return

    try:
        port = int(input("Enter port (e.g 80): ").strip())
    except ValueError:
        print("Invalid port number.")
        return

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        result = s.connect_ex((host, port))
    except socket.gaierror as exc:
        print("Host lookup failed:", exc)
        return
    finally:
        s.close()

    if result == 0:
        print(f"Port {port} is open on {host}.")
    else:
        print(f"Port {port} is closed on {host}.")


def interactive_menu():
    while True:
        print("\n--- Networking Tools ---")
        print("1. Ip Config")
        print("2. Ping")
        print("3. Traceroute")
        print("4. NSLookup")
        print("5. IP Lookup")
        print("6. Port Checker")
        print("7. Exit")

        choice = input("Select an option: ").strip()
        if choice == "1":
            ip_config()
        elif choice == "2":
            ping()
        elif choice == "3":
            traceroute()
        elif choice == "4":
            nslookup()
        elif choice == "5":
            iplookup()
        elif choice == "6":
            port_checker()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    interactive_menu()  
