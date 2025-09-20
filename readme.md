🧾 Medical Report Parser (.aspx / PDF Reports)

This project is a Python tool that fetches medical reports from .aspx or .pdf links and automatically converts them into structured JSON using an AI model (LLM via OpenRouter).

It helps labs, clinics, and developers by turning unstructured medical reports into clean, digital data for dashboards, analysis, or storage.

📌 Why this tool?

Doctors & labs share reports as PDFs hosted on .aspx links.

Manually reading each report is slow and error-prone.

This tool:
✅ Downloads the report
✅ Extracts text
✅ Parses it into JSON (Patient Name, Report Date, Findings, Results)
✅ Saves everything automatically

🖼️ Workflow Diagram
flowchart TD
    A[📥 Report URL (.aspx or PDF)] --> B[⬇️ Download Report]
    B --> C[📄 Extract Text (PDF/Text)]
    C --> D[🤖 Parse with LLM (OpenRouter)]
    D --> E[📊 Structured JSON Output]
    E --> F[💾 Save to extracted_reports.json]

⚙️ Features

Works with .aspx medical reports and direct PDFs

Extracts patient details, test names, findings, and results

Handles both PDF text and non-PDF text

Automatically fixes formatting issues in JSON

Saves all results into a single JSON file

📂 Project Structure
.
├── main.py                  # Main script
├── report_link.json          # Input file with report URLs
├── extracted_reports.json    # Output file with parsed results
└── README.md                 # Documentation

🚀 Quick Start
1️⃣ Clone the repository
git clone https://github.com/YOUR-USERNAME/medical-report-parser.git
cd medical-report-parser

2️⃣ Install dependencies
pip install requests pdfplumber openai

3️⃣ Add your API Key

Open main.py and set your OpenRouter API key:

client = OpenAI(
    api_key="YOUR_API_KEY_HERE",
    base_url="https://openrouter.ai/api/v1"
)

4️⃣ Add report URLs

Create a file report_link.json:

[
  {"url": "https://example.com/report1.aspx"},
  {"url": "https://example.com/report2.pdf"}
]

5️⃣ Run the script
python main.py

📊 Example Output
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

🛠️ How to Fork this Repository

Click the Fork button (top-right of this repo).

Choose your GitHub account as the destination.

Clone your fork locally:

git clone https://github.com/YOUR-USERNAME/medical-report-parser.git


Make changes and push them:

git add .
git commit -m "Updated parser"
git push origin main

📜 License

MIT License – Free for personal and commercial use.

👉 This README is now friendly for both developers and managers:

Techies get commands & structure.

Managers see workflow & purpose.
