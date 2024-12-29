from flask import Flask, request
import util
import whatsapp_services
import re
import chatgpt_services

app = Flask(__name__)


@app.route('/welcome', methods=['GET'])
def index():
    return 'Welcome to the Flask API'


@app.route('/whatsapp', methods=['GET'])
def VerifyToken():
    try:
        access_token = "holamundo"
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')

        if token != None and challenge != None and token == access_token:
            return challenge
        else:
            return "", 400
    except:
        return "", 400


@app.route('/whatsapp', methods=['POST'])
def ReceivedMessage():
    try:
        body = request.get_json()
        entry = (body["entry"])[0]
        changes = (entry["changes"])[0]
        value = changes["value"]
        message = (value["messages"])[0]
        number = message["from"]

        text = util.GetTextUser(message)
        
        responseGPT = chatgpt_services.get_response(text)
        
        if responseGPT != "error":
            data = util.TextMessage(responseGPT, number)
        else:
            data = util.TextMessage("Lo siento ocurrio un problema.", number)
        whatsapp_services.SentMessangeWhatsapp(data)
        # ProcessMessages(text, number)
        # print(text)

        return "EVENT_RECEIVED"
    except:
        return "EVENT_RECEIVED"


def ProcessMessages(text, number):
    # Convierte el texto a minúsculas para una comparación insensible al caso
    text = text.lower()
    listData = []

    if "hi" in text or "option" in text:  # Condición corregida
        data = util.TextMessage("Hola, ¿cómo te puedo ayudar?", number)
        dataMenu = util.ListMassage(number)

        listData.append(data)
        listData.append(dataMenu)

    elif "thank" in text:
        data = util.TextMessage("De nada, ¿en qué más puedo ayudarte?", number)
    elif "bye" in text:
        data = util.TextMessage("Adios!", number)
    elif "agency" in text:
        data = util.TextMessage("This is our agency", number)
        dataLocation = util.LocationMassage(number)
        listData.append(data)
        listData.append(dataLocation)
    elif "contact" in text:
        data = util.TextMessage("Contact center:\n00783456", number)
        listData.append(data)
    elif "buy" in text:
        data = util.ButtonsMassage(number)
        listData.append(data)
    elif "sell" in text:
        data = util.ButtonsMassage(number)
        listData.append(data)
    elif re.sub(r'[^\w\s]', '', text).strip() == "si":
        data = util.TextMessage("Ingresa al siguiente Link: https://wa.me/+51924003270", number)
        listData.append(data)
    elif re.sub(r'[^\w\s]', '', text).strip() == "no":
        data = util.TextMessage("Ingresa al siguiente Link: https://wa.me/+51924003270", number)
        listData.append(data)
    else:
        data = util.TextMessage("Lo siento, no puedo entender", number)
        dataMenu = util.ListMassage(number)

        listData.append(data)
        listData.append(dataMenu)


    for item in listData:
        whatsapp_services.SentMessangeWhatsapp(item)


def Generate_Messages(text, number):

    text = text.lower()

    if "text" in text:

        data = util.TextMessage("Text", number)
    if "format" in text:
        data = util.TextFormat(number)
    if "image" in text:
        data = util.ImageMassage(number)
    if "document" in text:
        data = util.DocumentMassage(number)
    if "video" in text:
        data = util.VideoMassage(number)
    if "audio" in text:
        data = util.AudioMassage(number)
    if "location" in text:
        data = util.LocationMassage(number)
    if "button" in text:
        data = util.ButtonsMassage(number)
    if "list" in text:
        data = util.ListMassage(number)

    whatsapp_services.SentMessangeWhatsapp(data)


if __name__ == '__main__':
    app.run(debug=True)
