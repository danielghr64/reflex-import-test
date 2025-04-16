
import reflex as rx
import asyncio
import google.generativeai as genai

from chat_app import styles, env_var

genai.configure(api_key=env_var.GOOGLE_API_KEY)

# List all gemini models
# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)

model = genai.GenerativeModel('gemini-1.5-flash')

class State(rx.State):
    question: str
    chat_history: list[tuple[str, str]]

    @rx.event
    async def answer(self):
        answer = model.generate_content(self.question).text
        self.chat_history.append((self.question, answer))
        self.question = ""

        yield

        for i in range(len(answer)):
            # Pause to see the streaming effect
            await asyncio.sleep(0.01)
            # Add one letter at a time to the output
            self.chat_history[-1] = (
                self.chat_history[-1][0],
                answer[:i + 1]
            )
            yield

def qa(question: str, answer: str) -> rx.Component :
    return rx.box(
        rx.box(rx.text(question, style=styles.question_style), text_align="right"),
        rx.box(rx.text(answer, style=styles.answer_style), text_align="left"),
        margin_y="1em",
        width="100%"
    )


def chat_layout() -> rx.Component:
    qa_pairs = [
        (
            "What is Reflex",
            "A way to build web app"
        ), 
        (
            "What is Reflex",
            "A way to build web app"
        )
    ]
    return rx.box(
        rx.foreach(
            State.chat_history, 
            lambda messages: qa(messages[0], messages[1])
        )
    )

# Manage the flex latter

def action_bar() -> rx.Component:
    return rx.flex(
        rx.input(
            placeholder="Ask a question",
            style=styles.input_style,
            on_change=State.set_question # Le role de on_change est de modifier la valeur interne de question à chaque fois que la valeur dans l'input varie, et ce de manière automatique grae à set_question
        ),
        rx.button(
            "Ask",
            style=styles.button_style,
            on_click=State.answer
        )
    )


def index() -> rx.Component:
    return rx.container(
        rx.heading(State.question, align="center"),
        chat_layout(),
        action_bar(),
    )


app = rx.App()
app.add_page(index)

# next: Add styles
