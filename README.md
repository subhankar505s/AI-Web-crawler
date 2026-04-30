# AI-Web-crawler Tool Using Ollama Llama 3.2
AI-powered web scraper that extracts structured data from any website using Selenium, BeautifulSoup, and local LLMs via Ollama. Features a Streamlit UI for easy interaction, prompt-based parsing, and support for dynamic pages—ideal for automation, research, and data collection

# 🤖 AI Web Scraper (Full Setup + Streamlit UI)

An AI-powered web scraping tool that extracts meaningful data from websites using automation and Large Language Models (LLMs).


---

## 🚀 What This Project Does

* Scrape any website (including dynamic JS websites)
* Clean and process HTML content
* Use AI (LLMs) to extract structured data
* Provide a simple Streamlit UI for interaction

---

## 🛠️ Tech Stack

* Python 3
* Selenium
* BeautifulSoup
* Streamlit
* Ollama (LLM)
* Chrome + ChromeDriver

---

# ⚙️ COMPLETE STEP-BY-STEP SETUP

---

## STEP 1: Install Python

Download and install Python (3.10+ recommended):
https://www.python.org/downloads/

Verify installation:
```sh
python --version
```
---

## STEP 2: Install Git

Download Git:
https://git-scm.com/

Verify:
```sh
git --version
```
---

## STEP 3: Clone Repository

git clone https://github.com/subhankar505s/AI-Web-crawler.git
cd AI-Web-crawler

---

## STEP 4: Create Virtual Environment
```sh
python -m venv venv
```
Activate it:

Windows:
```sh
venv\Scripts\activate
```
Linux/Mac:
```sh
source venv/bin/activate
```
---

## STEP 5: Install Dependencies
```sh
pip install -r requirements.txt
```
---

## STEP 6: Install Google Chrome

https://www.google.com/chrome/

---

## STEP 7: Install ChromeDriver

1. Check Chrome version:
  ``` google-chrome --version ```

2. Download matching ChromeDriver:
   https://chromedriver.chromium.org/downloads

3. Add ChromeDriver to PATH

---

## STEP 8: Install Ollama

Download:
https://ollama.com

Pull model:
```sh
ollama pull llama3
```
Run model:
```sh
ollama run llama3
```
(Keep it running in background)

---

## STEP 9: Verify Setup

Ensure:

* Virtual environment is active
* Ollama is running
* Chrome + ChromeDriver installed

---

# ▶️ RUNNING THE PROJECT

---

## Step 1: Navigate to Project
```sh
cd AI-Web-Scraper
```
---

## Step 2: Run Streamlit App
```sh
streamlit run spindle.py
```
---

## Step 3: Open Browser

http://localhost:8501

---

# 🧭 HOW TO USE

1. Enter website URL
2. Click "Scrape"
3. Enter prompt

Examples:

* Extract all product names and prices
* Get all article titles
* List job postings with salary

4. View structured output

---

# 🧠 HOW IT WORKS

1. Selenium loads webpage
2. BeautifulSoup cleans HTML
3. Data sent to Ollama
4. AI extracts relevant information

---

# 📂 PROJECT STRUCTURE
```
AI-Web-Scraper/
│── spindle.py
│── scraper.py
│── parser.py
│── utils/
│── requirements.txt
│── README.md

```
---

# ⚠️ COMMON ERRORS

ChromeDriver mismatch:
→ Install correct version

Ollama not running:
→ ollama run llama3

Missing modules:
→ pip install -r requirements.txt

Streamlit missing:
→ pip install streamlit

---

# 📸 USE CASES

* E-commerce scraping
* News extraction
* Job listings
* Market research
* Dataset creation

---

# ⚠️ DISCLAIMER

* Educational use only
* Respect website terms
* Do not scrape restricted data

---

# 🤝 CONTRIBUTING

1. Fork repo
2. Create branch
3. Commit changes
4. Open PR

---

# ⭐ SUPPORT

* Star the repo
* Fork it
* Share it

---

# 📜 LICENSE

MIT License

---

# 🙌 CREDITS

* Open-source community

---

# 🚀 Happy Scraping!
