import streamlit as st

marketing = st.Page("marketing.py", title="마케팅 대시보드", icon="🥇")
ecommerce = st.Page("ecommerce.py", title="이커머스 매출 대시보드", icon="🎁")
detail =st.Page("detail.py", title="Detailed Information", icon="🎨")
pg = st.navigation([marketing, ecommerce, detail])
pg.run()