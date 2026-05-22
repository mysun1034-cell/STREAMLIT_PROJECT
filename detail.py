# detail.py
import streamlit as st
import pandas as pd
from marketing import load_marketing
from ecommerce import load_ecommerce

# 데이터 선택 탭
tab1, tab2 = st.tabs(["📣 마케팅", "🛒 이커머스"])

with tab1:
    df = load_marketing().copy()
    with st.form("marketing_search"):
        keyword = st.text_input("키워드 검색")
        submitted = st.form_submit_button("검색")
    if submitted and keyword:
        mask = df.apply(lambda row: keyword.lower() in str(row).lower(), axis=1)
        filtered = df[mask]
        st.write(f"'{keyword}' 검색 결과: {len(filtered):,}행")
        st.dataframe(filtered.head(20))

with tab2:
    df = load_ecommerce().copy()
    with st.form("ecommerce_search"):
        keyword = st.text_input("키워드 검색")
        submitted = st.form_submit_button("검색")
    if submitted and keyword:
        mask = df.apply(lambda row: keyword.lower() in str(row).lower(), axis=1)
        filtered = df[mask]
        st.write(f"'{keyword}' 검색 결과: {len(filtered):,}행")
        st.dataframe(filtered.head(20))

st.divider()
uploaded = st.file_uploader("내 데이터 업로드 (CSV)", type=["csv"])
if uploaded is not None:
    user_df = pd.read_csv(uploaded)
    st.success(f"{uploaded.name} ({len(user_df):,}행)")
    st.dataframe(user_df.describe())