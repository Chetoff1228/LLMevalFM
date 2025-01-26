import pandas as pd
import streamlit as st



def load_data():
    df_itog = pd.read_csv("ITOG.csv").set_index("Model")
    df_oblzn = pd.read_csv("oblzn.csv").set_index("Model")
    df_vidvopr = pd.read_csv("vidvopr.csv").set_index("Model")
    df_provokac = pd.read_csv("provokac.csv").set_index("Model")

    return df_itog, df_oblzn, df_vidvopr, df_provokac

def select_table(tables):
    table_choice = st.selectbox(
        "Выберите таблицу для отображения:",
        ["ITOG", "Область знаний", "Вид вопроса", "Провокационность"],
        index=0
    )
    
    return tables[table_choice]

def filter_itog_columns(df):
    st.markdown("### Фильтрация по отдельным колонкам:")
    
    selected_columns = st.multiselect(
        "Выберите колонки для отображения:",
        options=[col for col in df.columns if col != "Model"]
    )
    
    
    return df[selected_columns]

def filter_oblzn_columns(df):
    st.markdown("### Фильтрация по областям знаний:")

    knowledge_areas_dict = {
        "GEO": "География",
        "HIST": "История",
        "SOC": "Обществознание (социология)",
        "POL": "Политология и основы нац.безопасности",
        "ALL": "Все области"
    }

    knowledge_areas = list(knowledge_areas_dict.values())

    selected_columns = st.multiselect(
        "Выберите области знаний:",
        knowledge_areas
    )

    if 'Все области' in selected_columns or not selected_columns:
        return df
    else:
        selected_abbr = [abbr for abbr, full in knowledge_areas_dict.items() if full in selected_columns]

        filtered_columns = [col for col in df.columns if any(abbr in col for abbr in selected_abbr)]
        
        return df[filtered_columns]


def filter_vidvopr_columns(df):
    st.markdown("### Фильтрация по виду вопроса:")

    question_types_dict = {
        "multich": "multichoice (мультивыбор)",
        "onech": "one choice (вопрос с одним правильным ответом)",
        "seq": "sequence (последовательность)",
        "map": "mapping (сопоставление)",
        "ALL": "Все типы"
    }

    question_types = list(question_types_dict.values())

    selected_columns = st.multiselect(
        "Выберите типы вопросов:",
        question_types
    )

    if 'Все типы' in selected_columns or not selected_columns:
        return df
    else:
        selected_abbr = [abbr for abbr, full in question_types_dict.items() if full in selected_columns]

        filtered_columns = [col for col in df.columns if any(abbr in col for abbr in selected_abbr)]
        
        return df[filtered_columns]


def filter_provokac_columns(df):
    st.markdown("### Фильтрация по уровню провокативности:")

    provocation_levels_dict = {
        "PROVOC_1": "1ый уровень провокативности",
        "PROVOC_2": "2ой уровень провокативности",
        "PROVOC_3": "3ий уровень провокативности",
        "ALL": "Все уровни"
    }

    provocation_levels = list(provocation_levels_dict.values())

    selected_columns = st.multiselect(
        "Выберите уровни провокативности:",
        provocation_levels
    )

    if 'Все уровни' in selected_columns or not selected_columns:
        return df
    else:
        selected_abbr = [abbr for abbr, full in provocation_levels_dict.items() if full in selected_columns]

        filtered_columns = [col for col in df.columns if any(abbr in col for abbr in selected_abbr)]
        
        return df[filtered_columns]




st.title("Leaderboard")

df_itog, df_oblzn, df_vidvopr, df_provokac = load_data()

tables = {
    "ITOG": df_itog,
    "Область знаний": df_oblzn,
    "Вид вопроса": df_vidvopr,
    "Провокационность": df_provokac
}

df_selected = select_table(tables)

if st.checkbox("Добавить фильтры"):
    if df_selected is df_itog:
        df_selected = filter_itog_columns(df_selected)
    elif df_selected is df_oblzn:
        df_selected = filter_oblzn_columns(df_selected)
    elif df_selected is df_vidvopr:
        df_selected = filter_vidvopr_columns(df_selected)
    elif df_selected is df_provokac:
        df_selected = filter_provokac_columns(df_selected)

st.dataframe(df_selected, use_container_width=True, width=5000)

st.download_button(
    "Скачать таблицу в формате CSV",
    df_selected.to_csv(index=True),
    "filtered_table.csv",
    "text/csv"
)
st.write('---')

st.write("""
### Описание структуры названий колонок:

#### Части, отвечающие за область знаний:
- **GEO** - география
- **HIST** - история
- **SOC** - обществознание (социология)
- **POL** - политология и основы национальной безопасности

#### Части, отвечающие за вид вопроса:
- **NUM_Q** или **_num_q_** - вопрос с числовым ответом, с делением на:
  - **_multich_** - "multichoice", мультивыбор
  - **_onech_** - "one choice", вопрос с одним правильным ответом
  - **_seq_** - "sequence", последовательность
  - **_map_** - "mapping", соответствие
- **OPEN_Q** или **_open_q_** - открытый вопрос, подразумевающий свободный письменный ответ

#### Части, отвечающие за уровень провокативности:
- **PROVOC_1** - первый уровень провокативности
- **PROVOC_2** - второй уровень провокативности
- **PROVOC_3** - третий уровень провокативности

#### Части, указывающие метрику:
- **_EM** - "exact match", ответ модели точно совпадает с правильным
- **_CC** - "contains check", ответ модели содержит правильный ответ
- **_PM** - "partially match", ответ модели частично верный
- **_F1** - метрика f1-score
- **_LR** - "levenshtein ratio", мера схожести ответа модели с эталонным, на основе расстояния Левенштейна

---

### Структура таблиц:
В таблице представлены три обобщенные вкладки по каждому срезу:
- **Область знаний**
- **Вид вопроса**
- **Уровень провокативности**

Также присутствует таблица **ИТОГ**, представляющая итоговый рейтинг. Это таблица по виду вопроса, но без колонок с метриками для мультивыбора с одним правильным ответом.
""")

st.write("### `Ссылки/контакты`")

st.write("[GitHub](https://github.com/ikanam-ai/slava)")
st.write("[Dataset](https://huggingface.co/datasets/RANEPA-ai/SLAVA-OpenData-2800-v1)")

