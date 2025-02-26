import FinanceDataReader as fdr
import streamlit as st
import plotly.graph_objects as go

df = fdr.DataReader('005930', '2025') # 2020-01-01 ~ 현재

fig = go.Figure(data=[go.Candlestick(      # DataFrame 인덱스를 날짜로 사용
    open=df['Open'],   # 시가
    high=df['High'],   # 고가
    low=df['Low'],     # 저가
    close=df['Close']  # 종가
)])


st.title('삼성전자 주식 차트')
st.plotly_chart(fig)
st.table(df)