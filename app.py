from flask import Flask
from flask_cors import CORS 
import pandas as pd
app =Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World'

@app.route('/list')
def print_list():   
    print("hey")
    df = pd.read_csv("leads_list_csv.csv")
    df.rename(columns={
        'Est. Sales Rank': 'Est_Sales_Rank',
        'Sales Rank (30 days)': 'Sales_Rank_30_days',
        'Sales Rank (90 days)':'Sales_Rank_90_days'
    }, inplace=True)
    print(df.head())
    df.columns = [col.replace(' ', '_') for col in df.columns]
    data=df.to_json(orient='records')
    return data

if __name__ == '__main__':
    app.run(debug=True)