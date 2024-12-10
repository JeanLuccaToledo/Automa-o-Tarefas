### **Automação de Arquivos**

O **Projeto de Automação de Arquivos** é uma ferramenta desenvolvida em Python com o objetivo de facilitar a organização e a manipulação de arquivos em um diretório. Ele oferece uma interface gráfica intuitiva para executar diferentes tarefas relacionadas à gestão de arquivos, como renomeação em massa, organização por extensão ou data de modificação. 

Essa solução é útil para quem lida com grandes volumes de arquivos e precisa automatizar tarefas repetitivas, otimizando o tempo e garantindo uma organização consistente.

---

### **Funcionalidades**
1. **Renomeação de Arquivos**:
   - Renomeia todos os arquivos de um diretório com um padrão especificado pelo usuário.
   - Permite definir uma extensão-alvo (ex.: `.txt`, `.png`).
   - Exemplo: Arquivos como `documento1.txt` e `documento2.txt` podem ser renomeados para `novo_nome_1.txt` e `novo_nome_2.txt`.

2. **Organização por Extensão**:
   - Agrupa arquivos com base em suas extensões em subpastas específicas.
   - Exemplo: Todos os arquivos `.jpg` são movidos para uma pasta chamada `jpg`, e arquivos `.pdf` para uma pasta `pdf`.

3. **Organização por Data**:
   - Classifica os arquivos em subpastas baseadas no mês e ano da última modificação.
   - Exemplo: Arquivos modificados em dezembro de 2024 serão movidos para uma pasta chamada `2024-12`.

---

### **Tecnologias Utilizadas**
- **Python**: Linguagem de programação principal do projeto.
- **Tkinter**: Biblioteca padrão para a criação da interface gráfica.
- **Pathlib**: Para manipulação e navegação nos arquivos do sistema.
- **Datetime**: Para trabalhar com datas de modificação dos arquivos.

---

### **Público-Alvo**
Este projeto é voltado para:
- Usuários que lidam com grandes volumes de arquivos.
- Profissionais que precisam de uma organização automatizada em pastas.
- Estudantes e desenvolvedores que buscam aprender e explorar Python em um projeto prático.

---

### **Motivação**
A organização manual de arquivos pode ser trabalhosa e propensa a erros. Este projeto oferece uma solução prática e automatizada, demonstrando o uso de Python para resolver problemas do cotidiano. Além disso, o projeto é modular, o que facilita sua manutenção e expansão.

---

### **Estrutura do Projeto**
Projeto2/<br>
├── main.py          # Arquivo principal<br>
├── renomear.py      # Script para renomear arquivos<br>
└── organizar.py     # Script para organizar arquivos<br>
