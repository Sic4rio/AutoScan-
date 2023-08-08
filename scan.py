import subprocess
from termcolor import colored

def display_menu():
    print(colored("User Menu:", "cyan"))
    print(colored("1.  Nmap Scan Intensive", "green"))
    print(colored("2.  Nmap Scan Quick", "green"))
    print(colored("3.  Nmap Scan All Ports Recon", "green"))
    print(colored("4.  Nmap Scan All Ports Report", "green"))
    print(colored("5.  Nmap Scan OS SYN Scan", "green"))
    print(colored("6.  Run testssl", "green"))
    print(colored("7.  Run nikto", "green"))
    print(colored("8.  Run nuclei", "green"))
    print(colored("9.  Run All Tests", "green"))
    print(colored("10. Run nslookup ", "green"))
    print(colored("11. Run dig ", "green"))
    print(colored("12. Run feroxbuster", "green"))
    print(colored("13. Run whois", "green"))
    print(colored("14. Quit", "red"))

def nmap_scan_1(host):
    command = ["nmap", "-p-", "-sV", "-sC", "Nmap-Scan-1", host]
    subprocess.run(command)

def nmap_scan_2(host):
    command = ["nmap",  "Nmap-Scan-2", host]
    subprocess.run(command)

def nmap_scan_3(host):
    command = ["nmap", "-p-", "-sV", "-sC",  "Nmap-Scan-3", host]
    subprocess.run(command)

def nmap_scan_4(host):
    command = ["nmap", "-p-", "-oX", "Nmap-Scan-4", host]
    subprocess.run(command)

def nmap_scan_5(host):
    command = ["nmap", "-p-", "-oX", "Nmap-Scan-5", host]
    subprocess.run(command)

def run_testssl(host):
    command = ["testssl", "-oH", "SSL-Test.html", host]
    subprocess.run(command)

def run_nikto(host):
    command = ["nikto", "-url", host]
    subprocess.run(command)

def run_nuclei(host):
    command = ["nuclei", "-u", host]
    subprocess.run(command)

def nslookup(host):
    command = ["nslookup", host]
    subprocess.run(command)

def dig(host):
    command = ["dig", host]
    subprocess.run(command)

def feroxbuster(host):
    command = ["feroxbuster", "--url", host]
    subprocess.run(command)

def whois(host):
    command = ["whois", host]
    subprocess.run(command)

# Banner
banner = colored("""
⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣶⣶⣿⣿⣿⣿⣿⣷⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣶⡿⠿⢿⣿⣶⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠞⠋⠉⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣷⣄⠀⠀⠀⠀⠀
⠀⠀⠀⣠⣾⣿⣿⣿⣿⠿⠛⠉⠁⠀⠀⠀⠀⠉⠙⠻⢿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣶⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣷⣄⠀⠀⠀
⠀⠀⣼⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣷⡀⠀⠀⠀⢀⣶⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣧⠀⠀
⠀⣼⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣄⠀⠀⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣧⠀
⢸⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⢂⣾⣿⣿⣿⠿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡄
⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀SICARIO⠀23.⠀⠀⠀⠀⠀⠀⠀⢻⡿⢡⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⡇
⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣱⣿⣿⣿⡿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⡇
⢿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⡟⣴⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡇
⠸⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⠏⢸⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⠁
⠀⢻⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⡿⠃⠀⠀⠹⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⠃⠀
⠀⠀⠹⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⠟⠁⠀⠀⠀⠀⠈⢻⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⡿⠃⠀⠀
⠀⠀⠀⠈⠻⣿⣿⣿⣿⣶⣤⣀⣀⠀⠀⠀⣀⣀⣤⣶⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣶⣤⣀⣀⠀⠀⠀⢀⣀⣤⣶⣿⣿⣿⣿⠟⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⠿⠿⠿⠿⠿⠟⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⢿⣿⣿⣿⠿⠿⠟⠋⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  
""", "yellow")

# Main program
host = input(colored("Enter the target IP or domain: ", "cyan"))

print(banner)

while True:
    display_menu()
    choice = input(colored("Enter your choice (1-14): ", "cyan"))

    if choice == '1':
        nmap_scan_1(host)
    elif choice == '2':
        nmap_scan_2(host)
    elif choice == '3':
        nmap_scan_3(host)
    elif choice == '4':
        nmap_scan_4(host)
    elif choice == '5':
        nmap_scan_5(host)
    elif choice == '6':
        run_testssl(host)
    elif choice == '7':
        run_nikto(host)
    elif choice == '8':
        run_nuclei(host)
    elif choice == '9':
        selected_checks = ['2', '3', '6', '7', '8', '9', '10', '11', '12', '13']
        for check in selected_checks:
            if check == '2':
                nmap_scan_2(host)
            elif check == '3':
                nmap_scan_3(host)
            elif check == '6':
                run_testssl(host)
            elif check == '7':
                run_nikto(host)
            elif check == '8':
                run_nuclei(host)
            elif check == '9':
                perform_all_scans(host)
            elif check == '10':
                nslookup(host)
            elif check == '11':
                dig(host)
            elif check == '12':
                feroxbuster(host)
            elif check == '13':
                whois(host)
    elif choice == '10':
        nslookup(host)
    elif choice == '11':
        dig(host)
    elif choice == '12':
        feroxbuster(host)
    elif choice == '13':
        whois(host)
    elif choice == '14':
        print(colored("Quitting the program...", "red"))
        break
    else:
        print(colored("Invalid choice. Please enter a valid option (1-14).", "yellow"))

    input(colored("Press Enter to continue...", "cyan"))
