import logging
import os
import pickle
import numpy as np
from collections import defaultdict
import joblib


MODEL_PATH = os.getcwd() + '/model'

label_dict = {"No":0,"Yes":1}
gender_map = {"Female":0,"Male":1}
target_label_map = {"Negative":0,"Positive":1}
['Age','Weight_KG','Height_Inch','Gender']


class DiabPredicService:
    loaded_models = {}

    def __init__(self):
        print(os.getcwd())
        for modelDirectory in self.get_model_directories(MODEL_PATH):
            self.load_model(os.path.join(MODEL_PATH, modelDirectory))
    

    
    def get_model_directories(self, modelsPath):
        modeldirectories = [dI for dI in os.listdir(modelsPath) if os.path.isdir(os.path.join(modelsPath, dI))]
        logging.debug('Random Forest Classifier models {modeldirectories} found'.format(modeldirectories=modeldirectories))
        return modeldirectories
    
    def load_model(self, absolute_model_directory_path):
        current_model = {}
        
        try:
            logging.debug("Diab prediction model loading start in load_mode func")
            loaded_model = joblib.load(open(os.path.join(absolute_model_directory_path),"rb"))
            logging.info("Loading model using joblib is done")
            return loaded_model
        except FileNotFoundError:
            logging.error("Diabetic learning model is not found in directory or model directory does exists in current project")

    
    def predict_score(self,inarray=[]):
        result = []
        logging.debug("Diab prediction model loading start in predict_score func")
        simplfy=np.array(inarray).reshape(1,-1)
        logging.info("simplyfy Output as NpArray{simplfy}".format(simplfy=simplfy))

        
        loaded_model = self.load_model('model/random_forst_model_Nirav.pkl');

        '''Now update using ML model to get our prediction'''
        prediction = loaded_model.predict(simplfy)
        predict_probability = loaded_model.predict_proba(simplfy)
        logging.info("Diab Model Prediction{pred} and Probability of predictuion{prob}".format(pred=prediction,prob=predict_probability))

        '''Now formatted prediction result'''
        if prediction ==1:
            logging.warning("Positive Risk-{}".format(prediction[0]))
            pred_probability_score = {"Negative DM": predict_probability[0][0] * 100, "Positive DM": predict_probability[0][1] * 100}
            logging.warning("Prediction Probability Score{Score}".format(Score=pred_probability_score))
            return "Positive Risk-{}".format(prediction[0]) + "Prediction Probability Score{Score}".format(Score=pred_probability_score)
            
        else:
            logging.info("Negative Risk-{}".format(prediction[0]))
            pred_probability_score = {"Negative DM": predict_probability[0][0] * 100, "Positive DM": predict_probability[0][1] * 100}
            logging.info("Prediction Probability Score {Score}".format(Score=pred_probability_score))
            return "Negative Risk-{}".format(prediction[0]) + "Prediction Probability Score{Score}".format(Score=pred_probability_score)


    