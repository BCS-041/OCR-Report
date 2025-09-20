
# 🧾 Medical Report Parser (.aspx / PDF Reports)

[![Python](https://img.shields.io/badge/Python-3.13%2B-blue?logo=python)](https://www.python.org/)
[![Dependencies](https://img.shields.io/badge/requirements-pdfplumber%2C%20requests%2C%20openai-green)](https://pypi.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![OpenRouter](https://img.shields.io/badge/LLM-OpenRouter-red?logo=openai)](https://openrouter.ai)

---

## 📌 Overview

This project is a **Python tool** that fetches medical reports from `.aspx` or `.pdf` links and converts them into **structured JSON** using an **AI model via OpenRouter**.

It helps labs, clinics, and developers by turning **unstructured medical reports** into **clean, digital data** for dashboards, analysis, or record-keeping.

---

## 🎯 Why this tool?

* Medical reports are often served as **PDFs behind `.aspx` URLs**.
* Manually extracting patient and test information is **slow and error-prone**.
* This tool automates the process:
  ✅ Downloads the report
  ✅ Extracts text
  ✅ Parses it into JSON (Patient Name, Date, Findings, Results)
  ✅ Saves everything automatically

---

## 🖼️ Workflow

```mermaid
flowchart TD
    A[📥 Report URL (.aspx or PDF)] --> B[⬇️ Download Report]
    B --> C[📄 Extract Text (PDF/Text)]
    C --> D[🤖 Parse with LLM (OpenRouter)]
    D --> E[📊 Structured JSON Output]
    E --> F[💾 Save to extracted_reports.json]
```

---

## ⚙️ Features

* Works with **.aspx medical reports** and direct PDFs
* Extracts **Patient Details, Report Date, Test Names, Key Findings, Results**
* Handles both **PDF text** and **non-PDF text**
* Fixes malformed JSON automatically
* Saves all results in `extracted_reports.json`

---

## 📂 Project Structure

```
.
├── main.py                  # Main script
├── report_link.json          # Input file with report URLs
├── extracted_reports.json    # Output file with parsed results
└── README.md                 # Documentation
```

---

## 🚀 Quick Start

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/medical-report-parser.git
cd medical-report-parser
```

### 2️⃣ Install dependencies

```bash
pip install requests pdfplumber openai
```

### 3️⃣ Configure API Key

Edit `main.py` and add your **OpenRouter API key**:

```python
client = OpenAI(
    api_key="YOUR_API_KEY_HERE",
    base_url="https://openrouter.ai/api/v1"
)
```

### 4️⃣ Add Report URLs

Create a file `report_link.json`:

```json
[
  {"url": "https://example.com/report1.aspx"},
  {"url": "https://example.com/report2.pdf"}
]
```

### 5️⃣ Run the script

```bash
python main.py
```

---

## 📊 Example Output

```json
[
  {
    "report_number": 1,
    "url": "https://example.com/report1.aspx",
    "parsed_output": {
      "Patient_Name": "John Doe",
      "Report_Date": "2025-09-20",
      "Test_Name": "Blood Test",
      "Key_Findings": "Mild anemia detected",
      "Test_Results": {
        "Hemoglobin": {
          "Value": "10.5 g/dL",
          "Reference_Range": "13-17 g/dL",
          "Status": "Low"
        }
      }
    }
  }
]
```

---

## 🛠️ How to Fork

1. Click the **Fork** button (top-right of this repo).
2. Choose your **GitHub account** as the destination.
3. Clone your fork locally:

   ```bash
   git clone https://github.com/YOUR-USERNAME/medical-report-parser.git
   ```
4. Make changes and push them:

   ```bash
   git add .
   git commit -m "Updated parser"
   git push origin main
   ```

---

## 📜 License

MIT License – Free to use, modify, and distribute.

