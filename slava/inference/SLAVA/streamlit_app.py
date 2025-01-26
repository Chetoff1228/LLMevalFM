import streamlit as st

main_page = st.Page("main.py", title="Описание"
)
Leaderboard_page = st.Page("Leaderboard.py", title="Лидерборд"
)

pg = st.navigation(
    {
            "Main": [Leaderboard_page, main_page],
        }
)
st.set_page_config(page_title="Leaderboard", layout="wide", page_icon="🏆",
)
pg.run()


