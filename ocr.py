#This code is specifically to fetch information from any .aspx file
import re
import json
import requests
import pdfplumber
from io import BytesIO
from openai import OpenAI

# ------------------------
# Config
# ------------------------
client = OpenAI(
    api_key="",   # 🔑 Add your API key here
    base_url="https://openrouter.ai/api/v1"   # OpenRouter endpoint
)


# ------------------------
# Fetch Report Text
# ------------------------
def fetch_pdf_text(url: str) -> str:
    """
    Fetch PDF report from the given URL and extract text.
    Some URLs end with a comma — keep it, do NOT strip.
    """
    try:
        print(f"  📥 Downloading: {url}")
        resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=60)

        if resp.status_code == 200 and resp.content:
            if "pdf" in resp.headers.get("content-type", "").lower():
                with pdfplumber.open(BytesIO(resp.content)) as pdf:
                    text = "\n".join(page.extract_text() or "" for page in pdf.pages)
                print("  ✅ PDF text extracted")
                return text
            else:
                print("  ⚠️ Report is not PDF, using raw text fallback")
                return resp.text
        else:
            raise Exception(f"HTTP {resp.status_code}")

    except Exception as e:
        print(f"  ❌ Error fetching {url}: {e}")
        return ""


# ------------------------
# Parse Report with LLM
# ------------------------
def parse_report_with_llm(report_text: str) -> dict:
    if not report_text.strip():
        return {"error": "No text extracted from report."}

    prompt = f"""
You are a medical report parser. Extract structured information from the report text.

Report text:
---
{report_text}
---

Return JSON with the following structure:

{{
  "Patient_Name": "string or null",
  "Report_Date": "YYYY-MM-DD or null",
  "Test_Name": "string or null",
  "Key_Findings": "string or null",
  "Test_Results": {{
     "Parameter_Name": {{
        "Value": "string",
        "Reference_Range": "string or null",
        "Status": "Normal | High | Low | Abnormal | null"
     }},
     ...
  }}
}}

⚠️ Rules:
- Do NOT include Patient_ID or any IDs in output.
- If a field is not explicitly mentioned, return `null`.
- Patient_Name may appear as "Patient Name", "Name of Patient", "Patient:".
- Report_Date may appear as "Date", "Reported On", "Report Generated".
- Key_Findings should summarize abnormalities.
- For Test_Results:
  - Always include Value, Reference_Range, Status.
  - Status should be "Normal" if within reference, otherwise "High", "Low", or "Abnormal".
  - If Reference_Range is not given, return null.
- Output **valid JSON only**.
    """

    try:
        resp = client.chat.completions.create(
            model="google/gemini-2.5-flash",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.15,
        )

        raw_output = resp.choices[0].message.content.strip()

        try:
            parsed = json.loads(raw_output)
            print("  ✅ LLM parsed successfully")
            return parsed
        except json.JSONDecodeError:
            json_match = re.search(r"\{.*\}", raw_output, re.DOTALL)  #re.DOTALL is a flag that modifies the behavior of the special character . (dot) in regular expressions.
            if json_match:
                parsed = json.loads(json_match.group(0))
                print("  ⚠️ JSON fixed with regex")
                return parsed
            else:
                print("  ❌ LLM did not return valid JSON")
                return {"error": "No valid JSON found", "raw_output": raw_output}

    except Exception as e:
        print(f"  ❌ LLM parsing failed: {e}")
        return {"error": f"LLM parsing failed: {e}"}


# ------------------------
# Run System (All at Once)
# ------------------------
def run_all_reports(json_file="report_link.json"):
    with open(json_file, "r") as f:
        data = json.load(f)

    final_results = []
    success_count = 0
    fail_count = 0

    print(f"🚀 Processing {len(data)} reports...\n")

    for idx, item in enumerate(data, start=1):
        url = item.get("url", "").strip()
        if not url:
            continue

        print(f"🔎 Report {idx}/{len(data)}")

        report_text = fetch_pdf_text(url)
        parsed_output = parse_report_with_llm(report_text)

        if "error" in parsed_output:
            fail_count += 1
        else:
            success_count += 1

        final_results.append({
            "report_number": idx,
            "url": url,
            "parsed_output": parsed_output
        })
        print("-" * 50)

    print("\n✅ Processing finished")
    print(f"   Success: {success_count}")
    print(f"   Failed:  {fail_count}")

    return final_results


# ------------------------
# Entry point
# ------------------------
if __name__ == "__main__":
    results = run_all_reports("report_link.json")
    print("\n📊 Final Parsed Output:")
    print(json.dumps(results, indent=2, ensure_ascii=False))

    with open("extracted_reports.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
        print("\n💾 Saved results to extracted_reports.json")
