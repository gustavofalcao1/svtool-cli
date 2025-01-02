# Samba AD DC Module

The Samba AD DC module in SVTool provides a simplified interface for configuring and managing a Samba Active Directory Domain Controller.

## 📋 Features

### System Preparation
- Minimum requirements verification
- System update
- Dependencies installation
- DNS and timezone configuration

### Advanced Operations
- Complete system purge
- Configuration cleanup
- Service management

## 🔧 System Requirements

### Hardware
- RAM: Minimum 2GB
- Disk: Minimum 30GB free

### Software
- Compatible Linux operating system
- Python 3.6 or higher
- Internet connection

## 💻 Usage

### Main Menu
```
╔═══════════════════════════════════════════════════════════════╗
║                  SAMBA AD DC - MANAGEMENT                     ║
╚═══════════════════════════════════════════════════════════════╝

Options Menu:
╔═══════════════════════════════════╗
║ [1] Check Requirements            ║
║ [2] Prepare System                ║
║ [3] Install Samba                 ║
║ [4] Configure Domain              ║
║ [9] Advanced Options              ║
║ [0] Back                          ║
╚═══════════════════════════════════╝
```

### System Preparation
1. Select option [1] Check Requirements
2. If requirements are met, select [2] Prepare System
3. Confirm the operation when prompted
4. Wait for the process to complete

### Advanced Options
```
╔═══════════════════════════════════╗
║         ADVANCED OPTIONS          ║
╠═══════════════════════════════════╣
║ [1] Purge Samba                   ║
║ [0] Back                         ║
╚═══════════════════════════════════╝
```

#### Purge Operation
The purge operation will:
- Stop all Samba services
- Remove all Samba packages
- Delete configuration files
- Clean system configurations

**Warning**: This operation cannot be undone. Always backup important data before proceeding.

## 🛠️ Development

### Module Structure
```
src/modules/samba_dc/
├── __init__.py
├── controller.py
├── menu.py
└── utils.py
```

### Main Components
- `controller.py`: Business logic and system operations
- `menu.py`: User interface and navigation
- `utils.py`: Helper functions

## 📝 Important Notes

### Security
- Module requires elevated privileges for some operations
- All operations are logged
- User confirmation required for critical operations

### Best Practices
- Always backup before modifying system configurations
- Check requirements before starting installation
- Follow Samba security recommendations
