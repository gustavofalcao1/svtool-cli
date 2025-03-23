# SVTool CLI - Server Script Hub

**SVTool** is a simple yet powerful command-line tool designed to manage Linux servers through a friendly and modular interface.

## 🚀 Getting Started

### Run Without Installing

Want to try SVTool without installing it system-wide? Simply run:

```bash
chmod +x run-dev.sh
./run-dev.sh
```

This will launch SVTool in development mode without making permanent changes to your system.

### One-Line Installation

Install SVTool with a single command:

```bash
wget -qO- https://raw.githubusercontent.com/gustavofalcao1/svtool-cli/main/quick-install.sh | bash
```

### Manual Installation

Prefer to install manually?

1. Clone the repository:

```bash
git clone https://github.com/gustavofalcao1/svtool-cli.git
cd svtool-cli
```

2. Run the installer:

```bash
./install.sh
```

## 📚 Documentation

Full documentation is available in the [Wiki](docs/wiki/Home.md), including:

- [Quick Start Guide](docs/wiki/user-guide/QuickStart.md)
- [Development Guide](docs/wiki/dev-guide/Development.md)
- [UI Standards](docs/wiki/dev-guide/UIStandards.md)
- [Available Modules](docs/wiki/user-guide/Modules.md)

## 🛠️ Features

- **Samba AD DC Module**: Configure and manage domain controllers with ease
- More modules coming soon!

## ⚙️ Requirements

- Linux-based OS (Ubuntu, Debian, CentOS, etc.)
- Python 3.6+
- Internet connection (required for installation only)

## 🤝 Contributing

Contributions are welcome! Please refer to the [Contributing Guide](docs/wiki/dev-guide/Contributing.md) to get started.

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

