#!/bin/bash

# Cores para melhor visualização
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}"
echo "======================================"
echo "    SVTool - Modo Desenvolvimento     "
echo "======================================"
echo -e "${NC}"

# Verifica Python
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Python 3 não encontrado!${NC}"
    echo -e "Para rodar em modo dev, você precisa ter Python 3 instalado."
    exit 1
fi

# Cria ambiente virtual temporário se não existir
if [ ! -d "venv" ]; then
    echo -e "\n${YELLOW}Criando ambiente virtual temporário...${NC}"
    python3 -m venv venv
fi

# Ativa o ambiente virtual
source venv/bin/activate

# Instala dependências se necessário
if [ ! -f "venv/pip-installed" ]; then
    echo -e "\n${YELLOW}Instalando dependências temporariamente...${NC}"
    pip install -r requirements.txt
    touch venv/pip-installed
fi

# Executa o SVTool
echo -e "\n${GREEN}Iniciando SVTool em modo desenvolvimento...${NC}"
echo -e "${YELLOW}Nota: Esta é uma execução temporária que não afeta seu sistema.${NC}\n"
PYTHONPATH="$(pwd)" python3 src/main.py

# Desativa o ambiente virtual
deactivate
