# 🚀 Sentiment Analysis App 

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)  
![Model](https://img.shields.io/badge/Model-BERT%20%7C%20BiLSTM-orange)  
![Deploy](https://img.shields.io/badge/Deploy-Vercel-black?logo=vercel)  

**Vercel App Link:** https://sentiment-alert-ai.vercel.app/
 
 ⚡ A **Production-ready sentiment analysis web app** with **fine-tuned BERT** (quantized) & **BiLSTM** models.  
 🌍 Supports **multilingual input** via translation API.  
 📩 Sends **email alerts** on negative feedback.  
 🚀 Deployed seamlessly on **Vercel**.  

---

## ✨ Features
- 🤖 **Fine-tuned BERT model** (quantized → faster inference).  
- 🔁 **BiLSTM deep learning model** (alternative backend).  
- 🌍 **Multilingual support** – Auto-translates non-English text.  
- 🏷 **Sentiment detection** – Positive / Negative / Neutral.  
- 📩 **Email alerts** – Auto-triggered for **negative feedback**.  
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

---

## ⚙️ How It Works  
```mermaid
flowchart TD
    A[User Input: Any Language] --> B[Translation API → English]
    B --> C[Sentiment Model (BERT / BiLSTM)]
    C --> D{Sentiment}
    D -->|Positive / Neutral| E[Show Result ✅]
    D -->|Negative| F[Trigger Email Alert 📩]
