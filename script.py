import requests
import json
import time


SPACE_URL = "https://chat.googleapis.com/v1/spaces/AAAAGSGaeK0/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=rfr3PfX0rX1uu9HJ8am9kyPrmX3S1T8lPP-BGG2NCsw"

content = {'cardsV2': [{'cardId': f'{time.time()}', 'card': {'header': {'title': 'Sasha', 'subtitle': 'Software Engineer', 'imageUrl': 'https://developers.google.com/chat/images/quickstart-app-avatar.png', 'imageType': 'CIRCLE', 'imageAltText': 'Avatar for Sasha'}, 'sections': [{'header': 'Contact Info', 'collapsible': True, 'uncollapsibleWidgetsCount': 1, 'widgets': [{'decoratedText': {'startIcon': {'knownIcon': 'EMAIL'}, 'text': 'sasha@example.com'}}, {'decoratedText': {'startIcon': {'knownIcon': 'PERSON'}, 'text': "<font color='red'>Online</font>"}}, {'decoratedText': {'startIcon': {'knownIcon': 'PHONE'}, 'text': '+1 (555) 555-1234'}}, {'buttonList': {'buttons': [{'text': 'Share', 'onClick': {'openLink': {'url': 'https://example.com/share'}}}, {'text': 'Edit', 'onClick': {'action': {'function': 'goToView', 'parameters': [{'key': 'viewType', 'value': 'EDIT'}]}}}]}}]}]}}]}

requests.post(SPACE_URL, json=content)
