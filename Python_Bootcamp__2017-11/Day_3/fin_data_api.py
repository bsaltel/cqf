#
# Simple Financial Data API
# based on Flask
#
import pandas as pd
from flask import Flask, request
app = Flask(__name__)

raw = pd.read_csv('http://hilpisch.com/tr_eikon_eod_data.csv',
                 index_col=0, parse_dates=True)

@app.route('/')
def main():
    symbols = request.args['symbols']
    if symbols == 'all':
        symbols = raw.columns
    else:
        symbols = symbols.split(',')
    out = request.args['format']
    no = int(request.args['no'])
    if out == 'html':
        return raw[symbols].iloc[-no:].to_html()
    elif out == 'json':
        return raw[symbols].iloc[-no:].to_json()
    else:
        return raw[symbols].iloc[-no:].to_csv()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777, debug=True)
