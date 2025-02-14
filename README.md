# 🌍 Multilingual Sentiment Analysis with Aspect Extraction

This project performs **sentiment analysis on multilingual text reviews** using **mBERT (Multilingual BERT)** and extracts aspects using **spaCy**.

✅ **Supports more than 100 languages**  
✅ **Automatically detects and categorizes aspects in reviews**  
✅ **Reads reviews from an Excel file (`reviews.xlsx`) if available**  
✅ **Falls back to static reviews if no file is found**  
✅ **Saves sentiment results to `sentiment_results.csv`**

---

## **📥 Installation & Setup**

### **1️⃣ Install Python (If Not Installed)**

Download and install **Python 3.x** from [Python.org](https://www.python.org/downloads/).  
Make sure to check **"Add Python to PATH"** during installation.

### **2️⃣ Clone This Repository**

```bash
git clone https://github.com/yourusername/multilingual-sentiment-analysis.git
cd multilingual-sentiment-analysis
```

### **3️⃣ Create a Virtual Environment (Optional)**

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### **4️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

### **5️⃣ Download spaCy Model**

```bash
python -m spacy download en_core_web_sm
```

---

## **📄 How to Use**

### **1️⃣ Ensure `reviews.xlsx` Exists (Optional)**

If you want to analyze real reviews, create an **Excel file (`reviews.xlsx`)** with a single column:
| Review |
|-------------------------------------------|
| "Makanannya enak dan harganya cukup terjangkau. Saya sangat puas!" |
| "The food was delicious, but the service was slow." |
| "La comida era excelente pero el servicio era muy lento." |

If the file is **not found**, the script will use **predefined dummy reviews**.

### **2️⃣ Run the Script**

```bash
python absa.py
```

### **3️⃣ View the Output**

After execution, sentiment results will be saved in:

```bash
sentiment_results.csv
```

You can open this file in **Excel** or use **Pandas**:

```python
import pandas as pd
df = pd.read_csv("sentiment_results.csv")
print(df.head())
```

---

## **📊 Output Example**

After running `absa.py`, the result will look like this:

| Review                                                             | Aspect  | Sentiment |
| ------------------------------------------------------------------ | ------- | --------- |
| "Makanannya enak dan harganya cukup terjangkau. Saya sangat puas!" | Makanan | Positif   |
| "The food was delicious, but the service was slow."                | Lainnya | Netral    |
| "La comida era excelente pero el servicio era muy lento."          | Lainnya | Negatif   |
| "Saya kecewa dengan tempat ini, makanan datang sangat terlambat."  | Makanan | Negatif   |

---

## **🛠 Troubleshooting**

### **1️⃣ "ModuleNotFoundError: No module named 'transformers'"**

Run:

```bash
pip install -r requirements.txt
```

### **2️⃣ "OSError: Can't find model 'en_core_web_sm'"**

Run:

```bash
python -m spacy download en_core_web_sm
```

### **3️⃣ "reviews.xlsx not found!"**

Either place the file in the same directory or let the script use dummy reviews.

---

## **📜 License**

This project is **MIT Licensed** – free to use and modify.

---

## **🌟 Credits**

- [Hugging Face](https://huggingface.co/) for **mBERT Sentiment Model**
- [spaCy](https://spacy.io/) for **Aspect Extraction**
- Open-source contributors 🚀
