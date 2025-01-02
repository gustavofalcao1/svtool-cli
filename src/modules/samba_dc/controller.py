import os
import subprocess
from colorama import Fore, Style

class SambaDCController:
    def __init__(self):
        self.packages = [
            'acl',
            'attr',
            'autoconf',
            'bind9-utils',
            'bison',
            'build-essential',
            'debconf-utils',
            'dnsutils',
            'docbook-xml',
            'docbook-xsl',
            'flex',
            'gdb',
            'krb5-user',
            'libacl1-dev',
            'libaio-dev',
            'libarchive-dev',
            'libattr1-dev',
            'libblkid-dev',
            'libbsd-dev',
            'libcap-dev',
            'libcups2-dev',
            'libgnutls28-dev',
            'libgpgme11-dev',
            'libjson-perl',
            'libldap2-dev',
            'libncurses5-dev',
            'libpam0g-dev',
            'libparse-yapp-perl',
            'libpopt-dev',
            'libreadline-dev',
            'perl',
            'perl-modules',
            'pkg-config',
            'python3-all-dev',
            'python3-crypto',
            'python3-dbg',
            'python3-dev',
            'python3-dnspython',
            'python3-gpg',
            'python3-markdown',
            'xsltproc',
            'zlib1g-dev'
        ]

    def check_system_requirements(self):
        """Check minimum system requirements"""
        print(f"\n{Fore.YELLOW}Checking system requirements...{Style.RESET_ALL}")
        
        # Check disk space
        df = subprocess.check_output(['df', '-h', '/']).decode()
        available = int(df.split()[-3].replace('G', ''))
        if available < 10:  # Minimum 10GB free
            return False, "Insufficient disk space (minimum 10GB)"
        
        # Check RAM
        with open('/proc/meminfo') as f:
            mem = int(f.readline().split()[1]) / 1024 / 1024  # Convert to GB
            if mem < 2:  # Minimum 2GB RAM
                return False, "Insufficient RAM (minimum 2GB)"
        
        return True, "System meets minimum requirements"

    def prepare_system(self):
        """Prepare system for Samba AD DC installation"""
        try:
            print(f"\n{Fore.GREEN}Preparing system for Samba AD DC...{Style.RESET_ALL}")
            
            # Update system
            print(f"\n{Fore.YELLOW}Updating system...{Style.RESET_ALL}")
            subprocess.run(['sudo', 'apt-get', 'update'], check=True)
            subprocess.run(['sudo', 'apt-get', 'upgrade', '-y'], check=True)
            
            # Install dependencies
            print(f"\n{Fore.YELLOW}Installing dependencies...{Style.RESET_ALL}")
            subprocess.run(['sudo', 'apt-get', 'install', '-y'] + self.packages, check=True)
            
            # Configure timezone
            print(f"\n{Fore.YELLOW}Configuring timezone...{Style.RESET_ALL}")
            subprocess.run(['sudo', 'timedatectl', 'set-timezone', 'America/Sao_Paulo'], check=True)
            
            # Disable systemd-resolved
            print(f"\n{Fore.YELLOW}Configuring DNS...{Style.RESET_ALL}")
            subprocess.run(['sudo', 'systemctl', 'disable', '--now', 'systemd-resolved'], check=True)
            
            # Backup and remove existing resolv.conf
            if os.path.exists('/etc/resolv.conf'):
                subprocess.run(['sudo', 'mv', '/etc/resolv.conf', '/etc/resolv.conf.bak'], check=True)
            
            return True, "System prepared successfully"
            
        except subprocess.CalledProcessError as e:
            return False, f"Error preparing system: {str(e)}"
        except Exception as e:
            return False, f"Unexpected error: {str(e)}"

    def purge_samba(self):
        """Completely remove Samba and all its configurations"""
        try:
            print(f"\n{Fore.YELLOW}Removing Samba packages and configurations...{Style.RESET_ALL}")
            
            # Stop Samba services
            subprocess.run(['sudo', 'systemctl', 'stop', 'smbd', 'nmbd', 'winbind'], check=False)
            subprocess.run(['sudo', 'systemctl', 'disable', 'smbd', 'nmbd', 'winbind'], check=False)
            
            # Remove Samba packages
            subprocess.run(['sudo', 'apt-get', 'purge', '-y', 'samba*', 'winbind'], check=True)
            subprocess.run(['sudo', 'apt-get', 'autoremove', '-y'], check=True)
            
            # Remove configuration directories
            subprocess.run(['sudo', 'rm', '-rf', '/etc/samba'], check=True)
            subprocess.run(['sudo', 'rm', '-rf', '/var/lib/samba'], check=True)
            subprocess.run(['sudo', 'rm', '-rf', '/var/cache/samba'], check=True)
            subprocess.run(['sudo', 'rm', '-rf', '/var/log/samba'], check=True)
            
            # Clean system configurations
            subprocess.run(['sudo', 'systemctl', 'daemon-reload'], check=True)
            
            return True, "Samba has been completely removed from the system"
            
        except subprocess.CalledProcessError as e:
            return False, f"Error purging Samba: {str(e)}"
        except Exception as e:
            return False, f"Unexpected error: {str(e)}"
