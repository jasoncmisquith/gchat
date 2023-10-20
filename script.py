import requests
import json
import time


SPACE_URL = "https://chat.googleapis.com/v1/spaces/AAAAGSGaeK0/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=rfr3PfX0rX1uu9HJ8am9kyPrmX3S1T8lPP-BGG2NCsw"

TEXT_PARAGRAPH = {
        "textParagraph": {
            "text": "Hello World!"
        }
    }


GRID_ITEM = {
        "image": {
        "imageUri": "https://developers.google.com/static/chat/images/chat-app-hero-image_1440.png",
        "cropStyle": {
            "type": "SQUARE"
        },
        "borderStyle": {
            "type": "STROKE"
        }
        },
        "title": "An item",
        "textAlignment": "CENTER"
    }

GRID_ITEM_TEXT = {
        "title": "An item",
        "subtitle": "Big subtitle",
        "textAlignment": "CENTER"
    }
GRID = {
            "grid": {
                "title": "A fine collection of items",
                "columnCount": 3,
                "borderStyle": {
                "type": "STROKE",
                "cornerRadius": 4.0
                },
                "items": [
                GRID_ITEM,
                GRID_ITEM,
                GRID_ITEM_TEXT
                ],
                "onClick": {
                "openLink": {
                    "url": "https://developers.google.com/chat"
                }
                }
            }
        }



COLUMNS = {
        "columns": {
            "columnItems": [
                {
                "horizontalSizeStyle": "FILL_MINIMUM_SPACE",
                "horizontalAlignment": "CENTER",
                "verticalAlignment": "CENTER",
                "widgets": [

                ]
                },
                {
                "horizontalSizeStyle": "FILL_AVAILABLE_SPACE",
                "horizontalAlignment": "CENTER",
                "verticalAlignment": "TOP",
                "widgets": [
                    {
                        "textParagraph": {
                            "text": "Text paragraph widget with text. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas viverra accumsan augue, non lobortis quam molestie at. Nunc vitae magna vel lectus ullamcorper accumsan. Nulla posuere pellentesque felis, sit amet vehicula nibh sagittis a. Vestibulum tempor ut quam non ultrices. Donec ut ullamcorper purus. Pellentesque interdum urna porta consectetur mollis."
                        }
                    }
                ]
                },


            ]
        }
    }


SELECTION_INPUT_CHECKBOX = {
          "selectionInput": {
            "type": "CHECK_BOX",
            "label": "Contact type",
            "name": "contactType",
            "items": [
              {
                "text": "Work",
                "value": "Work",
                "selected": False
              },
              {
                "text": "Personal",
                "value": "Personal",
                "selected": False
              }
            ]
          }
        }
      

content={
    'cardsV2': [
        {
            'cardId': f'{time.time()}',
            'card': {
                'header': {
                    'title': 'Sasha',
                    'subtitle': 'Software Engineer',
                    'imageUrl': 'https://developers.google.com/chat/images/quickstart-app-avatar.png',
                    'imageType': 'CIRCLE',
                    'imageAltText': 'Avatar for Sasha'
                },
                'sections': [
                    {
                        'header': 'Contact Info',
                        'collapsible': True,
                        'uncollapsibleWidgetsCount': 1,
                        'widgets': [
                            TEXT_PARAGRAPH,
                            GRID,
                            COLUMNS,
                            SELECTION_INPUT_CHECKBOX,

                            
                            {
                                'decoratedText': {
                                    'startIcon': {
                                        'knownIcon': 'EMAIL'
                                    },
                                    'text': 'sasha@example.com'
                                }
                            },
                            {
                                'decoratedText': {
                                    'startIcon': {
                                        'knownIcon': 'PERSON'
                                    },
                                    'text': "<font color='red'>Online</font>"
                                }
                            },
                            {
                                'decoratedText': {
                                    'startIcon': {
                                        'knownIcon': 'PHONE'
                                    },
                                    'text': '+1 (555) 555-1234'
                                }
                            },
                            {
                                'buttonList': {
                                    'buttons': [
                                        {
                                            'text': 'Share',
                                            'onClick': {
                                                'openLink': {
                                                    'url': 'https://example.com/share'
                                                }
                                            }
                                        },
                                        {
                                            'text': 'Edit',
                                            'onClick': {
                                                'action': {
                                                    'function': 'goToView',
                                                    'parameters': [
                                                        {
                                                            'key': 'viewType',
                                                            'value': 'EDIT'
                                                        }
                                                    ]
                                                }
                                            }
                                        }
                                    ]
                                }
                            }
                        ]
                    }
                ]
            }
        }
    ]
}




response = requests.post(SPACE_URL, json=content)
print(response.text)