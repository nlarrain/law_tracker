import pandas as pd
import scraper

# Run the scraper
#scraper.scrape_now()

# Read the latest scrape and compare against the database to
# see the new and old ones
data = pd.read_csv('results.csv', header = 0)
base = pd.read_csv('base.csv', header = 0)

# Grupos de boletines
new = data[~data['boletin'].isin(base['boletin'])]['boletin']
closed = base[~base['boletin'].isin(data['boletin'])]['boletin']

# Grupos de Interes
new_projects = data[data['boletin'].isin(new)]
closed_projects = base[base['boletin'].isin(closed)]
updated_projects = base.merge(data, how='inner', on='boletin', suffixes=['_1', '_2'])
updated_projects = updated_projects.query('status_1 != status_2').dropna()

# Columnas a seleccionar
cols_new = ['fecha', 'boletin', 'titulo', 'status']
cols_updated = ['fecha_1', 'boletin', 'titulo_1', 'status_1', 'status_2']

# Dataframes finales
new_projects = new_projects[cols_new]
updated_projects = updated_projects[cols_updated]
updated_projects.columns = ['fecha', 'boletin', 'titulo', 'estado_antiguo', 'estado_nuevo']

if pd.concat([new_projects, closed_projects, updated_projects], axis =1).shape[0]==0:
    with pd.ExcelWriter('output.xlsx') as writer:
      title = 'No Changes!'
      new_projects.to_excel(writer, sheet_name=title)

else:
    # Export to Excel
    with pd.ExcelWriter('output.xlsx') as writer:
      title = 'New'
      new_projects.to_excel(writer, sheet_name=title , index=False)
      title = 'Closed'
      closed_projects.to_excel(writer, sheet_name=title, index=False)
      title = 'Modified'
      updated_projects.to_excel(writer, sheet_name=title, index=False)

# Actualizamos el archivo base
data.to_csv('base.csv', index = False)
