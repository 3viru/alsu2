# 📘 Bitácora de Trabajo - Sesión de Git y GitHub CLI

## 📅 Fecha
24 de agosto de 2026

## 👤 Usuario
- **GitHub:** [3viru](https://github.com/3viru)

---

## 🎯 Objetivos de la Sesión
1. Instalar y autenticar **GitHub CLI** (`gh`) en Windows.
2. Crear, versionar y publicar el repositorio **alsu** en GitHub.
3. Crear, versionar y publicar el repositorio **alsu2** en GitHub.
4. Documentar el flujo de trabajo completo paso a paso.

---

## 🛠️ Paso a Paso Detallado

### 1. Instalación y Autenticación de GitHub CLI
Se instaló la herramienta de línea de comandos oficial de GitHub mediante `winget`:
```powershell
winget install --id GitHub.cli
```

Luego se realizó la autenticación interactiva vía navegador:
```powershell
gh auth login --web -h github.com -p https
```
- Se copió el código de un solo uso en la consola.
- Se autorizó el dispositivo en [https://github.com/login/device](https://github.com/login/device).

---

### 2. Creación del Proyecto 1: `alsu`
Flujo completo para crear y publicar el primer repositorio:

```powershell
# Crear y entrar a la carpeta
mkdir alsu
cd alsu

# Crear el archivo Markdown
Set-Content -Path "alsu.md" -Value "# Proyecto Alsu`n`nBienvenido al proyecto Alsu."

# Inicializar Git localmente
git init

# Agregar archivo al stage y hacer el primer commit
git add alsu.md
git commit -m "Initial commit with alsu.md"

# Crear el repositorio público en GitHub y subir el código
gh repo create alsu --public --source=. --remote=origin --push
```
- **Repositorio creado:** [https://github.com/3viru/alsu](https://github.com/3viru/alsu)

---

### 3. Creación del Proyecto 2: `alsu2`
Flujo completo para el segundo proyecto:

```powershell
# Crear y entrar a la carpeta
mkdir alsu2
cd alsu2

# Crear el archivo alsu2.md
Set-Content -Path "alsu2.md" -Value "# Proyecto Alsu`n`nBienvenido al proyecto Alsu2."

# Inicializar Git localmente
git init

# Preparar y confirmar cambios
git add alsu2.md
git commit -m "initial commit alsu2"

# Crear y publicar el repositorio público en GitHub
gh repo create alsu2 --public --source=. --remote=origin --push
```
- **Repositorio creado:** [https://github.com/3viru/alsu2](https://github.com/3viru/alsu2)

---

## 📋 Resumen de Comandos Principales de Git y GitHub CLI

| Comando | Descripción |
| :--- | :--- |
| `git init` | Inicializa un repositorio Git local en la carpeta actual. |
| `git status` | Muestra el estado del árbol de trabajo y archivos preparados. |
| `git add <archivo>` | Agrega archivos específicos al área de preparación (*stage*). |
| `git commit -m "<mensaje>"` | Guarda los cambios preparados en el historial con un mensaje explicativo. |
| `git push` | Sube los commits locales al repositorio remoto configurado. |
| `gh auth login` | Inicia sesión con tu cuenta de GitHub desde la terminal. |
| `gh repo create <nombre>` | Crea un nuevo repositorio en GitHub y permite vincularlo/subirlo automáticamente. |

---

✅ *Documento generado automáticamente al finalizar la sesión de trabajo.*
