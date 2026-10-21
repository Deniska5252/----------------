import ollama
import streamlit as st 

from llm import MODEL, ask_ollama
from tasks import TASKS

st.title("Найди баг")
st.write("Выбери уровень и задание, исправь код и попроси Ollama помочь.")
level = st.selectbox("Сложность", list(TASKS))
tasks = TASKS[level]
number = st.selectbox("Задание", range(len(tasks)), format_func=lambda i: tasks[i]["title"])
task = tasks[number]
st.write(task["text"])
st.caption(f"{level} · {number + 1} из {len(tasks)}")

# Храним решения отдельно, чтобы они не терялись при смене уровня.
if "solutions" not in st.session_state:
    st.session_state.solutions = {}
code = st.text_area(
    "Твой код", value=st.session_state.solutions.get(task["id"], task["code"]),
    height=250, key=task["id"],
)
st.session_state.solutions[task["id"]] = code
hint = st.button("Подсказка")
review = st.button("Разобрать решение")
st.caption("Код не запускается. Ответ языковой модели может содержать ошибки.")

if hint or review:
    if not code.strip():
        st.warning("Сначала введи код.")
    else:
        try:
            with st.spinner("Ollama думает…"):
                answer = ask_ollama(task, code, hint, level)
            st.write(answer)
        except ConnectionError:
            st.error("Открой Ollama или запусти ollama serve в отдельном терминале.")
        except ollama.ResponseError as error:
            if error.status_code == 404:
                st.error(f"Сначала скачай модель: ollama pull {MODEL}")
            else:
                st.error("Ollama вернула ошибку. Проверь, что модель работает.")
        except Exception:
            st.error("Не удалось получить ответ. Проверь Ollama и попробуй снова.")
