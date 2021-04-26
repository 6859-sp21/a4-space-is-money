import pandas as pd
pd.set_option("display.max_rows", None, "display.max_columns", None)

def get_mission_data():
    url = 'data.xlsx'
    old = pd.read_excel('data.xlsx', sheet_name = 'Mission Costs')
    mission_dfs = []

    # flatten the data for better formatting
    for name in old.columns[2:]:
      mission_dfs.append(old[['Fiscal Year',name]].melt('Fiscal Year', var_name='Mission', value_name='Cost')[3:])
    df = pd.concat(mission_dfs)

    missions_by_destination= {
    'Mars' : ['Mariner 3 & 4','Mariner 6 & 7','Early Mariner LVs','Mariner 8 & 9','Viking','Mars Data Analysis','Mars Observer','Mars \'94 NASA Cont.','Mars Pathfinder','Mars Exploration Program','InSight'],
    'Venus' : ['Mariner 1 & 2', 'Mariver 1 & 2 LV','Mariner 5','Mariner 5 LV','Pioneer Venus','Magellan'],
    'Mercury' :	['Mariner 10','MESSENGER'],
    'Outer Planets' : ['Pioneer 10 & 11','Voyager','Galileo','Cassini','Juno','Outer Planets Program','Europa Clipper'],
    'Moon' : ['Lunar Ranger','Lunar Orbiter','Lunar Surveyor','Lunar Prospector','GRAIL','Lunar Exploration Program'],
    'Small Bodies' : ['NEAR','Stardust','DS1','CONTOUR','Deep Impact','Dawn','New Horizons','OSIRIS-REx','Lucy','Psyche']
    }

    # add new column for destination
    mission_to_dest = {}
    for k in missions_by_destination:
      for m in missions_by_destination[k]:
        mission_to_dest[m] = k
    df['Destination'] = df.apply(lambda row: mission_to_dest.get(row['Mission'],'Other'), axis=1)

    df.
    df.reset_index(drop=True, inplace=True)
    df.to_csv('data/mission_data.csv')

def csv_to_json():
    pd.to_json(pd.read_csv('mission_data.csv'))

# def add_infl_adjusted_mission_data():
#     mission_data = pd.read_json('data/mission_data.json')
#     infl_rates = df.read_excel('data.xlsx', sheet_name='NNSI')
#
#     df['Inflation Adjusted Cost'] = df.apply(lambda row: row['Fiscal Year'])
