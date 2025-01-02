# Frequently Asked Questions (FAQ)

Common questions and answers about SVTool.

## 📌 General Questions

### What is SVTool?
SVTool is a command-line interface (CLI) tool designed to simplify server management tasks through an intuitive menu-driven interface.

### Which operating systems are supported?
Currently, SVTool supports Linux-based operating systems including:
- Ubuntu
- Debian
- CentOS
- Other Linux distributions (may require additional configuration)

### Do I need root access?
- Basic operations don't require root access
- Some system configuration tasks require sudo privileges
- The installer will notify you when elevated privileges are needed

## 🔧 Installation Issues

### The installer fails to run
```bash
# Check file permissions
chmod +x install.sh

# Run with sudo if needed
sudo ./install.sh
```

### Python version conflicts
```bash
# Check Python version
python3 --version

# Install correct Python version
sudo apt install python3.8  # Example for Python 3.8
```

## 🛠️ Usage Problems

### Menu navigation isn't working
- Ensure your terminal supports ANSI colors
- Try running in development mode: `./run-dev.sh`
- Check terminal size (minimum 80x24 recommended)

### System preparation fails
- Verify internet connection
- Check disk space: `df -h`
- Verify RAM: `free -h`
- Look for specific error messages in logs

## 🔒 Security Concerns

### Is SVTool secure?
- Open-source and auditable code
- No data collection
- Local operation only
- Logged operations for accountability

### How are privileges handled?
- Principle of least privilege
- Explicit user confirmation for system changes
- Detailed operation logs
- Sudo only when necessary

## 🔄 Updates and Maintenance

### How to update SVTool?
```bash
# Using the built-in updater
svtool update

# Or manually
git pull
./install.sh
```

### How to backup configurations?
```bash
# Export settings
svtool export-config

# Import settings
svtool import-config
```

## 🆘 Getting Help

### Where to find logs?
```bash
# View application logs
cat ~/.svtool/logs/app.log

# View system preparation logs
cat ~/.svtool/logs/system.log
```

### How to report issues?
1. Check existing issues on GitHub
2. Gather relevant logs and system information
3. Create a detailed bug report
4. Submit through GitHub issues

### Need more help?
- Check the [documentation](../Home.md)
- Join our community forum
- Create a GitHub issue
