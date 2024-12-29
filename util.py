def GetTextUser(message):
    text = ''
    typeMessage = message['type']
    
    if typeMessage == 'text':
        text = (message['text'])['body']
    elif typeMessage =='interactive':
        interactiveObject = (message['interactive'])
        typeInteractive = interactiveObject["type"]
        if typeInteractive == 'button_reply':
            text = (interactiveObject['button_reply'])['title']
        elif typeInteractive == 'list_reply':
            text = (interactiveObject['list_reply'])['title']
        else:
            text = 'No es un mensaje de texto esperado'
            print(text)
    else:
        text = 'No es un mensaje de texto esperado'
        print(text)
    return text

def TextMessage(text,number):
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": number,
        "type": "text",
        "text": {
            "body": text
        }
    }
    return data

def TextFormat(number):
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": number,
        "type": "text",
        "text": {
            "body": "*Hola Causa* \n_que fue barrio_"
        }
    }
    return data
def ImageMassage(number):
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": number,
        "type": "image",
        "image": {
            "link": "https://docs.smooch.io/static/file.d3b6024b.jpg"
        }
    }
    return data
def AudioMassage(number):
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": number,
        "type": "audio",
        "audio": {
            "link": "https://ser.ak47full.com/dfiles/Blessd_Ft._Anuel_AA_-_Mirame_Remix_(WWW.ELGENEROPLUS.COM).mp3"
        }
    }
    return data
def VideoMassage(number):
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": number,
        "type": "video",
        "video": {
            "link": "https://biostoragecloud.blob.core.windows.net/resource-udemy-whatsapp-node/video_whatsapp.mp4"
        }
    }
    return data
def DocumentMassage(number):
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": number,
        "type": "document",
        "document": {
            "link": "https://www.jugandoainvertir.com.ar/descargas/Padre-Rico-Padre-Pobre.pdf",
            "caption": "Padre Rico Padre Pobre"
        }
    }
    return data
def LocationMassage(number):
    data = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "location",
        "location": {
            "latitude": "-12.118483677301667",
            "longitude": "-76.81399415596725",
            "name": "Placita Cieneguilla",
            "address": "V5JP+HCR, Cieneguilla 15593"
        }
    }
    return data
def ButtonsMassage(number):
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": "51924003270",
        "type": "interactive",
        "interactive": {
            "type": "button",
            "body": {
                "text": "¿Confirmas tu registro? 🙊"
            },
            "action": {
                "buttons": [
                    {
                        "type": "reply",
                        "reply": {
                            "id": "001",
                            "title": "✅Si"
                        }
                    },
                    {
                        "type": "reply",
                        "reply": {
                            "id": "002",
                            "title": "❌ No"
                        }
                    }
                ]
            }
        }
    }
    return data


def ListMassage(number):
    data = {
        "messaging_product": "whatsapp",
        "to": "51924003270",
        "type": "interactive",
        "interactive": {
            "type": "list",
            "body": {
                "text": "✅ I have these options"
            },
            "footer": {
                "text": "Select an option"
            },
            "action": {
                "button": "See options",
                "sections": [
                    {
                        "title": "Buy and sell products",
                        "rows": [
                            {
                                "id": "main-buy",
                                "title": "Buy",
                                "description": "Buy the best product your home"
                            },
                            {
                                "id": "main-sell",
                                "title": "Sell",
                                "description": "Sell your products"
                            }
                        ]
                    },
                    {
                        "title": "📍center of attention",
                        "rows": [
                            {
                                "id": "main-agency",
                                "title": "Agency",
                                "description": "Your can visit our agency"
                            },
                            {
                                "id": "main-contact",
                                "title": "Contact center",
                                "description": "One of our agents will assist you"
                            }
                        ]
                    }
                ]
            }
        }
    }
    return data