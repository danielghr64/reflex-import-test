import reflex as rx
from reflex_simpleicons import simpleicons

from portfolio.css import styles
from .views.landing_page import new_landing_page

TITLES = ["Python junior developper", "3D designer", "Graduate from Culture.Ed"]

gradient_text_style_light = {
    "background": "linear-gradient(to left, #222222, #e1e1e1)",  # Dégradé de gris à blanc (de droite à gauche)
    "background_clip": "text",
    "display": "inline-block", 
}

data = [
    ["/github.png", "Github", "#"],
    ["/whatsapp.png", "WhatsApp", "#"],
    ["/linkedin.png", "Linkedin", "#"],
]


def header() -> rx.Component:
    return rx.hstack(
        rx.box(rx.icon(tag="mail")),  # Icône de mail
        rx.box(rx.text("danieltchonang101@gmail.com")),
        rx.spacer(),
        rx.color_mode.button(),
        width="100%",
        # margin_y="1em",
        padding="1em",
    )

def badges(title: str) -> rx.Component:
    return rx.badge(
        title,
        variant="solid",
        padding=[
            "0.15rem 0.35rem",
            "0.15rem 0.35rem",
            "0.15rem 1rem",
            "0.15rem 1rem",
            "0.15rem 1rem",
        ]
    )

def custom_breadcrumb() -> rx.Component:
    return rx.hstack(
        rx.link(simpleicons("github", size=16, color="gray.400"), "Github", href="https://github.com/danielghr64", target="_blank"),  # Lien avec icône
        rx.text("/"),  # Séparateur avec icône
        rx.link(simpleicons("whatsapp", size=16, color="gray.400"), "WhatsApp", href="https://cbl.link/knmWwpK", target="_blank"),  # Lien avec icône
        rx.text("/"),  # Séparateur avec icône
        rx.link(rx.icon(tag="linkedin", size=16), "Linkedin", href="#"),  # Lien avec icône
        spacing="2",  # Espacement entre les éléments
        style={"font_size": "1rem", }, # "font_weight": "bold"
    )

def footer() -> rx.Component:
    return rx.center(
        rx.text(
            "Copyright 2024 - 2025 DanielGhr64",
            font_size="10px",
            font_weight="semibold",
            align="center"
        ),
        style=styles.get("footer")
    )

def main() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.heading("Hi - I'm Daniel Ghr64",
                       font_weight="900",
                       font_size=["2rem", "2.85rem", "4rem", "5rem", "5rem"],
                       padding="1.2rem",
                       color="transparent",
                       style= gradient_text_style_light
            ),
            rx.heading(
                rx.icon(tag="smile", size=50), 
                style=styles.get("wave"),
            )
        ),

        rx.hstack(
            rx.foreach(TITLES, lambda title: badges(title)),
        ),
        custom_breadcrumb(),
        rx.center(
            rx.link("Click here to see my projects", href="/new/", font_size="1.2rem")
        ),
        style=styles.get("main").get("property"),
    )

def landing() -> rx.Component:
    return rx.vstack(
        header(),  # Ajouter la navbar,
        main(),
        footer(),
        background=rx.color_mode_cond(
            dark="radial-gradient(circle, rgba(255, 255, 255, 0.09) 1px, transparent 1px)",
            light="radial-gradient(circle, rgba(0, 0, 0, 0.35) 1px, transparent 1px)"
        ),
        background_size="25px 25px",
        align="center",
        style=styles.get("dots"),
    )

# Créer l'application Reflex
app = rx.App()
app.add_page(landing, route="/")  # Ajouter la page d'accueil
app.add_page(new_landing_page, route="new/")

# Modify app theme: accent -> gray
