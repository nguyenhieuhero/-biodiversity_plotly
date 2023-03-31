import pandas as pd
import plotly.express as px



def wl_ep():
    df = pd.read_csv('data\wildlife-exports.csv')
    df = df.drop(['Code'], axis=1)
    df = df.drop(df[df['Entity'] == 'Total'].index)
    df = df.drop(df[df['Entity'] == 'Plants'].index)

    # Load data

    # Create figure using plotly express
    fig = px.line(df, x="Year", y="Exported organisms", color="Entity",
                hover_data=["Entity"],
                labels={"Year": "<b>Year</b>", "Exported organisms": "<b>Exported organisms</b>"},
                markers=True,
                width=1000
                )



    # Update layout
    fig.update_layout(
        title="<b>Wildlife Exports by Entity</b>",
        xaxis=dict(
            tickvals=[1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2014],
            tickformat="d",
            title_font=dict(size=18, family="Arial"),
            tickfont=dict(size=14, family="Arial"),
            gridcolor="#e4e4e4",
            gridwidth=2
        ),
        yaxis=dict(
            tickvals=[1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000],
            ticktext=['1 million', '2 million', '3 million', '4 million', '5 million', '6 million', '7 million'],
            tickformat=",.0f",
            title_font=dict(size=18, family="Arial"),
            tickfont=dict(size=14, family="Arial"),
            gridcolor="#e4e4e4",
            gridwidth=2
        ),
        hoverlabel=dict(
            bgcolor="white",
            font_size=14,
            font_family="Arial"
        ),
        legend=dict(
            font=dict(size=14, family="Arial"),
            traceorder="normal",
            title="<b>Entity</b>",
            bgcolor="#F5F5F5",
            bordercolor="#d9d9d9",
            borderwidth=1,
            orientation="v",
            yanchor="auto",
            y=1.05,
            xanchor="auto",
            x=1.1
        ),
        title_font=dict(size=24, family="Arial"),
        plot_bgcolor="white",
    )

    return fig
