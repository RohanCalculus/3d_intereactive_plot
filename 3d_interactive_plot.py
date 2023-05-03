# -*- coding: utf-8 -*-
"""3D Interactive Plot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QtnpdT0dnHTdeZrVMqcxR-JyTRpy7XOG
"""

import plotly.graph_objs as go
import plotly.io as pio
import numpy as np

# Define the three planes
X, Y = np.meshgrid(np.arange(-10, 11), np.arange(-10, 11))
Z1 = (1 - X - 2 * Y) / 3.0
Z2 = (0 - 2 * X - 4 * Y) / 6.0
Z3 = (3 - 7 * X - 8 * Y) / 9.0

# Create traces for the three planes
trace1 = go.Surface(x=X, y=Y, z=Z1, opacity=0.5, colorscale='Viridis', name='x + 2y + 3z = 1', showscale=False, hovertemplate='x + 2y + 3z = 1')
trace2 = go.Surface(x=X, y=Y, z=Z2, opacity=0.5, colorscale='Magma', name='2x + 4y + 6z = 0', showscale=False, hovertemplate='2x + 4y + 6z = 0')
trace3 = go.Surface(x=X, y=Y, z=Z3, opacity=0.35, colorscale='Blues', name='7x + 8y + 9z = 3', showscale=False, hovertemplate='7x + 8y + 9z = 3')

# Create the figure
fig = go.Figure(data=[trace1, trace2, trace3])

# Set the layout
fig.update_layout(
    scene=dict(
        xaxis=dict(title='X', visible=False),
        yaxis=dict(title='Y', visible=False),
        zaxis=dict(title='Z', visible=False),
        aspectratio=dict(x=1, y=1, z=1),
        camera=dict(
            up=dict(x=0, y=0, z=1),
            center=dict(x=0, y=0, z=0),
            eye=dict(x=-0.8, y=-0.8, z=0.8)
        ),
        dragmode='orbit',
        ),
    title='Visualizing the System of given 3 equations for k = 2'
)

# Save the figure as an HTML file
pio.write_html(fig, file='3_planes.html', auto_open=True)