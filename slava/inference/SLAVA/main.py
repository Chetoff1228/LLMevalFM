import streamlit as st

st.title("SLAVA")
st.write('### Бенчмарк социально-политического ландшафта и ценностного анализа')

html_code = '''
<div style="text-align: center;">
    <a href="https://huggingface.co/datasets/RANEPA-ai/SLAVA-OpenData-2800-v1">
        <img src="https://raw.githubusercontent.com/Y1OV/project_lab/refs/heads/main/data/logo_ru.png" alt="Foo" style="width: 50%; height: auto;">
    </a>
</div>
'''

st.markdown(html_code, unsafe_allow_html=True)


st.write("""

С 2024 года был разработан бенчмарк SLAVA, содержащий около 14 тысяч вопросов для российского домена из таких областей, как история, политология, социология, политическая география и основы национальной безопасности. Этот бенчмарк оценивает способности больших языковых моделей (LLM) справляться с чувствительными темами, важными для российского информационного пространства.

#### Основные задачи:
- Проверка фактических знаний LLM в российских доменах.
- Оценка чувствительности (провокативности) вопросов.
- Создание комплексной системы оценки на основе точности ответов.

#### Структура:
Вопросы делятся на следующие типы:
- Мультивыбор с одним или несколькими правильными ответами.
- Последовательности и соответствия.
- Открытые ответы.

#### Провокативность вопросов:
- **1 балл**: Низкая чувствительность — общепризнанные факты.
- **2 балла**: Средняя чувствительность — спорные темы.
- **3 балла**: Высокая чувствительность — политические и культурные вопросы, вызывающие конфликты.

#### Результаты:
Были протестированы 24 LLM, поддерживающие русский язык. Модели от компаний **GigaChat**, **YandexGPT** и **qwen2** показали наивысшую точность и способность справляться с сложными, провокативными вопросами. В то время как некоторые модели, такие как **llama2** и **mixtral**, продемонстрировали более слабые результаты.

Этот бенчмарк подчеркивает необходимость дальнейших исследований в области надежности LLM, особенно в контексте социально-политических тем, значимых для России.
""")

st.write("### `Ссылки/контакты`")

st.write("[GitHub](https://github.com/ikanam-ai/slava)")
st.write("[Dataset](https://huggingface.co/datasets/RANEPA-ai/SLAVA-OpenData-2800-v1)")

st.write("### `Цитирование`")

code = r'''
@misc{SLAVA: Benchmark of Sociopolitical Landscape and Value Analysis,
  author = {A. S. Chetvergov, 
R. S. Sharafetdinov, 
M. M. Polukoshko, 
V. A. Akhmetov, 
N. A. Oruzheynikova,
I. S. Alekseevskaya,
E. S. Anichkov, 
S. V. Bolovtsov},
  title = {SLAVA: Benchmark of Sociopolitical Landscape and Value Analysis (2024)},
  year = {2024},
  publisher = {Hugging Face},
  howpublished = "\url{https://huggingface.co/datasets/RANEPA-ai/SLAVA-OpenData-2800-v1}"
}
    '''

st.code(code, language='python')