
from flask import Flask, render_template,request
import pandas as pd
import json

app = Flask(__name__)

df_scatter = pd.DataFrame({
      'sales':  [2115, 1562, 1584, 1892, 1487, 2223, 2966, 2448, 2905, 3838, 2917, 3327],
      'orders':[958, 724, 629, 883, 915, 1214, 1476, 1212, 1554, 2128, 1466, 1827],
      'months': ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
   })
@app.route('/')
def apextutorialdropdown():
          
    sales = df_scatter['sales'].to_list()
    orders = df_scatter['orders'].to_list()
    months = df_scatter['months'].to_list()

    dataObject = {
        "sales":sales,
        "orders":orders,
        "months":months
    }
    res = json.loads(df_scatter.to_json(orient='records'))
    print(res)

    return render_template('index.html',dataObject=dataObject,res=res)
    
if __name__=="__main__":
    app.run(debug=True)