# 🚀 Sentiment Analysis App 

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)  
![Model](https://img.shields.io/badge/Model-BERT%20%7C%20BiLSTM-orange)  
![Deploy](https://img.shields.io/badge/Deploy-Vercel-black?logo=vercel)  

**Vercel App Link:** https://sentiment-alert-ai.vercel.app/
 
> ⚡ A **production-ready sentiment analysis web app** with **fine-tuned BERT** (quantized) & **BiLSTM** models.  
> 🌍 Supports **multilingual input** via translation API.  
> 📩 Sends **email alerts** on negative feedback.  
> 📂 Allows **photo, CSV, and text file uploads** for batch analysis.  
> 🚀 Deployed seamlessly on **Vercel**.  

---

## ✨ Features
- 🤖 **Fine-tuned BERT model** (quantized → faster inference).  
- 🔁 **BiLSTM deep learning model** (alternative backend).  
- 🌍 **Multilingual support** – Auto-translates non-English text.  
- 🏷 **Sentiment detection** – Positive / Negative / Neutral.  
- 📩 **Email alerts** – Auto-triggered for **negative feedback**.  
- 📂 **File uploads supported**:  
  - 🖼️ **Image (Photo)** → Extracts text (OCR) → Sentiment analysis.  
  - 📑 **CSV** → Batch analyze multiple feedback entries.  
  - 📜 **TXT** → Analyze long documents or text files.  
- ☁️ **Vercel Deployment** – Fast, serverless, production-ready.  

---

## 🛠 Tech Stack  

| Layer       | Tools Used |
|-------------|------------|
| **Frontend / Deployment** | Vercel |
| **Backend** | Python, FastAPI (or Flask if applicable) |
| **Models**  | BERT (quantized), BiLSTM |
| **Translation API** | Google Translate / DeepL |
| **Email Alerts** | SMTP / SendGrid |
| **OCR (for images)** | Tesseract / EasyOCR |

---

## ⚙️ How It Works  

```mermaid
flowchart TD
    A["User Input: Text / Image / CSV / TXT"] --> B["Preprocessing"]
    B --> C["Translation API → English (Only If Input is not English, Then only API will Trigger)"]
    C --> D["Sentiment Model: BERT or BiLSTM"]
    D --> E{Sentiment}
    E -->|Positive / Neutral| F["Show Result ✅"]
    E -->|Negative| G["Trigger Email Alert 📩"]

