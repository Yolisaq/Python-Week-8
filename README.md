# 🦠 CORD-19 Data Explorer (Memory-Safe Version)

The **CORD-19 Data Explorer** is an interactive Python application built using **Streamlit** to analyze COVID-19 research papers. This project provides researchers, students, and data enthusiasts an easy-to-use interface for exploring the vast **CORD-19 dataset**, while handling potential memory limitations of large datasets.

The app provides filtering, visualization, and text analysis features, all optimized for memory efficiency by loading a **sample of the dataset**.

---

## 📑 Table of Contents

1. [Project Overview](#project-overview)  
2. [Dataset](#dataset)  
3. [Sample Size & Insights](#sample-size--insights)  
4. [Features](#features)  
5. [Installation](#installation)  
6. [Usage](#usage)  
7. [Data Cleaning & Preprocessing](#data-cleaning--preprocessing)  
8. [Filters and Interactivity](#filters-and-interactivity)  
9. [Visualizations](#visualizations)  
10. [Memory-Safe Handling](#memory-safe-handling)  
11. [App URLs](#app-urls)  
12. [Notes & Recommendations](#notes--recommendations)  
13. [Dataset Reference](#dataset-reference)  
14. [License](#license)  

---

## 📝 Project Overview

The CORD-19 dataset is a large collection of scholarly articles related to COVID-19, SARS-CoV-2, and related coronaviruses. While this dataset contains millions of entries, this app loads a **manageable subset** to prevent memory overload, making it practical for exploratory data analysis on standard computers.

The app provides:

- 📊 Data preview and exploration  
- 🛠 Dynamic filters for years and journals  
- 📈 Publication trends over time  
- 🏆 Top journals and sources  
- ☁️ Word cloud visualization of paper titles  

This approach allows users to gain insights into COVID-19 research trends without requiring advanced computational resources.

---

## 📂 Dataset

- **Source:** [CORD-19 Kaggle Dataset](https://www.kaggle.com/datasets/allen-institute-for-ai/CORD-19-research-challenge)  
- **Original Size:** Millions of records (~1.5M papers)  
- **Columns Include:**  
  - `title` 📰 Title of the research paper  
  - `authors` ✍️ Author names  
  - `publish_time` 📅 Publication date  
  - `journal` 🏛 Journal or conference source  
  - `abstract` 📝 Abstract text  
  - `source_x` 🌐 Source type  

> ⚠️ The dataset may contain missing or inconsistent values, which are handled in the app.

---

## 🔍 Sample Size & Insights

- **Sample Loaded in App:** 10,000 rows (memory-safe)  
- **Total Papers Analyzed in Sample:** 726 papers  
- Allows users to perform **quick exploratory analysis** without memory issues.  

---

## ⚡ Features

### 1. Data Loading
- Efficiently loads a **sample of the dataset** (`metadata_sample.csv`) to prevent memory errors.  
- Automatically saves the sample for future sessions.  
- Handles missing files gracefully with user-friendly error messages.  

### 2. Data Cleaning & Preprocessing
- Converts publication dates to `datetime` format. Invalid dates are converted to `NaT`.  
- Handles missing values for key columns (`title`, `journal`, `abstract`).  
- Creates additional computed columns:  
  - `year` 🗓 extracted from `publish_time`  
  - `abstract_word_count` ✏️ to analyze text length  

### 3. Sidebar Filters
- Year range selector: Choose specific publication years.  
- Journal selector: Filter by a specific journal or choose "All".  
- Filters dynamically update the dataset preview and visualizations.

### 4. Visualizations
- **Publications by Year** 📊: Bar chart showing number of papers published per year.  
- **Top Journals** 🏆: Bar chart highlighting the top 10 journals by paper count.  
- **Word Cloud** ☁️: Visual representation of the most common words in paper titles.  
- **Source Distribution** 🌐: Top sources of the research papers.

### 5. Memory-Safe Handling
- The app avoids `MemoryError` by loading **only a sample of the full dataset**.  
- The sample is cached for subsequent runs using Streamlit’s caching feature.

---

## 💻 Installation

1. **Clone the repository**:
```bash
git clone <repository-url>
cd <repository-folder>
