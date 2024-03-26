# from flask import Flask, request, jsonify
# # from tensorflow.keras.models import load_model
# from tensorflow import keras
# from keras.models import load_model
# import numpy as np
# from PIL import Image
# import io
import tensorflow as tf

# app = Flask(__name__)
# model = load_model('Model.h5')

# # Define the image dimensions expected by the model
# img_width, img_height = 224, 224

# @app.route('/')
# def index():
#     return '''
#     <form action="/predict" method="post" enctype="multipart/form-data">
#         <input type="file" name="file">
#         <input type="submit" value="Upload">
#     </form>
#     '''

# @app.route('/predict', methods=['POST'])
# def predict():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file part'})
#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({'error': 'No selected file'})
#     try:
#         img = Image.open(io.BytesIO(file.read()))
#         img = img.resize((img_width, img_height))  # Resize image to match model input size
#         img_array = np.asarray(img) / 255.0  # Normalize pixel values
#         img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
#         prediction = model.predict(img_array)
#         predicted_class = np.argmax(prediction)
#         class_names = ['Alpinia Galanga (Rasna)',
#                         'Amaranthus Viridis (Arive-Dantu)',
#                         'Artocarpus Heterophyllus (Jackfruit)',
#                         'Azadirachta Indica (Neem)',
#                         'Basella Alba (Basale)',
#                         'Brassica Juncea (Indian Mustard)',
#                         'Carissa Carandas (Karanda)',
#                         'Citrus Limon (Lemon)',
#                         'Ficus Auriculata (Roxburgh fig)',
#                         'Ficus Religiosa (Peepal Tree)',
#                         'Hibiscus Rosa-sinensis',
#                         'Jasminum (Jasmine)',
#                         'Mangifera Indica (Mango)',
#                         'Mentha (Mint)',
#                         'Moringa Oleifera (Drumstick)',
#                         'Muntingia Calabura (Jamaica Cherry-Gasagase)',
#                         'Murraya Koenigii (Curry)',
#                         'Nerium Oleander (Oleander)',
#                         'Nyctanthes Arbor-tristis (Parijata)',
#                         'Ocimum Tenuiflorum (Tulsi)',
#                         'Piper Betle (Betel)',
#                         'Plectranthus Amboinicus (Mexican Mint)',
#                         'Pongamia Pinnata (Indian Beech)',
#                         'Psidium Guajava (Guava)',
#                         'Punica Granatum (Pomegranate)',
#                         'Santalum Album (Sandalwood)',
#                         'Syzygium Cumini (Jamun)',
#                         'Syzygium Jambos (Rose Apple)',
#                         'Tabernaemontana Divaricata (Crape Jasmine)',
#                         'Trigonella Foenum-graecum (Fenugreek)'] 
#         result = class_names[predicted_class]
#         return jsonify({'result': result})
#     except Exception as e:
#         return jsonify({'error': str(e)})

# if __name__ == '__main__':
#     app.run(debug=True)
print(tf.keras.__version__)
