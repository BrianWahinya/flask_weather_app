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
        if valid_input(city):
            weather_data = get_weather_data(city)
            # print(weather_data)
            return render_template(
                "weather.html",
                city=weather_data["name"].upper(),
                status=weather_data["weather"][0]["description"].capitalize(),
                temperature=f"{weather_data['main']['temp']:.1f}"
            )
        else:
            raise Exception
    except:
        return render_template("error.html")
    


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
    # app.debug = True
    # serve(app, host="0.0.0.0", port=8000)