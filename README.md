[![DOI](https://zenodo.org/badge/932587816.svg)](https://doi.org/10.5281/zenodo.18732348)

# Multilingual Sentiment Analysis with Aspect Extraction

This project performs multilingual sentiment analysis using Multilingual BERT (mBERT) and extracts aspects from text reviews using spaCy.

The system supports more than 100 languages and can analyze reviews from an Excel file. If no file is provided, the script uses predefined sample reviews.

---

## Features

- Supports more than 100 languages using Multilingual BERT (mBERT)
- Performs sentiment classification on multilingual reviews
- Automatically extracts and categorizes aspects using spaCy
- Reads reviews from `reviews.xlsx` if available
- Falls back to predefined sample reviews if no file is found
- Saves analysis results to `sentiment_results.csv`

---

## Installation

### 1. Install Python

Install Python 3.x from:

https://www.python.org

Ensure Python is added to your system PATH.

---

### 2. Clone the Repository

```bash
git clone https://github.com/yourusername/multilingual-sentiment-analysis.git
cd multilingual-sentiment-analysis
```

---

### 3. Create Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Download spaCy Model

```bash
python -m spacy download en_core_web_sm
```

---

## Usage

### Optional: Prepare reviews.xlsx

Create an Excel file named `reviews.xlsx` with a single column:

```
Review
```

Example entries:

- Makanannya enak dan harganya cukup terjangkau. Saya sangat puas!
- The food was delicious, but the service was slow.
- La comida era excelente pero el servicio era muy lento.

If the file does not exist, the script will use predefined sample reviews.

---

### Run the Script

```bash
python absa.py
```

---

## Output

After execution, results will be saved in:

```
sentiment_results.csv
```

You may open this file in Excel or load it using Pandas:

```python
import pandas as pd
df = pd.read_csv("sentiment_results.csv")
print(df.head())
```

---

## Example Output

| Review | Aspect | Sentiment |
|--------|--------|-----------|
| Makanannya enak dan harganya cukup terjangkau | Makanan | Positif |
| The food was delicious, but the service was slow | Lainnya | Netral |
| La comida era excelente pero el servicio era muy lento | Lainnya | Negatif |

---

## Troubleshooting

### ModuleNotFoundError: No module named 'transformers'

Run:

```bash
pip install -r requirements.txt
```

### OSError: Can't find model 'en_core_web_sm'

Run:

```bash
python -m spacy download en_core_web_sm
```

### reviews.xlsx not found

Place the file in the project directory or allow the script to use default sample reviews.

---

## Citation

If you use this software for academic or research purposes, please cite:

Pratama, I. W. P. (2026). Multilingual Sentiment Analysis with Aspect Extraction [Software].  
https://doi.org/10.5281/zenodo.18732348

---

## License

This project is licensed under the MIT License.
