# 🏋️ Sistema de Gestão de Alunos - Personal

Sistema para gerenciamento de alunos de personal trainer, com controle de treinos, frequência e mensalidades.

## 📌 Funcionalidades

- **Cadastro de Alunos**
  - Registro com nome, dias de treino e valor por aula
  - Validação de dados integrada
- **Controle de Frequência**
  - Registro automático de aulas por mês
  - Histórico completo de treinos
- **Cálculo Financeiro**
  - Geração de valores com base na frequência
- **Armazenamento Seguro**
  - Dados salvos em arquivo JSON

## ⚙️ Tecnologias Utilizadas

- Python 3.x
- Módulos padrão: `json`, `os`, `calendar`
- Armazenamento: Arquivo JSON local

## 🚀 Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/sistema-academia.git
   ```

2. Execute o programa principal:
   ```bash
   python main.py
   ```

## 📋 Estrutura do Código

```plaintext
sistema-academia/
│
├── sistema.py            # Programa principal
├─── modulos.py            # Recursos implementados
├── alunos.json           # Banco de dados (gerado automaticamente)
├── README.md             # Este arquivo
```

## 📊 Exemplo de Uso

```python
# Cadastrar novo aluno
>>> cadastraraluno(alunos)
Nome do(a) aluno(a): Maria Silva
Treina na Segunda? [S/N]: S
Valor hora/aula: R$ 80,50
✅ Maria Silva cadastrada com sucesso!
```

## 🤝 Como Contribuir

1. Faça um fork do projeto
2. Crie uma branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Add nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

---
