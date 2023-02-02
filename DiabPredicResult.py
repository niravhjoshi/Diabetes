import logging


class DiabPredictResult:
    result = None
    

    
    def show_result(self, text):
            prediction_message = 'Predicting Result Class  "{text}"'
            logging.debug(prediction_message.format(text=text))