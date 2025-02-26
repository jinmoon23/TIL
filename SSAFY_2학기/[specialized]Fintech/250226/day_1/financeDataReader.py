import FinanceDataReader as fdr
import plotly.graph_objects as go
df = fdr.DataReader('005930') # 2020-01-01 ~ 현재

print(df)

fig = go.Figure(data=[go.Candlestick(x=df.index,
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'],
                increasing_line_color= 'red', decreasing_line_color= 'blue',
                )],)
fig.show()