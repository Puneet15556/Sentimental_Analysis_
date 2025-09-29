Sentiment Analysis App 🚀

A production-ready sentiment analysis web application built with fine-tuned BERT and BiLSTM models. The app is deployed on Vercel, supports multilingual input via translation API, and sends email alerts for negative feedback.

🔥 Features

Fine-tuned BERT model (quantized for faster inference).

Deep Learning BiLSTM model (alternative backend for comparison).

Multilingual Support – Any non-English input is automatically translated to English before sentiment prediction.

Sentiment Categories – Detects Positive, Negative, Neutral sentiment.

Email Alerts – Triggers email notifications for negative feedback.

Deployed on Vercel – Scalable, serverless deployment.

🛠️ Tech Stack

Frontend/Deployment: Vercel

Backend: Python / FastAPI (or Flask if you used that – change accordingly)

NLP Models:

Fine-tuned BERT (quantized for efficiency)

BiLSTM model (baseline)

Translation API: Google Translate API (or specify if you used DeepL/Azure/etc.)

Email Alerts: SMTP / SendGrid / Nodemailer (whichever you used)

⚙️ How It Works

User enters text in any language.

If not in English → translated to English.

Text is passed to the BERT model (or BiLSTM).

Model outputs sentiment score (Positive, Negative, Neutral).

If Negative → system triggers an email alert.
