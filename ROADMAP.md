# 🗺️ Roadmap de Estudos & Projetos

Este documento serve como guia de desenvolvimento para popular o **cs-studies-monorepo** com projetos práticos e relevantes.

---

## 1. 🛠️ Development (`/projects`)
Foco: Engenharia de Software e construção de produtos.

### 🚀 Fullstack
- [ ] **Sistema de Chamados (Mini HelpDesk)**
    - **Stack:** SvelteKit + SQLite (ou Supabase).
    - **Objetivo:** Criar um CRUD onde usuários abrem tickets e admins respondem.
    - **Aprendizado:** Autenticação, Rotas protegidas, Banco de Dados.

### 🎨 Frontend
- [ ] **Dashboard de Monitoramento (Fake)**
    - **Stack:** HTML, TailwindCSS + Chart.js (ou apenas CSS puro).
    - **Objetivo:** Interface estática mostrando gráficos de uso de CPU/Ram.
    - **Aprendizado:** Layouts responsivos, Grid/Flexbox, UI Design.

### ⚙️ Backend
- [ ] **API Encurtadora de URL**
    - **Stack:** Node.js (Express/Fastify) ou Python (FastAPI).
    - **Objetivo:** Receber uma URL longa, salvar, e redirecionar através de um código curto.
    - **Aprendizado:** HTTP Status Codes (301, 404), Design de API REST.

### 🤖 Scripts
- [ ] **Rastreador de Preços (Web Scraper)**
    - **Stack:** Python (BeautifulSoup ou Selenium).
    - **Objetivo:** Monitorar o preço de um produto na Amazon e alertar no terminal se baixar.
    - **Aprendizado:** Automação, parsing de HTML.

---

## 2. 🛡️ Security & Infra (`/security`)
Foco: Redes, Linux e Segurança Ofensiva/Defensiva.

### 🕵️ InfoSec
- [ ] **Port Scanner (Python)**
    - **Stack:** Python (lib `socket`).
    - **Objetivo:** Script que pede um IP e verifica portas abertas (21, 22, 80, 443).
    - **Aprendizado:** TCP/IP, Sockets, Handshake.

### 🐧 Linux
- [ ] **Server Setup Script**
    - **Stack:** Bash Script (`.sh`).
    - **Objetivo:** Script que configura um servidor Ubuntu do zero (Instala Git, Docker, Configura Firewall UFW).
    - **Aprendizado:** Automação de Infra (IaC básico), Shell Scripting.

---

## 3. 🔧 IT Operations (`/it-support`)
Foco: Ferramentas úteis para o dia a dia de suporte e manutenção.

### 💻 Scripts de Suporte
- [x] **Diagnóstico e Limpeza Windows**
    - **Stack:** PowerShell (`.ps1`).
    - **Objetivo:** Limpar pastas temporárias (`%temp%`), verificar disco e listar últimos erros de log.
    - **Aprendizado:** Administração Windows, Automação de tarefas repetitivas.

### 📄 Docs (Knowledge Base)
- [x] **Guia: Reset de Spooler de Impressão**
    - **Formato:** Markdown.
    - **Objetivo:** Documentar passo a passo como resolver problemas de impressora travada.
    - **Aprendizado:** Escrita técnica e documentação.

---

## 4. 🧠 CS Core (`/cs-core`)
Foco: Fundamentos da Ciência da Computação.

### 🧮 Algoritmos
- [ ] **Corrida de Ordenação (Bubble vs Quick Sort)**
    - **Stack:** Python ou C.
    - **Objetivo:** Implementar os dois algoritmos, ordenar 10.000 números e medir o tempo de cada um.
    - **Aprendizado:** Complexidade de Algoritmos (Big O), Estrutura de Dados.

---

## 📅 Histórico de Conclusão
> Mova os itens concluídos para cá com a data de término.

* [x] Criação da estrutura do Monorepo (2025-12-29)
* [x] Script de Diagnóstico Windows e Guia de Spooler - IT Support (2025-12-29)
