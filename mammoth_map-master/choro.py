import pandas, folium, json

data = pandas.read_csv('mammoth_data.csv')

quantities = data['abd']
quantities = quantities.fillna(value=1)

data['quantity'] = quantities

state_data_groups = data.groupby(by=['state']).sum().reset_index()

states_abbr = json.load(open('us_states_abbr.json'))
state_list = list(states_abbr.keys())

all_states_zeros = pandas.DataFrame({'state': state_list, 'quantity': 0})

all_states_data = state_data_groups.append(all_states_zeros)

all_states_data = all_states_data.drop_duplicates('state', keep='first')

state_data_groups = all_states_data.replace(states_abbr)

print(state_data_groups)

us_states_file = r'us_states.json'

choromap = folium.Map(location=[40, -120], zoom_start=3)

choromap.choropleth(
    geo_path=us_states_file,
    data=state_data_groups,
    columns=['state', 'quantity'],
    key_on='id',
    fill_color='BuPu', fill_opacity=0.6, line_opacity=0.4,
    threshold_scale=[0,5,10,15,20,90],
    legend_name='Mammoth Finds Per State'
)

choromap.save('mammoth_choropleth.html')