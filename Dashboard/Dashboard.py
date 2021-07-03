import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from Data.dataframe_maker import DataMaker

from static import LejziTime as lTime

app = dash.Dash(__name__)
lt = lTime()
# data returns {'city':df}
data = DataMaker('WH','x', lt.x_days_ago_till_now(7), 2).get_data()



def labels(labels):
    options = []
    if type(labels) != str:
        for l in labels:
            label = {'label': f'{l}', 'value': l}
            options.append(label)
    else:
        label = {'label': f'{labels}', 'value': labels}
        options.append(label)
    return options



def create_dashboard(app, label, data_cat = 'weather'):

    app.layout = html.Div([

    dcc.Dropdown(id='tmax', options=label, multi=False),


    html.Div(id='output_cont', children=[]),

    html.Br(),

    dcc.Graph(id='map', figure={})
    ])

@app.callback(
    [Output(component_id='output_cont', component_property='children'),
    Output(component_id='map', component_property='figure')],
    [Input(component_id='year', component_property='value')])

def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))
    container = f'year{option_slctd}'

    dff = data.values()
    names = data.keys()
    dff = [df for df in dff]
    dff = [df[df['time'] == option_slctd] for df in dff]



    return container

label = [df.keys() for df in data.values()]
label = label[0].values


print(label)
label = labels(label)
print(label)

data = data['Gdańsk']
data = data['tmax']
label = 'tmax'
label = labels(label)

dash = create_dashboard(app, label)


app.run_server()
