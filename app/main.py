from flask import Flask, render_template, request
from weather import get_weather_data
from utils import valid_input
# from waitress import serve

app = Flask(__name__, template_folder="../templates")
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/weather', methods=['GET'])
def get_weather():
    try: 
        city = request.args.get('city').strip()

        # checks for empty or spaces
        if not valid_input(city): 
            return render_template(
                "error.html",
                message="Invalid inputs"
            )
        
        weather_data = get_weather_data(city)

        # On success display
        if weather_data['cod'] in {200, str(200)}:
            return render_template(
                "weather.html",
                city=weather_data["name"].upper(),
                status=weather_data["weather"][0]["description"].capitalize(),
                temperature=f"{weather_data['main']['temp']:.1f}"
            )
        
        # if city not found
        if weather_data['cod'] in {404, str(404)}:
            return render_error(f"Error: {city} not found")
        
        # all other cases
        return render_error(weather_data['message'] or weather_data)
    
    except Exception as e:
        return render_error("Empty or invalid inputs")
    
def render_error(msg):
    return render_template("error.html", message=msg)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
    # app.debug = True
    # serve(app, host="0.0.0.0", port=8000)