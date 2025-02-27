import os
import tensorflow as tf
import numpy as np
import cv2
import telebot

# Cargar el modelo 
model = tf.keras.models.load_model('cane_classifier_model.h5')  

# Obtener el token de Telegram
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TELEGRAM_TOKEN)

print("🤖 Bot en ejecución... Esperando mensajes en Telegram...")

# Diccionario de etiquetas
class_labels = {0: "Sana", 1: "Dañada", 2: "Mutilada"}

# Responder cuando el usuario envíe /start
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "¡Hola! Soy un bot de clasificación de trozos de caña de azúcar. 🧑‍🌾\n"
                          "Envíame una imagen de un trozo de caña y te diré su estado.")

# Preprocesamiento de imagen
def preprocess_image(image_path):
    img = cv2.imread(image_path)  # Cargar imagen
    img = cv2.resize(img, (128, 128))  # Redimensionar al tamaño esperado por el modelo
    img = img.astype(np.float32) / 255.0  # Normalizar y convertir a float32
    img = np.expand_dims(img, axis=0)  # Agregar batch dimension
    return img

# Manejo de imágenes enviadas al bot
@bot.message_handler(content_types=["photo"])
def handle_image(message):
    bot.reply_to(message, "📥 Recibiendo imagen, procesando... ⏳")

    file_info = bot.get_file(message.photo[-1].file_id)  # Obtener la imagen
    downloaded_file = bot.download_file(file_info.file_path)

    image_path = "received_image.jpg"
    with open(image_path, "wb") as new_file:
        new_file.write(downloaded_file)

    # Preprocesar la imagen
    img = preprocess_image(image_path)
    
    # Predecir
    prediction = model.predict(img)
    predicted_class = np.argmax(prediction)  # Obtener la clase con mayor probabilidad

    # Obtener etiqueta de clase
    predicted_label = class_labels.get(predicted_class, "Desconocido")

    # Enviar respuesta con la clasificación
    bot.reply_to(message, f"✅ Predicción: {predicted_label}")

# Iniciar el bot
bot.polling()