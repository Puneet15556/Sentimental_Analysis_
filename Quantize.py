import tensorflow as tf
from transformers import AutoTokenizer, TFAutoModelForSequenceClassification

# Path to your saved model
MODEL_PATH = "./fine_tuned_rating_based_model"

# Load the model using transformers
model = TFAutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)

# Save the model in SavedModel format first
tf.saved_model.save(model, "saved_model")

# Convert the SavedModel to TFLite format
converter = tf.lite.TFLiteConverter.from_saved_model("saved_model")

# Enable quantization
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.target_spec.supported_ops = [
    tf.lite.OpsSet.TFLITE_BUILTINS,
    tf.lite.OpsSet.SELECT_TF_OPS
]

# Convert the model
tflite_model = converter.convert()

# Save the quantized model
with open('sentiment_model_quantized.tflite', 'wb') as f:
    f.write(tflite_model)

print("Quantized model saved as sentiment_model_quantized.tflite")

# Save tokenizer for later use
tokenizer.save_pretrained("quantized_model_tokenizer")
print("Tokenizer saved in quantized_model_tokenizer directory")
