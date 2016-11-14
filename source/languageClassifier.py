
import json
from watson_developer_cloud import ConversationV1

class langClassifier:
    """This module takes text as input and returns intent, confidence, entity, value."""

    def __init__(self):
        """initialise the watson conversation service."""
        # initializing with the watson conversation object.
        self.conversation = ConversationV1(
            username='8f3bdb08-ce20-4ec8-ad91-886ac6648319',
            password='67yc28TWbL5J',
            version='2016-09-20')

        # define a blank context file.
        self.context = {}
        # workspace id to access.
        self.workspace_id = '09f71121-d51e-4eb2-8d0d-73fb7ba82774'

    def getIntent(self, text):
        """ This method calls the watson conversation service.
            input - text returned from ASR.
            output :-
            intent - value of the intent
            confidence - confidence of the intent
            entity - base entity values.
            value - actual value of the entity.
            alternateIntent - true/false - if alternate intents are available.
        """
        textDict = {'text': text}

        response = self.conversation.message(
          workspace_id=self.workspace_id,
          #message_input={'text': 'pick the key'},
          message_input=textDict,
          context=self.context
        )

        intentDict = response['intents'][0]
        
        if(response['entities'] != []):
            entityDict = response['entities'][0]
            entity = entityDict['entity']
            value = entityDict['value']
        else:
            value = "empty"

        # check if alternate intent is actually required.
        alternateIntent = response['alternate_intents']
        #print(intentDict)
        #print(entityDict)

        intent = intentDict['intent']
        confidence = intentDict['confidence']

        #print("intent is ", intent, "confidence is ", confidence)
        return intent, value

if __name__ == '__main__':
    test = langClassifier();
    # a,b,c,d = test.getIntent("pick the key and hammer");
    # print("intent is ", a, "confidence is ", b, "entity is ", c, "value is", d)
