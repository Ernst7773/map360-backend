from flask import Flask, request, jsonify
from flask_cors import CORS
from pyproj import Transformer

app = Flask(__name__)
CORS(app)

transformer = Transformer.from_crs("EPSG:4326", "EPSG:2193", always_xy=True)

# TFW values
A = 0.075
E = -0.075
C = 1451117.3875
F = 5046574.312497

@app.route("/convert", methods=["POST"])
def convert():
    data = request.json
    lat = data["lat"]
    lon = data["lon"]

    easting, northing = transformer.transform(lon, lat)

    x = (easting - C) / A
    y = (F - northing) / abs(E)

    print("Lat:", lat)
    print("Lon:", lon)
    print("Easting:", easting)
    print("Northing:", northing)
    print("X:", x)
    print("Y:", y)

    return jsonify({"x": x, "y": y})
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    
    