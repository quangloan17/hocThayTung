import cv2
import os
from sklearn.neural_network import MLPClassifier
from sklearn.externals import joblib

IMG_DIR = 'mnist'

def read_data(tag):
    X = []
    y = []
    
    for digit in range(10):
        dir = os.path.join(IMG_DIR, tag, str(digit))        
        for f in os.listdir(dir):
            file_name = os.path.join(dir, f)
            img = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)
            x = img/255.0
            X.append(x.reshape(-1))
            y.append(digit)
            
    return X,y

print('Reading data ...')
            
Xtrain, ytrain = read_data('train')
Xtest, ytest = read_data('test')
            
print('Training model ...')

model = MLPClassifier(hidden_layer_sizes=(50,), activation='relu',
                    max_iter=50, tol=-1, verbose=True)
            
model.fit(Xtrain, ytrain)

print('Test accuracy : ', model.score(Xtest, ytest))    

joblib.dump(model, 'mnist.model')

model = joblib.load('mnist.model')