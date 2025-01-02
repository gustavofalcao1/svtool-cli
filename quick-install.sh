#!/bin/bash

# Cores para melhor visualização
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}"
echo "======================================"
echo "    Instalador Rápido do SVTool CLI   "
echo "======================================"
echo -e "${NC}"

# Verifica se git está instalado
if ! command -v git &> /dev/null; then
    echo -e "${YELLOW}Instalando git...${NC}"
    if [ -f /etc/debian_version ]; then
        sudo apt-get update
        sudo apt-get install -y git
    elif [ -f /etc/redhat-release ]; then
        sudo dnf install -y git
    else
        echo -e "${RED}Não foi possível instalar git automaticamente${NC}"
        echo "Por favor, instale git manualmente e tente novamente"
        exit 1
    fi
fi

# Cria diretório temporário
TMP_DIR=$(mktemp -d)
cd $TMP_DIR

# Clona o repositório
echo -e "\n${GREEN}==> ${NC}Baixando SVTool..."
git clone https://github.com/seu-repo/svtool.git
cd svtool

# Executa o instalador
echo -e "\n${GREEN}==> ${NC}Iniciando instalação..."
chmod +x install.sh
./install.sh

# Limpa arquivos temporários
cd ..
rm -rf $TMP_DIR
