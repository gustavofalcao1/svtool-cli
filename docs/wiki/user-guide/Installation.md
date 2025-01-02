# Installation Guide

This guide provides detailed instructions for installing SVTool in different environments.

## 📋 Prerequisites

Before installing, ensure your system meets these requirements:

### Hardware Requirements
- RAM: Minimum 2GB
- Disk Space: Minimum 30GB free

### Software Requirements
- Linux Operating System (Ubuntu, Debian, CentOS, etc.)
- Python 3.6 or higher
- Internet connection (for installation only)

## 🚀 Installation Methods

### 1. Development Mode (No Installation)

For testing or development purposes:

```bash
git clone https://github.com/your-repo/svtool.git
cd svtool
chmod +x run-dev.sh
./run-dev.sh
```

### 2. Quick Installation

For production environments:

```bash
wget -qO- https://raw.githubusercontent.com/your-repo/svtool/main/quick-install.sh | bash
```

### 3. Manual Installation

Step by step installation:

1. Clone the repository:
```bash
git clone https://github.com/your-repo/svtool.git
cd svtool
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the installer:
```bash
./install.sh
```

## 🔧 Post-Installation

After installation:

1. Verify installation:
```bash
svtool --version
```

2. Check system compatibility:
```bash
svtool check-system
```

## 🆙 Updating SVTool

To update to the latest version:

```bash
svtool update
```

## 🗑️ Uninstallation

If you need to remove SVTool:

```bash
svtool uninstall
```

## 🔍 Troubleshooting

### Common Issues

1. Permission Errors
```bash
sudo chmod +x install.sh
sudo ./install.sh
```

2. Python Version Issues
```bash
python3 --version  # Check Python version
```

3. Dependency Issues
```bash
pip install --upgrade -r requirements.txt
```

For more issues, check our [FAQ](FAQ.md)
