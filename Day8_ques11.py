from flask import Flask, jsonify, request, Response
import random

app = Flask(__name__)

weather_conds = ["sunny", "rainy", "cloudy", "windy", "snowy"]

@app.route("/weather/<city>")
def weather(city):
    resp_format = request.args.get("format", "json").lower()
    temp = random.randint(10,50) #random temp's
    cond = random.choice(weather_conds) #random weather conditions from above list
    
    if resp_format == "xml":  #xml format http://127.0.0.1:5000/weather/ladak?format=xml
        xml_data= f"""        
        <weather>
            <city>City : {city}</city></br>
            <temperature>temperature: {temp}℃ </temperature></br>
            <condition>Condition : {cond}</condition>
        </weather>
        """
        return Response(xml_data) 
        
    #json response http://127.0.0.1:5000/weather/ladak?format=json or http://127.0.0.1:5000/weather/ladak
    json_data = { 
                    "city": city,
                    "temperature in Celsius": temp,
                    "condition": cond
                }                       
    return jsonify(json_data)
    
if __name__ =='__main__':
    app.run(debug = True)
