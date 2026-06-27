# UCV - Laboratorio Perceptrón Simple

## 🎯 Objetivo
Implementar desde cero un perceptrón simple para resolver un problema de aprobación
de créditos y comprender el aprendizaje de una neurona artificial.

## 🏦 Caso de negocio
Un banco desea automatizar la aprobación preliminar de créditos a partir de dos
variables del cliente:

- **Ingreso mensual** (escala normalizada de 1 a 9)
- **Historial crediticio** (1 = bueno, 0 = malo)

El modelo aprende, a partir de casos históricos, a clasificar si un crédito debe
ser **aprobado (1)** o **rechazado (0)**.

## 🛠️ Herramientas
- Python 3.12
- Git / GitHub
- GitHub Actions (CI/CD)
- pytest / pytest-cov
- SonarCloud
- Visual Studio Code

## ⚙️ Instalación

```bash
git clone https://github.com/jramosalc/ucv-ate-si-laboratorio12.git
cd ucv-ate-si-laboratorio12
git checkout develop

python -m venv venv
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate

pip install -r requirements.txt
```

## ▶️ Ejecución

```bash
python main.py
```

## ✅ Pruebas

```bash
pytest -v
```

Con reporte de cobertura (igual al que usa el pipeline):

```bash
pytest --cov=src --cov-report=xml
```

## 🔄 GitHub Actions
Cada `push` o `pull request` sobre `develop` o `main` ejecuta automáticamente:
1. Instalación de dependencias
2. Ejecución de pruebas con `pytest`
3. Generación de reporte de cobertura
4. Análisis del código en SonarCloud

Puedes ver el estado del pipeline en la pestaña **Actions** del repositorio.

## 📊 SonarCloud
El análisis de calidad de código se ejecuta automáticamente vía GitHub Actions.
Resultados disponibles en: `https://sonarcloud.io/project/overview?id=jramosalc_ucv-ate-si-laboratorio12`

## ✍️ Autor
jramosalc — UCV
