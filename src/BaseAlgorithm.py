from __future__ import annotations
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from BaseResult import BaseResult

class BaseAlgorithm:
    @staticmethod
    def visualize(result: BaseResult) -> None:
        #Objective function plotting
        x = range(1, len(result.objective_function_history) + 1)
        plt.plot(x, result.objective_function_history)
        plt.xlabel('Iteration')
        plt.ylabel('Objective Function Result')
        plt.title('Objective Function Plot at Every Iteration')
        plt.grid(True)
        plt.show()

    @staticmethod
    def visualize3D(result:BaseResult) -> None:
        n = result.state_history[-1].cube.values.shape[0]
        values = result.state_history[-1].cube.values

        x,y,z = [], [], []
        text = []

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    x.append(i)
                    y.append(j)
                    z.append(k)
                    text.append(str(values[i][j][k]))

        # Main 3D scatter plot with markers
        fig = go.Figure(data=[go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers+text',
            marker=dict(size=17, color='rgba(0, 51, 102, 0.9)', colorscale='Viridis', showscale=True, opacity=1),
            text=text,
            textposition='middle center',
            textfont=dict(size= 15, color='yellow')
        )])

        # Adding lines connecting dots in each x-plane
        for i in range(n):
            for j in range(n):
                x_plane1, y_plane1, z_plane1 = [], [], []
                x_plane2, y_plane2, z_plane2 = [], [], []
                x_plane3, y_plane3, z_plane3 = [], [], []
                for k in range(n):
                    #x dir
                    x_plane1.append(k)
                    y_plane1.append(j)
                    z_plane1.append(i)

                    #y dir
                    x_plane2.append(j)
                    y_plane2.append(k)
                    z_plane2.append(i)

                    #z dir
                    x_plane3.append(j)
                    y_plane3.append(i)
                    z_plane3.append(k)

                #x dir line
                fig.add_trace(go.Scatter3d(
                    x=x_plane1, y=y_plane1, z=z_plane1,
                    mode='lines',
                    line=dict(color='blue', width=2),
                    name=f'Plane x={i}'
                    ))

                #y dir line
                fig.add_trace(go.Scatter3d(
                    x=x_plane2, y=y_plane2, z=z_plane2,
                    mode='lines',
                    line=dict(color='blue', width=2),
                    name=f'Plane x={i}'
                    ))

                #z dir line
                fig.add_trace(go.Scatter3d(
                    x=x_plane3, y=y_plane3, z=z_plane3,
                    mode='lines',
                    line=dict(color='blue', width=2),
                    name=f'Plane x={i}'
                    ))

        fig.update_layout(scene=dict(
            xaxis=dict(visible=False, showgrid=False),
            yaxis=dict(visible=False, showgrid=False),
            zaxis=dict(visible=False, showgrid=False),
        ))

        # Show the plot
        fig.show()
