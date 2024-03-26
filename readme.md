Installation steps:
Steps to run it in your machine
You can either run it google collab or run it locally:



1. It's developed on python 3.10
2. Create a virtual environment by running the following command: `python -m venv meds`
3. Activate it with the following command: Windows -> `.\postures\Scripts  -> activate , For Example: cd postures/Scripts-> next command->activate
4. Install the following libraries by running the following command: `pip install -r requirements.txt'
5. Open medsplantdetection.ipynb file and runn the cells one after the other


Worflow:


1. Importing Libraries:

TensorFlow and its required modules like layers, models, and preprocessing are imported.
Modules from Keras such as ImageDataGenerator, ModelCheckpoint, and EarlyStopping are imported.

2. Loading Pre-trained Model:
MobileNetV2 model pre-trained on ImageNet dataset is loaded.
The model is configured to exclude the top classification layer and to accept input images of size 224x224x3.

3. Inspecting Model Layers:
Each layer in the pre-trained MobileNetV2 model is printed along with its index and whether it's trainable or not.
This helps in understanding the structure of the loaded model.

4. Freezing Layers:
All layers of the pre-trained MobileNetV2 model are set as non-trainable.
This ensures that the weights of these layers remain fixed during training.

5. Adding Custom Classification Head:
A custom classification head is added to the MobileNetV2 model.
This head consists of global average pooling followed by several dense layers with ReLU activation.
The output layer has softmax activation with the number of units equal to the number of classes.

6. Preparing Image Data:
Image data generators are set up for training and validation data.
Data augmentation techniques like rotation, shifting, and flipping are applied to the training data.
Training and validation directories are specified, and file paths along with corresponding class labels are collected.

7. Building Data Generators:
Image data generators are created for both training and validation sets.
They preprocess images and generate batches of augmented data during model training.

8. Inspecting Class Names and Samples:
Class names and the number of samples per class in the training and validation sets are collected and printed.

9. Building the Final Model:
The final model is constructed by combining the pre-trained MobileNetV2 base model with the custom classification head.
The model summary is printed to examine the architecture.

10. Compiling the Model:
The model is compiled with categorical cross-entropy loss and RMSprop optimizer.
Metrics like accuracy are specified for monitoring during training.

11. Training the Model:
The model is trained using the fit method.
Training data generator is used with specified batch size and steps per epoch.
Validation data generator is used with specified validation steps.

12. Model Checkpoint and Early Stopping:
ModelCheckpoint and EarlyStopping callbacks are defined to save the best model and prevent overfitting.

13. Visualizing Training History:
Training history such as accuracy and loss is plotted for both training and validation sets using Matplotlib.

14. Prediction on a Sample Image:
An example image is loaded, preprocessed, and fed into the trained model for prediction.
The predicted class probabilities are printed along with the predicted class label.