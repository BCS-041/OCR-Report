# 🧾 Medical Report Parser (.aspx / PDF Reports)

[![Python](https://img.shields.io/badge/Python-3.13%2B-blue?logo=python)](https://www.python.org/)
[![Dependencies](https://img.shields.io/badge/requirements-pdfplumber%2C%20requests%2C%20openai-green)](https://pypi.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![OpenRouter](https://img.shields.io/badge/LLM-OpenRouter-red?logo=openai)](https://openrouter.ai)

A Python tool that fetches medical reports from `.aspx` or `.pdf` links and converts them into structured JSON using AI models via OpenRouter.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Why This Tool?](#-why-this-tool)
- [Installation](#-installation)
- [Usage](#-usage)
- [Configuration](#-configuration)
- [Example Output](#-example-output)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)

---

## 📌 Overview

This project is a **Python tool** that fetches medical reports from `.aspx` or `.pdf` links and converts them into **structured JSON** using an **AI model via OpenRouter**.

It helps labs, clinics, and developers by turning **unstructured medical reports** into **clean, digital data** for dashboards, analysis, or record-keeping.

---

## 🎯 Why This Tool?

- Medical reports are often served as **PDFs behind `.aspx` URLs**
- Manually extracting patient and test information is **slow and error-prone**
- This tool automates the process:
  - ✅ Downloads the report
  - ✅ Extracts text
  - ✅ Parses it into JSON (Patient Name, Date, Findings, Results)
  - ✅ Saves everything automatically

---

## ⚙️ Features

- Works with **.aspx medical reports** and direct PDFs
- Extracts **Patient Details, Report Date, Test Names, Key Findings, Results**
- Handles both **PDF text** and **non-PDF text**
- Fixes malformed JSON automatically
- Saves all results in `extracted_reports.json`

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/medical-report-parser.git
cd medical-report-parser
```

### 2. Install dependencies

```bash
pip install requests pdfplumber openai
```

### 3. System Dependencies (if needed)

For PDF processing, you might need:

**On Ubuntu/Debian:**
```bash
sudo apt-get install build-essential libpoppler-cpp-dev pkg-config python3-dev
```

**On macOS:**
```bash
brew install pkg-config poppler
```

**On Windows:**
No additional system dependencies required.

---

## ⚙️ Configuration

### 1. Add your OpenRouter API Key

Edit `main.py` and add your **OpenRouter API key**:

```python
client = OpenAI(
    api_key="YOUR_API_KEY_HERE",
    base_url="https://openrouter.ai/api/v1"
)
```

### 2. Configure Input/Output Files

Modify these variables in the script if needed:

```python
INPUT_FILE = "report_link.json"        # Input file with report URLs
OUTPUT_FILE = "extracted_reports.json" # Output file for parsed results
```

### 3. Prepare Input Data

Create a file `report_link.json` with your report URLs:

```json
[
  {"url": "https://example.com/report1.aspx"},
  {"url": "https://example.com/report2.pdf"}
]
```

---

## 🚀 Usage

Run the script:

```bash
python main.py
```

The tool will:
1. Fetch each report from the provided URLs
2. Extract text content
3. Process through the AI model
4. Save structured data to `extracted_reports.json`

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

## 📂 Project Structure

```
medical-report-parser/
├── main.py                  # Main script
├── report_link.json         # Input file with report URLs
├── extracted_reports.json   # Output file with parsed results
├── requirements.txt         # Python dependencies
├── LICENSE                  # MIT License
└── README.md               # Documentation
```

---

## 🛠️ Customization

### Modifying the Extraction Schema

Edit the system prompt in `main.py` to change what information is extracted:

```python
system_prompt = """You are a medical report parsing assistant. Extract the following information from the medical report:
- Patient Name
- Report Date
- Test Name
- Key Findings
- Test Results (including values, reference ranges, and status)
..."""
```

### Adding Support for New Formats

The tool can be extended to support additional medical report formats by:

1. Adding new text extraction functions
2. Modifying the URL handling logic
3. Creating specialized parsing prompts for different report types

---

## 🐛 Troubleshooting

### Common Issues

1. **API Errors**
   - Verify your OpenRouter API key is correct
   - Check your API quota and billing status

2. **PDF Extraction Issues**
   - Ensure `pdfplumber` is properly installed
   - For encrypted PDFs, additional handling may be required

3. **Network Errors**
   - Check your internet connection
   - Verify the report URLs are accessible

### Debug Mode

Enable debug output by modifying the script:

```python
DEBUG = True  # Set to True for verbose output
```

---

## 🤝 Contributing

We welcome contributions! Please feel free to submit issues, feature requests, or pull requests.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [OpenRouter](https://openrouter.ai/) for providing AI model access
- [pdfplumber](https://github.com/jsvine/pdfplumber) for PDF text extraction
- [OpenAI Python Library](https://github.com/openai/openai-python) for API interactions

---


<div align="center">

**⭐ Don't forget to star this repository if you find it useful!**

</div>
