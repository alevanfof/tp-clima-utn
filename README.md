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

## 📜 Normas de trazabilidad
Cada commit debe iniciar con el ID del Issue de Jira correspondiente.  
Ejemplo:  

### Inicialización del repositorio (Issue PROY‑1 – Ale)
```bash
git add .
git commit -m "PROY-1: Inicialización de estructura de carpetas y README"
git push origin main

### Desarrollo del análisis (Issue PROY‑2 – Gabriel)
bash
git add scripts/analisis_clima.py
git commit -m "PROY-2: Desarrollo del análisis climático"
git push origin feature/analisis-clima

### Revisión y documentación (Issue PROY‑3 – Josue)
bash
git add README.md
git commit -m "PROY-3: Mejora de documentación y revisión QA"
git push origin main

---

### 🔎 Convención de nombres de ramas (feature sugerida)
En Git, las ramas se nombran con convenciones que ayudan a organizar el trabajo.  
La convención más usada es **prefix/nombre-tarea**, por ejemplo:  
- `feature/analisis-clima` → rama para desarrollar una nueva funcionalidad (el análisis climático).  
- `bugfix/correccion-lectura` → rama para corregir un error.  
- `hotfix/token-seguridad` → rama para un arreglo urgente.  

👉 En este TP, la rama **sugerida para Gabriel** es `feature/analisis-clima`, ya que corresponde a su rol de desarrollador técnico.  

---

### 🧩 Práctica sugerida para crear ramas
La práctica más actual es usar el comando:  
```bash
git checkout -c feature/analisis-clima

✅ Buenas prácticas
No exponer tokens ni credenciales en el repositorio.

Usar .gitignore para excluir archivos temporales y sensibles.
Documentar el código con comentarios técnicos claros.
Mantener reproducibilidad en Google Colab utilizando rutas relativas.

### Buenas prácticas de commits
Cada commit debe describir exhaustivamente los cambios realizados, no solo un título genérico.

Se recomienda hacer commits frecuentes y pequeños, ya que esto permite:

Mayor trazabilidad del trabajo.

Posibilidad de hacer rollback en puntos más precisos cuando ocurre un error.

Mejor revisión por parte del QA.

Evidenciar la secuencia de pasos del desarrollo en el historial de GitHub.

Seguidos y descriptivos, para facilitar encontrarlos al hacer rollback.  
Ejemplo de mensaje de commit:

bash
git commit -m "PROY-1: Agrego prácticas de commit sugeridas en README, para trazabilidad de rollback en caso de incidentes"