"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
import time


class State(rx.State):
    """The app state."""
    count: int = 0
    text: str = ""
    logged: bool = "False"
    len_input: int = 0
    items: list = [str(i+1) for i in range(10)]
    
    @rx.event
    def increment(self, num: int):
        self.count += 1

    @rx.event
    def send(self, text):
        self.text = text
        self.get_len_input()
    
    @rx.event
    def display_num(self):
        pass

    @rx.event
    def toggle_login(self):
        self.logged = not self.logged

    @rx.event
    def get_len_input(self):
        self.len_input = len(self.text)

    

def render_items(items: rx.Var[str]):
    return rx.list.item(items)
    

def index() -> rx.Component:
    # Welcome Page (Index)
    button = rx.button("click me")
    return rx.box(
        rx.hstack(
            rx.heading(State.count),
            rx.button(
                "Increment",
                on_click=lambda: State.increment(1),
            ),
            rx.input(
                placeholder="enter some text",
                on_blur=State.send
            ),
            rx.heading(State.text)
        ),
        rx.vstack(
            rx.cond(
                State.logged,
                rx.heading("Logged In"),
                rx.text("Not Logged In")
            ),
            rx.button("toggle login", on_click=State.toggle_login)
        ),
        rx.box(
            rx.cond(
                State.len_input > 5,
                rx.heading(State.len_input),
                rx.heading("Not sufficient text lenght")
            ),
            rx.foreach(State.items, render_items),
            rx.image(src="WhatsApp Image 2025-01-18 at 14.14.52.jpeg")
        )
    )

app = rx.App()
app.add_page(index, route="/")
