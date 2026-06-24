# Academic Projects Portfolio

A curated collection of projects developed during my university studies, covering basic web development tasks and foundational machine learning techniques.

---

## 📂 Repository Structure

The repository contains two main parts:
1. **University Web Project:** A basic website made for a class credit, focusing on forms and database connection.
2. **Machine Learning Tasks:** Implementation and evaluation of predictive models.

---

## 🌐 1. University Web Project (HTML, CSS, PHP, MySQLi, JS)

A simple website created as a standard laboratory assignment to pass a university course. It covers the basics of handling user inputs and connecting a frontend form to a backend script.

### ⚠️ Security & Code Disclaimer
> **Important:** This is a legacy student assignment meant for local testing only. It uses basic procedural PHP and is **vulnerable to SQL Injection** because variables are inserted directly into SQL queries. It is left as-is to show my historical progress.

### What is inside:
*   **Form Handling (`index.html`, `osoby.php`):** Sends data from an HTML form to a PHP script, which connects to a local MySQL database via `mysqli`.
*   **Simple Cart (`sklep.html`, `koszyk.php`):** A basic calculator that takes item quantities from a form and computes prices using simple math in PHP.
*   **JavaScript Additions:** Tiny scripts for displaying a live clock and calculating days.

### Known Issues & What I Learned:
*   **Security:** The project lacks input sanitization. In a real-world app, I would use PDO with Prepared Statements to prevent SQL Injection.
*   **Cart Limitations:** The cart works only "one time" per form submission because data is passed via raw POST arrays. A real shop requires `$_SESSION` to remember items across different subpages.

---

## 🤖 2. Machine Learning & Predictive Analytics (Python)

A collection of Python scripts exploring data classification, regression, and basic decision-making models.

### Models & Concepts Covered:
*   **Decision Trees:** Worked with `DecisionTreeClassifier` and `DecisionTreeRegressor` on standard datasets (Iris, Student performance). Includes Gini impurity evaluations and tree visualizations.
*   **Support Vector Machines (SVM):** Tested Linear, RBF, and Polynomial kernels, along with plotting 2D decision boundaries.
*   **Linear & Polynomial Regression:** Compared standard linear lines against higher-degree features to fit non-linear data.
*   **Custom Perceptron:** Features a from-scratch object-oriented implementation of a basic binary **Perceptron** classifier (`MLNeuronTask1.py`) to understand training weights and learning loops without relying on high-level libraries.

### Libraries & Stack Used
*   **Core Toolkit:** `scikit-learn`, `pandas`, `numpy`
*   **Visualization:** `matplotlib`, `seaborn`, `mlxtend` (used for correlation heatmaps and automated scatter matrix generation)

---
*Maintained as a showcase of foundational computer science methodologies and continuous academic progress.*
