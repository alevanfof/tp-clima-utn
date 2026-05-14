# TP CLIMA – UTN  
**Tecnicatura Universitaria en Programación (TUP) – Modalidad a Distancia**  
**Cátedra: Organización Empresarial**  
**Año Lectivo: 2026**

---

## 📌 Integrantes del equipo
- **Alejandro Fernández** – P1 Líder y Organizador  
- **Gabriel** – P2 Desarrollador Técnico  
- **Josue** – P3 Revisor y QA  

---

## 🎯 Escenario elegido
**Escenario A – Análisis de Datos Climáticos**  
El equipo desarrollará un script que procese datos meteorológicos históricos de una ciudad, utilizando datasets abiertos de temperatura global.

---

## 📂 Estructura del repositorio
repo-proyecto/
├── datos/
│   └── global-temp.csv
├── scripts/
│   └── analisis_clima.py
├── resultados/
│   └── grafico_temperatura.png
├── README.md
└── .gitignore


---

## 📊 Dataset utilizado
Se emplea el dataset abierto de temperaturas globales:  
**Fuente:** [Global Temperature Data – datahub.io/core/global-temp](https://datahub.io/core/global-temp)  
- Registros históricos de temperatura promedio global.  
- Formato CSV.  
- Datos provenientes del análisis climático GISTEMP.  

El archivo se almacenará en la carpeta `/datos`.

---

## ⚙️ Instrucciones de ejecución
1. Clonar el repositorio:  
   ```bash
   git clone https://github.com/alevanfof/tp-clima-utn.git
   cd tp-clima-utn

📜 Normas de trazabilidad
Cada commit debe iniciar con el ID del Issue de Jira correspondiente.
Ejemplo:

Código
PROY-2: Desarrollo del análisis climático
Todo cambio debe realizarse en ramas específicas y luego integrarse mediante Pull Requests revisados por el QA.

✅ Buenas prácticas
No exponer tokens ni credenciales en el repositorio.

Usar .gitignore para excluir archivos temporales y sensibles.
Documentar el código con comentarios técnicos claros.
Mantener reproducibilidad en Google Colab utilizando rutas relativas.