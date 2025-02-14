import os
import spacy
import pandas as pd
from transformers import pipeline

# **Load spaCy model for aspect extraction**
nlp = spacy.load("en_core_web_sm")

# **Load mBERT Sentiment Model from Hugging Face**
sentiment_pipeline = pipeline("text-classification", model="nlptown/bert-base-multilingual-uncased-sentiment")

# **Check if 'reviews.xlsx' exists**
file_path = "reviews.xlsx"

if os.path.exists(file_path):
    print("📂 Using reviews from 'reviews.xlsx'...")
    df = pd.read_excel(file_path)

    # **Ensure the file contains the correct column**
    if "Review" not in df.columns:
        raise ValueError("The Excel file must have a column named 'Review'.")

    # **Convert the column into a list of reviews**
    dummy_reviews = df["Review"].dropna().tolist()  # Remove NaN values

else:
    print("⚠ 'reviews.xlsx' not found! Using static dummy reviews.")
    
    # **Fallback to hardcoded dummy reviews**
    dummy_reviews = [
        "Makanannya enak dan harganya cukup terjangkau. Saya sangat puas!",  # Indonesia
        "The food was delicious, but the service was slow.",  # English
        "La comida era excelente pero el servicio era muy lento.",  # Spanish
        "Makanan terlalu asin dan porsinya kecil, tidak sesuai dengan harganya.",  # Indonesia
        "Le restaurant était propre et agréable. J'y retournerai!",  # French
        "El lugar es hermoso y el ambiente es relajante.",  # Spanish
        "Saya kecewa dengan tempat ini, makanan datang sangat terlambat.",  # Indonesia
        "Die Bedienung war unfreundlich und langsam.",  # German
        "Pelayanannya sangat ramah dan cepat!",  # Indonesia
        "Layanan pelanggan sangat buruk, saya tidak akan kembali lagi.",  # Indonesia
    ]

# **Predefined aspects for restaurants**
predefined_aspects = ["Makanan", "Pelayanan", "Harga", "Pemandangan", "Suasana", "Kebersihan"]

# **Function to extract aspects from reviews**
def extract_aspect(text):
    doc = nlp(text)
    for token in doc:
        if token.text.lower() in [aspect.lower() for aspect in predefined_aspects]:
            return token.text.capitalize()
    return "Lainnya"  # If no clear aspect is found

# **Apply aspect extraction**
aspects = [extract_aspect(review) for review in dummy_reviews]

# **Function to analyze sentiment using mBERT**
def get_sentiment(review):
    result = sentiment_pipeline(review)[0]
    
    # The model outputs a score from 1 to 5:
    # 1-2 = Negative, 3 = Neutral, 4-5 = Positive
    score = int(result["label"].split()[0])  # Extract numeric score
    if score >= 4:
        return "Positif"
    elif score == 3:
        return "Netral"
    else:
        return "Negatif"

# **Apply sentiment analysis**
sentiments = [get_sentiment(review) for review in dummy_reviews]

# **Create DataFrame with results**
df_reviews = pd.DataFrame({
    "Review": dummy_reviews,
    "Aspect": aspects,
    "Sentiment": sentiments
})

# **Save results to a new CSV file**
output_file = "sentiment_results.csv"
df_reviews.to_csv(output_file, index=False)

# **Display results**
print("\n✅ Sentiment Analysis Completed! Results saved in 'sentiment_results.csv'.")
print(df_reviews)