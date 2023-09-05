import sys
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.models import model_from_json
from get_dataset import get_img

def predict(model, X):
    Y = model.predict(X)
    Y = np.argmax(Y, axis=1)
    # print(Y)
    
    if Y[0] == 0:
        Y = 'cat \U0001f431'
    elif Y[0] == 1:
        Y = 'dog \U0001f436'
    elif Y[0] == 2:
        Y = 'ship \U0001f6a2'
        
    return Y

if __name__ == '__main__':
    img_dir = sys.argv[1]
    img = get_img(img_dir)
    X = np.zeros((1, 64, 64, 3), dtype='float64')
    X[0] = img

    # Getting model:
    model_file = open('Model/model.json', 'r')
    model = model_file.read()
    model_file.close()
    model = model_from_json(model)

    # Getting weights
    model.load_weights("Model/weights.h5")
    
    # Running predictions
    Y = predict(model, X)
    print('\nIt is a ' + Y + '!\n')
