import streamlit as st

main_page = st.Page("main.py", title="Главная"
# , icon=":material/add_circle:"
)
bot_page = st.Page("bot.py", title="Чат-бот"
# , icon=":material/delete:"
)

pg = st.navigation(
    {
            "Main": [main_page, bot_page],
            # "Reports": []
        }
)
st.set_page_config(page_title="Lia ranepa bot"
# , page_icon=":material/edit:"
)
pg.run()




