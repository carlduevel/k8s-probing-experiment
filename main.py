import time
from flask import Flask
from flask import abort
app = Flask(__name__)
secondsSinceEpoch = time.time()
trafficReceivedYet = False
trafficReceivedAfter = False


@app.route("/")
def hello():
    global trafficReceivedYet
    if not trafficReceivedYet:
        trafficReceivedAfter = time.time() - secondsSinceEpoch
        trafficReceivedYet = True
        print(f"Traffic received for the first time after {trafficReceivedAfter} s." )

    return str()

@app.route('/health30')
def healthz():
    print("/health30 called")
    if time.time() - secondsSinceEpoch > 30:
        return "OK"
    else:
        abort(400)

@app.route('/health15')
def healthx():
    print("/health15 called")
    if time.time() - secondsSinceEpoch > 15:
        return "OK"
    else:
        abort(400)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
