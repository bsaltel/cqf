#
# Simple FXCM Tick Data API
# based on Flask
#
import pandas as pd
from flask import Flask, request
app = Flask(__name__)

raw = pd.read_hdf('data.h5', 'data')

@app.route('/')
def main():
    start = request.args['start']
    end = request.args['end']
    out = request.args['format']
    data = raw.loc[start:end]
    if out == 'html':
        return data.to_html()
    elif out == 'json':
        return data.to_json()
    else:
        return data.to_csv()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)
