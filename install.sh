#!/bin/bash

# Cores para melhor visualização
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color
BOLD='\033[1m'

# Função para imprimir mensagens com estilo
print_step() {
    echo -e "\n${GREEN}==>${NC} ${BOLD}$1${NC}"
}

print_info() {
    echo -e "${YELLOW}INFO:${NC} $1"
}

print_error() {
    echo -e "${RED}ERRO:${NC} $1"
}

# Função para verificar se um comando existe
check_command() {
    if ! command -v $1 &> /dev/null; then
        return 1
    fi
    return 0
}

# Banner de boas-vindas
clear
echo -e "${GREEN}"
echo "======================================"
echo "      Instalador do SVTool CLI        "
echo "======================================"
echo -e "${NC}"
echo -e "Este instalador irá configurar o SVTool em seu sistema.\n"

# Detecta o sistema operacional
print_step "Verificando seu sistema..."
OS="$(uname -s)"
case "${OS}" in
    Linux*)
        print_info "Sistema Linux detectado"
        if [ -f /etc/os-release ]; then
            . /etc/os-release
            print_info "Distribuição: $NAME"
        fi
        ;;
    Darwin*)
        print_info "Sistema macOS detectado"
        print_error "Suporte para macOS está em desenvolvimento"
        exit 1
        ;;
    CYGWIN*|MINGW32*|MSYS*|MINGW*)
        print_info "Sistema Windows detectado"
        print_error "Suporte para Windows está em desenvolvimento"
        exit 1
        ;;
    *)
        print_error "Sistema operacional não suportado: ${OS}"
        exit 1
        ;;
esac

# Verifica requisitos
print_step "Verificando requisitos..."

# Python 3
if ! check_command python3; then
    print_error "Python 3 não encontrado"
    print_info "Tentando instalar Python 3..."
    
    if [ -f /etc/debian_version ]; then
        sudo apt-get update
        sudo apt-get install -y python3 python3-pip python3-venv
    elif [ -f /etc/redhat-release ]; then
        sudo dnf install -y python3 python3-pip python3-virtualenv
    else
        print_error "Não foi possível instalar Python 3 automaticamente"
        print_info "Por favor, instale Python 3 manualmente e execute este instalador novamente"
        exit 1
    fi
fi

# Verifica se a instalação do Python foi bem-sucedida
if ! check_command python3; then
    print_error "Falha ao instalar Python 3"
    exit 1
fi

print_info "Python $(python3 --version) encontrado"

# Cria ambiente virtual
print_step "Configurando ambiente virtual..."
python3 -m venv venv
source venv/bin/activate

# Instala dependências
print_step "Instalando dependências..."
pip install -r requirements.txt

# Cria link simbólico
print_step "Configurando comando 'svtool'..."
if [ -f /usr/local/bin/svtool ]; then
    sudo rm /usr/local/bin/svtool
fi
sudo ln -s "$(pwd)/svtool.sh" /usr/local/bin/svtool
chmod +x svtool.sh

# Conclusão
print_step "Instalação concluída!"
echo -e "\nPara usar o SVTool, simplesmente digite: ${GREEN}svtool${NC}"
echo -e "Se encontrar algum problema, visite: ${YELLOW}https://github.com/seu-repo/svtool${NC}\n"
