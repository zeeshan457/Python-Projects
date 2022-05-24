import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

color = sns.color_palette()
import plotly.graph_objs as go
import numpy as np

# Print the file contents
file = "C:\\Users\\zeeshan\\Desktop\\Solar_Flares_Dataset.xlsx"
File_Reader = pd.read_excel(file)


fig = px.scatter(File_Reader, x='X-class flares', y='spot distribution')
fig.update_traces(marker_color="turquoise",marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5)
fig.update_layout(title_text='X-class flares plot')
fig.show()

