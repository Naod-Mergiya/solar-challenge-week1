# Solar Challenge Week 1
# EDA Project Structure

This project repository is structured to support Exploratory Data Analysis (EDA) tasks in a clean and scalable way.

---

## 📁 Folder Overview

### `.github/workflows/`
- **ci.yml/**: github actions.
  
### `.vscode/`
- **cofig: config files.

### `data/`
- **raw/**: Original datasets, unmodified.
- **processed/**: Cleaned and transformed data used for analysis.

### `notebooks/`
Jupyter notebooks used during the EDA phase:
- `01_data_loading.ipynb`: Load and inspect raw data.
- `02_data_cleaning.ipynb`: Handle missing values, outliers, and formatting.
- `03_eda_visuals.ipynb`: Generate exploratory plots and visualizations.
- `04_feature_engineering.ipynb`: Create new features for modeling.

### `src/`
Reusable Python scripts to modularize tasks:
- `data_loader.py`: Load data from source.
- `data_analyzer.py`: Data analyzer functions.
- `data_transformer.py`: Data cleaning functions.
- `visualizer.py`: Custom plotting functions.
- `utils.py`: file loading.

### `script/`

### `test/`
- Configuration files (e.g., `settings.yaml`) for paths, parameters, or environment variables.

### `venv/`
- virtual env.

### Root Files
- `requirements.txt`: List of Python dependencies.
- `README.md`: Project overview and folder structure.

---

## 🛠️ Getting Started

1. Clone the repository.
2. Create a virtual environment and install dependencies:
   ```bash
   pip install -r requirements.txt


## Environment Setup

To reproduce the environment for this project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/solar-challenge-week1.git
   cd solar-challenge-week1
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
6. Verify the setup:
   ```bash
   python --version
