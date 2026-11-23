<div align="center">

# 🛢️ PetroARX

### AI-Assisted Petrophysical Analysis & Well Log Interpretation Platform

**An Integrated Python-Based Platform for Petrophysics, Formation Evaluation, Well Log Visualization, and Subsurface Analytics.**

<br>

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![PyQt](https://img.shields.io/badge/GUI-PyQt-green)
![Petrophysics](https://img.shields.io/badge/Domain-Petrophysics-orange)
![Machine Learning](https://img.shields.io/badge/AI-Machine%20Learning-purple)
![Status](https://img.shields.io/badge/Status-Under%20Development-yellow)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows-lightgrey)

<br>

**Developed by [Md Ashraf](https://github.com/Ashraf-ISM)**

[GitHub Repository](https://github.com/Ashraf-ISM/PetroARX) · [Portfolio](https://ash-geophysics.netlify.app/)

</div>

---

## 📌 Overview

**PetroARX** is a Python-based desktop application designed to simplify and enhance petrophysical analysis and well-log interpretation through an integrated computational environment.

The platform combines conventional petrophysical evaluation techniques with interactive visualization, automated calculations, quality control, and machine-learning-assisted analytics.

It aims to provide geoscientists, petrophysicists, and subsurface engineers with a unified environment for analyzing well-log data, evaluating reservoir properties, visualizing subsurface characteristics, and exploring data-driven interpretation workflows.

Rather than relying on disconnected scripts and manual calculations, PetroARX brings multiple stages of petrophysical interpretation into a structured graphical interface.

### 🎯 Project Objectives

- Develop an integrated desktop environment for well-log analysis.
- Automate conventional petrophysical calculations.
- Improve well-log quality control and visualization.
- Facilitate reservoir characterization through formation evaluation.
- Integrate machine learning into petrophysical interpretation workflows.
- Explore missing-log prediction and data-driven subsurface analytics.
- Provide an extensible architecture for future geoscience applications.

---

## ✨ Key Features

### 1. 📂 Well Log Data Management

A centralized environment for importing and managing well-log datasets.

Capabilities include:

- LAS file loading and parsing.
- Support for additional data formats such as DLIS, CSV, and Excel.
- Well and curve data management.
- Log metadata and curve information handling.
- Structured data access for downstream analysis.

**Primary technologies:** Python, LASIO, NumPy, Pandas.

### 2. 🔍 Well Log Quality Control (QC)

Quality control is an essential step before conducting formation evaluation.

PetroARX incorporates workflows for inspecting and evaluating well-log data.

Key capabilities:

- Well-log visualization and inspection.
- Identification of missing or invalid measurements.
- Curve quality assessment.
- Log data consistency checks.
- Preparation of well-log datasets for interpretation and analytics.

### 3. 🧪 Formation Evaluation

The formation evaluation module provides computational workflows for estimating important reservoir properties from well-log measurements.

Implemented evaluation workflows include:

| Parameter | Description |
|---|---|
| Volume of Shale (Vsh) | Estimation of shale content using gamma-ray-based interpretation. |
| Effective Porosity (PHIE) | Estimation of effective formation porosity. |
| Water Saturation (Sw) | Evaluation of formation water saturation. |
| Net-to-Gross (NTG) | Estimation of net reservoir proportion. |
| Net Pay | Identification and evaluation of potentially productive reservoir intervals. |
| Reservoir Flagging | Classification of intervals based on selected reservoir criteria. |

The module is designed to support configurable interpretation workflows and visualize calculated petrophysical parameters alongside original well logs.

**Objective:** Transform raw well-log measurements into interpretable reservoir properties.

### 4. 📊 Interactive Well Log Visualization

PetroARX provides graphical tools for inspecting and visualizing well-log data.

Visualization capabilities include:

- Interactive well-log tracks.
- Multi-curve visualization.
- Depth-based log plotting.
- Petrophysical parameter visualization.
- Interactive crossplots.
- Reservoir interval inspection.

**Primary technologies:** Plotly, Matplotlib, NumPy.

### 5. 📈 Crossplot Analysis

Crossplots are important tools for understanding relationships between petrophysical measurements.

The platform includes crossplot-oriented visualization workflows for exploring relationships between well-log curves and derived parameters.

Potential applications include:

- Porosity relationships.
- Density-neutron interpretation.
- Gamma-ray versus porosity analysis.
- Reservoir characterization.
- Identification of anomalous measurements.

### 6. 🤖 AI Analytics & Machine Learning

PetroARX incorporates a dedicated AI Analytics environment to explore machine-learning applications in petrophysical interpretation.

The objective is to complement conventional interpretation with data-driven analytical methods.

Areas of development include:

- Machine-learning-assisted well-log analysis.
- Electrofacies classification workflows.
- Prediction of missing well-log measurements.
- Data-driven reservoir characterization.
- Integration of pretrained machine-learning models.

#### Missing Log Prediction

Missing or incomplete well-log measurements can affect formation evaluation and reservoir characterization.

PetroARX explores ML-based prediction workflows to estimate missing log measurements using available well-log information.

The intended workflow involves:

1. Loading well-log data.
2. Identifying missing curves or intervals.
3. Preparing available input measurements.
4. Applying compatible pretrained prediction models.
5. Generating estimated log measurements.
6. Comparing predicted and available measurements.

**Note:** Machine-learning predictions are estimates and should be validated against available measurements and geological context before being used for interpretation.

### 7. 🪨 3D Well Visualization

The repository also contains a dedicated `Well_3d` module for exploring three-dimensional well-related visualization workflows.

This provides a foundation for extending PetroARX beyond conventional two-dimensional log interpretation.

### 8. 🧰 Additional Analytical Modules

The existing repository also contains dedicated modules for:

- Facies classification.
- Geomechanics.
- ML-based quality control.
- Subsurface calculations.
- Well visualization.
- Image and asset management.

These modules contribute to the broader objective of building an integrated subsurface analysis platform.

---

## 🏗️ Project Architecture

PetroARX follows a modular organization to separate application functionality, computational workflows, visualization, and analytical components.

### Repository Structure

```text
PetroARX/
│
├── Facies_classifications/
│
├── Well_3d/
│
├── ai_analytics/
│
├── app/
│
├── assets/
│
├── borehole_image/
│
├── calculations/
│
├── controllers/
│
├── core/
│
├── data/
│
├── extra/
│
├── geomechanics/
│
├── images/
│
├── ml_qc/
│
├── plotting/
│
├── projects/
│
├── README.md
│
└── requirements.txt
```

*The structure above represents the major directories in the existing project. Individual modules may evolve as development progresses.*

### Architectural Components

| Component | Responsibility |
|---|---|
| `app/` | Main application interface and GUI components. |
| `core/` | Core application functionality. |
| `controllers/` | Application control and interaction logic. |
| `data/` | Well-log data handling and management. |
| `calculations/` | Petrophysical and subsurface calculations. |
| `plotting/` | Data visualization and plotting workflows. |
| `ai_analytics/` | Machine-learning-assisted analytical workflows. |
| `ml_qc/` | Machine-learning-related quality control. |
| `Facies_classifications/` | Facies classification workflows. |
| `Well_3d/` | Three-dimensional well visualization. |
| `geomechanics/` | Geomechanical analysis components. |
| `borehole_image/` | Borehole image-related functionality. |
| `projects/` | Project-related resources and workflows. |
| `assets/` | Application resources and assets. |
| `images/` | Image resources. |

---

## ⚙️ Technology Stack

PetroARX is developed primarily using Python and its scientific computing ecosystem.

| Technology | Application |
|---|---|
| Python | Core programming language |
| PyQt | Desktop graphical user interface |
| Qt Designer | GUI design |
| NumPy | Numerical computation |
| Pandas | Data manipulation |
| LASIO | LAS well-log file handling |
| Plotly | Interactive visualization |
| Matplotlib | Scientific plotting |
| Scikit-learn | Machine learning workflows |

Additional libraries may be used by individual modules.

---

## 🚀 Installation

### Prerequisites

- Python 3.x
- Git
- pip
- A compatible desktop environment

### 1. Clone the Repository

```bash
git clone https://github.com/Ashraf-ISM/PetroARX.git
```

### 2. Navigate to the Project Directory

```bash
cd PetroARX
```

### 3. Create a Virtual Environment

```bash
python -m venv petroarx-env
```

Activate the environment.

**Linux:**

```bash
source petroarx-env/bin/activate
```

**Windows:**

```bash
petroarx-env\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Launch the Application

The application entry point and launch command will be documented here after the startup configuration is finalized.

---

## 🔬 Typical Petrophysical Workflow

PetroARX is designed around a structured well-log interpretation workflow.

```text
          WELL LOG DATA
                │
                ▼
        DATA IMPORT & LOADING
                │
                ▼
        DATA QUALITY CONTROL
                │
                ▼
       LOG VISUALIZATION
                │
                ▼
        FORMATION EVALUATION
                │
          ┌─────┴─────┐
          ▼           ▼
      VOLUME OF    POROSITY
       SHALE       ANALYSIS
          │           │
          └─────┬─────┘
                │
                ▼
       WATER SATURATION
                │
                ▼
         NET PAY ANALYSIS
                │
                ▼
      RESERVOIR CHARACTERIZATION
                │
                ▼
       AI / ML ANALYTICS
                │
                ▼
        INTERPRETATION
```

This workflow represents the intended integrated interpretation process. Individual modules can also be used independently.

---

## 🖥️ Application Screenshots

Screenshots of the application will be added here to demonstrate its interface and functionality.

Suggested sections:

| Module | Screenshot |
|---|---|
| Main Dashboard | `assets/screenshots/dashboard.png` |
| Well Log Visualization | `assets/screenshots/well_logs.png` |
| Formation Evaluation | `assets/screenshots/formation_evaluation.png` |
| Crossplot Analysis | `assets/screenshots/crossplot.png` |
| AI Analytics | `assets/screenshots/ai_analytics.png` |
| 3D Well Visualization | `assets/screenshots/well_3d.png` |

To display a screenshot in this README, use:

```markdown
![PetroARX Dashboard](assets/screenshots/dashboard.png)
```

---

## 🛠️ Development Roadmap

PetroARX is an evolving project. Future development will focus on improving its computational capabilities, architecture, and usability.

- [x] Desktop application foundation.
- [x] Modular application components.
- [x] Well-log data handling.
- [x] Petrophysical calculation workflows.
- [x] Interactive visualization components.
- [x] AI Analytics module foundation.
- [ ] Comprehensive automated testing.
- [ ] Improved multi-well interpretation.
- [ ] Advanced missing-log prediction workflows.
- [ ] Expanded electrofacies classification.
- [ ] Enhanced 3D subsurface visualization.
- [ ] Improved reporting and export capabilities.
- [ ] Cross-platform packaging and distribution.
- [ ] Stable public release (v1.0).

*Roadmap items may change as the project develops.*

---

## 🎓 Scientific & Geoscientific Relevance

PetroARX focuses on computational applications in applied geophysics and petroleum geoscience.

Its development brings together several important areas:

- Well-log interpretation.
- Formation evaluation.
- Petrophysical modelling.
- Reservoir characterization.
- Machine learning in geoscience.
- Subsurface data visualization.
- Computational geophysics.

The broader objective is to bridge conventional petrophysical workflows with modern computational and AI-assisted approaches.

---

## 👨‍💻 Developer

**Md Ashraf**

M.Sc. (Tech.) Applied Geophysics  
Indian Institute of Technology (ISM), Dhanbad

Interested in:

- Applied Geophysics
- Petrophysics & Well Log Interpretation
- Subsurface Data Analytics
- Machine Learning in Geoscience
- Seismic Data Processing
- AI-Driven Subsurface Workflows

**Connect:**

- GitHub: [Ashraf-ISM](https://github.com/Ashraf-ISM)
- Portfolio: [ash-geophysics.netlify.app](https://ash-geophysics.netlify.app/)
- LinkedIn: [Connect with me](https://www.linkedin.com/)

---

## 🤝 Contributions

Contributions, suggestions, and discussions are welcome.

If you are interested in contributing:

1. Fork the repository.
2. Create a feature branch.
3. Implement your changes.
4. Test your implementation.
5. Submit a pull request describing your contribution.

For significant changes, consider opening an issue first to discuss the proposed implementation.

---

## 📄 License

The licensing terms for PetroARX will be finalized before its public release.

Third-party libraries, datasets, icons, and other resources remain subject to their respective licenses and usage restrictions.

---

## ⭐ Support the Project

If you find PetroARX interesting or useful for your geoscience work, consider giving the repository a star ⭐.

Feedback, suggestions, and technical discussions are always appreciated.

---

<div align="center">

### PetroARX

**Bridging Petrophysics, Computational Geoscience & Artificial Intelligence.**

*Building smarter workflows for subsurface interpretation.*

</div>
