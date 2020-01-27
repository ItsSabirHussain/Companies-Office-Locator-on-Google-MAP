from flask import Flask, jsonify, request, render_template
import csv
import json
import xmltodict
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/',  methods=['GET', 'POST'])
@app.route('/index',  methods=['GET', 'POST'])
def indexpage():
    return render_template("index.html")
@app.route('/getregions',  methods=['GET', 'POST'])
def getregions():
    with open('Station_Regions', 'r') as f:
        r = csv.reader(f)
        dd = {}
        for rr in r:
            dd[rr[0]] = rr[2]
    print(dd)
    return render_template("main.html", data = dd)
@app.route('/getstations', methods=['GET', 'POST'])
def getstations():
    value = request.form.get("selected")
    odata = []
    with open('Fire_Station_locations.csv', 'r') as f:
        rr = csv.reader(f)
        for r in rr:
            if value == r[0]:
                dd={}
                dd['id'] = r[1]
                dd['Station'] = r[2]
                dd['Address'] = r[4]
                dd['Phone'] = r[5]
                dd['Email'] = r[7]
                dd['lat'] = r[8]
                dd['lon'] = r[9]
                odata.append(dd)
    oo = odata
    print(oo)
    return render_template('office_map.html', data=oo)

if __name__ == '__main__':

    app.run(debug=True)