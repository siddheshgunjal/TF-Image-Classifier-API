import os
import numpy
from tensorflow.keras.callbacks import ModelCheckpoint, TensorBoard
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from get_dataset import get_dataset
from get_model import get_model, save_model

def train_model(model, X, X_test, Y, Y_test):
    # Creates live data:
    # For better yield when duration of the training is extended.
    generated_data = ImageDataGenerator(featurewise_center=False,
        samplewise_center=False,
        featurewise_std_normalization=False,
        samplewise_std_normalization=False,
        zca_whitening=False,
        rotation_range=0,
        width_shift_range=0.1,
        height_shift_range=0.1,
        horizontal_flip = True,
        vertical_flip = False)
    
    generated_data.fit(X)

    # Create directory for checkpoints if does not exists
    if not os.path.exists('Checkpoints/'):
        os.makedirs('Checkpoints/')

    # ModelCheckpoint callback
    model_checkpoint = ModelCheckpoint('Checkpoints/best_weights.h5',
        monitor='val_loss',
        save_best_only=True,
        save_weights_only=True,
        mode='auto',
        verbose=1,)

    # TensorBoard callback
    tensorboard = TensorBoard(log_dir='Checkpoints/logs',
        histogram_freq=0,
        write_graph=True,
        write_images=False,
        embeddings_freq=0,
        embeddings_layer_names=None,
        embeddings_metadata=None)
    # Use `tensorboard --logdir Checkpoints/logs` in terminal to view graphs

    model.fit_generator(generated_data.flow(X, Y, batch_size=64),
        steps_per_epoch=X.shape[0]//8,
        epochs=50,
        validation_data=(X_test, Y_test),
        callbacks=[model_checkpoint, tensorboard])

    # # If you don't want to use Image Augmentation/Generator, use this:
    # model.fit(X, Y,
    #     batch_size=10,
    #     epochs=25,
    #     validation_data=(X_test, Y_test),
    #     shuffle=True,
    #     callbacks=[model_checkpoint, tensorboard])
    
    return model

def main():
    X, X_test, Y, Y_test = get_dataset()
    model = get_model(len(Y[0]))
    model = train_model(model, X, X_test, Y, Y_test)
    save_model(model)
    return model

if __name__ == '__main__':
    main()
