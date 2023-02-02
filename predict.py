import logging
import DiablPredicService as DaibPreSvc

"""
This file should be named as 'predict.py' and should contain the 'ModelServe' class and the 'predict' method.
"""
class ModelServe:

    def __init__(self):
        """
        Initialization method for the deployment. Invoked once during deployment startup.
        Load your ML models here and use them in the predict function for serving individual requests.
        """
        logging.info('Initializing models for serving prediction requests for Diabetic Prediction based on Age ,Sex,Weight and Height all numeric values')

    def predict(self, request):
        """
        Return model prediction for a request. Invoked for every individual request.
        Implement this method.

        Arguments:
        request -- a Python dictionary representing JSON body of a prediction request.
        """
        logging.info('Processing the DiabPrediction request')
        Age = request['Age']
        MF = request['MF']
        Weight = request['Weight']
        Height = request['Height']
        logging.info([Age,MF,Weight,Height])
        DiabPredictServer = DaibPreSvc.DiabPredicService()
        result = DiabPredictServer.predict_score([Age,MF,Weight,Height])
        return result
