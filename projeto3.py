import pandas
import plotly.express as pe
import plotly.figure_factory as ff
from dash import html,dcc,Dash
from matplotlib.pyplot import figure
import statsmodels.api as sm

df = pandas.read_csv("C:/Users/thiag/Downloads/ecommerce_estatistica.csv")

# Histograma de Nota
fig1 = pe.histogram(df,x="Nota",color_discrete_sequence=pe.colors.sequential.Greens_r,nbins=150,title="Histograma de Notas")
fig1.update_layout(
    xaxis_title="Intervalo de Notas",
    yaxis_title="Quantidade",
    height=400,
    width=1000
)

# Gráfico de dispersão de Nota_MinMax e Desconto_MinMax
fig2 = pe.scatter(df,x="Desconto_MinMax",y="Nota_MinMax",color_discrete_sequence=pe.colors.qualitative.Pastel)
fig2.update_layout(
    title="Gráfico de Dispersão Desconto_MinMax x Nota_MinMax",
    xaxis_title="Desconto",
    yaxis_title="Nota",
    height=600,
    width=900
)
# Mapa de calor
corr = df[["Qtd_Vendidos_Cod","N_Avaliações_MinMax"]].corr()

fig3 = pe.imshow(corr,zmin=0,zmax=1,
                labels=dict(x="Qtd_Vendidos_Cod", y="N_Avaliações_MinMax"),
                x=["Qtd_Vendidos_Cod","N_Avaliações_MinMax"],
                y=["Qtd_Vendidos_Cod","N_Avaliações_MinMax"],
                text_auto=True,color_continuous_scale=pe.colors.sequential.Bluered,
                title="Mapa de Calor - Correlação Qtd_Vendidos_Cod x N_Avaliações_MinMax"
               )

# Gráfico de Barra
fig4 = pe.histogram(df,x="Temporada_Cod",nbins=70)
fig4.update_layout(
     xaxis_title="Código",
     yaxis_title="Quantidade",
     title="Gráfico de Barras - Temporada_Cod"
 )

# Gráfico de Pizza
fig5 = pe.pie(df,names="Qtd_Vendidos",color="Qtd_Vendidos",hole=0.2,color_discrete_sequence=pe.colors.qualitative.Plotly,
              title="Gráfico de Pizza - Quantidade de produtos vendidos")

# Gráfico de Densidade
desconto=[df["Desconto"]]
legenda=["Desconto"]
fig6 = ff.create_distplot(desconto,legenda,show_hist=False)
fig6.update_layout(title_text="Gráfico de Densidade - Desconto",
                   height=800,
                   width=700)

# Gráfico de Regressão
fig7 = pe.scatter(df, x='Qtd_Vendidos_Cod', y='N_Avaliações_MinMax', opacity=0.65,trendline='ols', trendline_color_override='Green')
fig7.update_layout(
    title="Gráfico de Regressão - Qtd_Vendidos_Cod x N_Avaliações_MinMax"
)

app = Dash(__name__)
app.layout = html.Div([
    html.H1("Dashboard"),
    html.H2("Gráficos"),
    html.Br(),
    dcc.Graph(figure=fig1),
    dcc.Graph(figure=fig2),
    dcc.Graph(figure=fig3),
    dcc.Graph(figure=fig4),
    dcc.Graph(figure=fig5),
    dcc.Graph(figure=fig6),
    dcc.Graph(figure=fig7)
])

app.run_server(debug=True,port=8050)
