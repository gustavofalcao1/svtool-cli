# Padrões de Interface

Este documento descreve os padrões de interface usados no SVTool para manter consistência visual em todo o projeto.

## 🎨 Elementos Visuais

### Tamanhos de Caixas e Layout

#### Banner Principal (61 caracteres)
```python
print(f"╔═══════════════════════════════════════════════════════════════╗")
print(f"║ {'TÍTULO DO BANNER':^61} ║")
print(f"╚═══════════════════════════════════════════════════════════════╝")
```

#### Menu de Opções (33 caracteres)
```python
print(f"╔═══════════════════════════════════╗")
print(f"║ [1] {'Opção do Menu':<29} ║")
print(f"║ [0] {'Voltar':<29} ║")
print(f"╚═══════════════════════════════════╝")
```

#### Menu Avançado (33 caracteres)
```python
print(f"╔═══════════════════════════════════╗")
print(f"║           {'TÍTULO DO MENU':^33} ║")
print(f"╠═══════════════════════════════════╣")
print(f"║ [1] {'Opção do Menu':<29} ║")
print(f"║ [0] {'Voltar':<29} ║")
print(f"╚═══════════════════════════════════╝")
```

### Caixas de Mensagem Adaptáveis

Use a utilidade `MessageBox` para avisos e notificações que se adaptam ao conteúdo:

```python
from src.utils.message_box import MessageBox

# Crie uma caixa de mensagem com tamanhos padrão (31-71 caracteres)
msg_box = MessageBox()

# Notificação simples
msg_box.show(
    "NOTIFICAÇÃO",
    ["Operação concluída com sucesso!"]
)

# Aviso com várias linhas
msg_box.show(
    "ATENÇÃO - LEIA COM CUIDADO",
    [
        "Esta operação irá:",
        "• Atualizar pacotes do sistema",
        "• Instalar novas dependências",
        "• Configurar serviços do sistema"
    ]
)

# Prompt de confirmação
if msg_box.prompt(
    "CONFIRMAR AÇÃO",
    ["Isso irá modificar as configurações do sistema.", "Você tem certeza?"],
    "Continuar?",
    ("s", "N")
):
    # Usuário confirmou
    pass
```

A caixa de mensagem irá ajustar automaticamente sua largura com base no conteúdo, mantendo:
- Largura mínima de 31 caracteres (tamanho do menu)
- Largura máxima de 71 caracteres (segurança do terminal)
- Largura ímpar para centralização perfeita

### Formatação de Texto

#### Títulos
- Usar `:^61` para centralizar em caixas grandes
- Exemplo: `print(f"║ {'TÍTULO':^61} ║")`

#### Opções de Menu
- Usar `:<29` para alinhar à esquerda com padding
- Exemplo: `print(f"║ [1] {'Opção':<29} ║")`

### Cores (usando colorama)
```python
from colorama import Fore, Style

# Verde para banners e menus principais
print(f"{Fore.LIGHTGREEN_EX}Menu Principal{Style.RESET_ALL}")

# Amarelo para avisos e prompts
print(f"{Fore.YELLOW}Aviso importante{Style.RESET_ALL}")

# Vermelho para erros
print(f"{Fore.RED}Erro: mensagem{Style.RESET_ALL}")
```

## 📏 Dimensões Padrão

### Tamanhos de Caixas
- Banner Principal: 61 caracteres internos
- Menus: 33 caracteres internos
- Mensagens Adaptáveis: 31-71 caracteres (auto-ajustáveis)

### Raciocínio para Tamanhos
1. **Compatibilidade de Terminal**:
   - Terminais padrão são 80 caracteres de largura
   - Nossos tamanhos deixam margens confortáveis
   - Funciona bem em sistemas modernos e legados

2. **Legibilidade de Conteúdo**:
   - 61 caracteres permitem títulos detalhados
   - 33 caracteres cabem opções de menu completas
   - Tamanhos adaptáveis para conteúdo variável

3. **Hierarquia Visual**:
   - Banner (61) aproximadamente duas vezes a largura do menu (33)
   - Cria distinção visual clara
   - Mantém design proporcional

### Regras de Alinhamento
1. Títulos sempre centralizados em suas caixas
2. Opções de menu alinhadas à esquerda
3. Alinhamento de conteúdo configurável em MessageBox

## 🔄 Adaptação de Tamanhos

Quando o texto excede os tamanhos padrão:
1. Use MessageBox para conteúdo auto-ajustável
2. Para elementos de tamanho fixo, veja [Tamanhos de Menu](../examples/menu_sizes.md)
3. Nunca exceda 71 caracteres (margem de segurança do terminal)

## 📝 Exemplos Práticos

### Banner Principal
```python
print(f"╔═══════════════════════════════════════════════════════════════╗")
print(f"║ {'SERVER MANAGEMENT HUB':^61} ║")
print(f"╚═══════════════════════════════════════════════════════════════╝")
```

### Mensagem de Atenção (Adaptável)
```python
from src.utils.message_box import MessageBox

msg_box = MessageBox()
msg_box.show(
    "ATENÇÃO - LEIA COM CUIDADO",
    [
        "Esta operação irá preparar seu sistema:",
        "• Atualização do sistema",
        "• Instalação de dependências",
        "• Configuração de serviços"
    ],
    color=Fore.YELLOW
)
```

## 🔍 Testando Layout da Interface

Para verificar seu layout:
1. Teste em terminal padrão 80x24
2. Verifique centralização com caracteres de teste temporários
3. Verifique se todas as caixas se alinham corretamente
4. Teste MessageBox com várias extensões de conteúdo

Para mais exemplos e comparações de tamanho, veja [Tamanhos de Menu](../examples/menu_sizes.md)
