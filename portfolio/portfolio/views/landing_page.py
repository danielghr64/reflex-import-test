import reflex as rx
from reflex_simpleicons import simpleicons

class LandingState(rx.State):
    experience_items:list[str] = ["International competitions", "Cultural Projects", "Step Up projectsx"]

def left_card() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.flex(
                rx.icon(tag="bird", size=30, align_self="center"),
                rx.heading("Daniel Ghr64", size="6", weight="bold"),
                spacing="2",
            ),
            rx.avatar(src="/pexels-di-lai-567499892-31537019.jpg", size="9"),
            rx.text("Python Developer"),
            rx.divider(),
            rx.vstack(
                rx.text("Specialisation: ", color="gray.500"),
                rx.vstack(
                    rx.text("Machine-learning", weight="bold", size="2"),
                    rx.text("and front-end developper", weight="bold", size="2"),
                    spacing="0",
                ),
                padding_left="1rem",
                align_items="start",
                width="100%",
            ),
            rx.vstack(
                rx.link(
                    rx.hstack(
                        rx.icon(tag="github"),
                        rx.text("GitHub"),
                    ),
                    href="#",
                    _hover={"text_decoration": "none"},
                ),
                rx.link(
                    rx.hstack(
                        rx.icon(tag="linkedin"),
                        rx.text("LinkedIn"),
                    ),
                    href="#",
                    _hover={"text_decoration": "none"},
                ),
                spacing="3",
                align_items="start",
                padding_left="1rem",
            ),
            rx.container(
                rx.button(
                    rx.hstack(
                        rx.text("Let's work together", size="3"),
                        justify_content="center",
                        width="100%",
                    ),
                    padding_x="1rem",
                    radius="full",
                    width="100%",  # Prend toute la largeur disponible
                    bg="#3182CE",
                    color="white",
                    _hover={"bg": "#2C5282"},
                    margin_top="1rem",  # Espacement supplémentaire
                ),
            ),
            align="center",
            spacing="4",
            height="calc(100vh - 2rem)",  # Ajustement de la hauteur
            padding_y="1rem",  # Marge interne haut/bas
        ),
        width="25%",
        height="calc(100vh - 2rem)",  # Réduit la hauteur de 2rem
        margin="1rem",
        box_shadow="lg",
        position="sticky",
        top="0",  # Ancrage en haut
        left="0",  # Ancrage à gauche
    )


def navbar() -> rx.Component:
    return rx.hstack(
        rx.flex(
            rx.link(
                rx.button(
                    "Home",
                    bg="transparent",
                    border="1px solid #E2E8F0",  # Bordure grise légère
                    radius="full",  # Forme ovale
                    _hover={
                        "bg": "rgba(255, 255, 255, 0.08)",  # Léger effet au survol
                        "transform": "scale(1.02)",  # Micro animation
                        "transition": "all 0.2s ease",
                    },
                    padding_x="1.5rem",
                    padding_y="0.75rem",
                ),
                href="/",
            ),
            rx.link(
                "My experiences",
                color_scheme="indigo",
                _hover={
                    "bg": "transparent",
                    "transform": "translateX(2px)",  # Petit déplacement horizontal
                    "transition": "all 0.2s ease",
                },
                href="/new/#experience_section",
            ),
            rx.link(
                "About Me",
                color_scheme="indigo",
                _hover={
                    "bg": "transparent",
                    "transform": "translateX(2px)",  # Petit déplacement horizontal
                    "transition": "all 0.2s ease",
                },
                href="#",
            ),
            rx.link(
                "Resume",
                color_scheme="indigo",
                _hover={
                    "bg": "transparent",
                    "transform": "translateX(2px)",  # Petit déplacement horizontal
                    "transition": "all 0.2s ease",
                },
                href="#",
            ),
            rx.link(
                "Contact",
                color_scheme="indigo",
                _hover={
                    "bg": "transparent",
                    "transform": "translateX(2px)",  # Petit déplacement horizontal
                    "transition": "all 0.2s ease",
                },
                href="#",
            ),
            spacing="4",
        ),
        rx.spacer(),
        rx.hstack(
            rx.color_mode.button(),
            rx.button(
                rx.hstack(
                    rx.text("Let's Talk", color="white"),
                    simpleicons("whatsapp", size=16, color="gray.400"),
                    spacing="2",
                    align_items="center",
                ),
                bg="transparent",
                border="1px solid #E2E8F0",  # Bordure grise légère
                radius="full",  # Forme ovale
                _hover={
                    "bg": "rgba(255, 255, 255, 0.08)",  # Léger effet au survol
                    "transform": "scale(1.02)",  # Micro animation
                    "transition": "all 0.2s ease",
                },
                padding_x="1.5rem",
                padding_y="0.75rem",
            ),
            spacing="4",
        ),
        width="100%",
        max_width="100vw",  # Nouvelle propriété importante
        padding_y="1em",
        position="sticky",
        top="0",
    )


def ghost_button(text: str, icon: str) -> rx.Component:
    return rx.button(
        rx.hstack(
            rx.text(text, color="white"),
            rx.icon(tag=icon, size=16, color="gray.400"),
            spacing="2",
            align_items="center",
        ),
        bg="transparent",
        border="1px solid #E2E8F0",  # Bordure grise légère
        radius="full",  # Forme ovale
        _hover={
            "bg": "rgba(255, 255, 255, 0.08)",  # Léger effet au survol
            "transform": "scale(1.02)",  # Micro animation
            "transition": "all 0.2s ease",
        },
        padding_x="1.5rem",
        padding_y="0.75rem",
    )


def text_link_button(text: str, icon: str) -> rx.Component:
    return rx.button(
        rx.hstack(
            rx.text(
                text,
                color="gray.500",
                _hover={"text_decoration": "underline"},
            ),
            rx.icon(tag=icon, size=16, color="gray.500"),
            spacing="2",
            align_items="center",
        ),
        bg="transparent",
        _hover={
            "bg": "transparent",
            "transform": "translateX(2px)",  # Petit déplacement horizontal
            "transition": "all 0.2s ease",
        },
        padding_x="0.5rem",
        padding_y="0.5rem",
        box_shadow="none",  # Supprime tout effet d'ombre
    )


def project_card() -> rx.Component:
    return rx.card(
        rx.link(
            rx.flex(
                simpleicons("github", color="gray.400"),
                rx.box(
                    rx.heading("Quick Start", size="4"),
                    rx.text("Get started with Reflex in 5 minutes.", size="3"),
                ),
                spacing="2",
                align_items="start",
                direction="column",
                width="100%",
            ),
            as_child=True,
        ),
        width=["100%", "45%", "45%"],
        aspect_ratio=1,
        # Utilisez 'style' pour définir les propriétés de background
        background="center/cover url('/identity picture.png')",
        border_radius="0.5rem",
        box_shadow="md",
        overflow="hidden",
        display="flex",
        align_items="center",
        justify_content="center",
        box_sizing="border-box",
    )

def experience_card() -> rx.Component:
    return rx.card(
        rx.inset(
            rx.image(
                src="/pexels-di-lai-567499892-31537019.jpg",
                width="100%",
                height="auto",
            ),
            side="top",
            pb="current",
        ),
        rx.text(
            "Reflex is a web framework that allows developers to build their app in pure Python."
        ),
        width="25vw",
    )

def experience_accordion(id: int | str, header: str) -> rx.Component:
    card = experience_card()
    return rx.accordion.item(
                header=header,
                content=rx.flex(
                    card,
                    card, 
                    card,
                ),
                value=str(id),
            ),

def experience_section() -> rx.Component:
    return rx.vstack(
        rx.button(
            rx.hstack(
                simpleicons("stackblitz", size=16, color="gray.400"),
                rx.text("Portfolio", color="white"),
                spacing="2",
                align_items="center",
            ),
            bg="transparent",
            border="1px solid #E2E8F0",
            radius="full",
            _hover={
                "bg": "rgba(255, 255, 255, 0.08)",
                "transform": "scale(1.02)",
                "transition": "all 0.2s ease",
            },
            padding_x="1.5rem",
            padding_y="0.75rem",
        ),
        rx.heading("Check out my featured projects", size="4", weight="bold"),
        rx.flex(
            rx.box( # Wrapper for the cards
                project_card(),
                project_card(),
                project_card(),
                project_card(),
                display="flex",
                flex_wrap="wrap",
                justify_content="center", # Distribute cards evenly
                gap="1em", # Add gap between cards
                width="100%",
                box_sizing="border-box", # Ensure padding is included in width
            ),
            padding="1rem",
            width="100%",
        ),
        rx.accordion.root(
            rx.foreach(
                LandingState.experience_items,
                lambda header, index: experience_accordion(index, header)
            ),
            width="100%",
            default_value="item_2",
        ),

        width="100%",
        id="experience_section",  # ID for scrolling
        
    )


def main_content() -> rx.Component:
    return rx.box(
        rx.vstack(
            navbar(),
            rx.flex(  # Utilisation de flex pour l'espacement et l'alignement
                rx.vstack(
                    rx.button(
                        rx.hstack(
                            rx.icon(tag="mail", size=20),
                            rx.text("Let's meet"),
                            spacing="2",
                            align_items="center",
                        ),
                        radius="large",
                        bg="#000000",
                        color="white",
                        _hover={"bg": "#2C5282"},
                    ),
                    rx.heading("Hello I'm Daniel Ghr64", size="9"),
                    rx.text("Développeur Python passionné par la création web", size="4"),
                    rx.hstack(
                        ghost_button("My Works", "grid-2x2"),
                        text_link_button("Download CV", "download"),
                        spacing="4",
                    ),
                    spacing="4",
                    # flex="1",  # Removed flex from here
                    align_items="start",  # Aligner au début
                    # justify_content="flex-start",  # Removed justify-content
                ),
                height="80vh", # Removed height, let content define it.
                width="100%",
                align_items="start",  # Center horizontally
                justify_content="center",  # Center Vertically
                flex_direction="column" # Stack items vertically
            ),
            experience_section(),
            rx.hstack(
                rx.text("More projects coming soon", size="2"),
                justify_content="center",
                align_items="center",
                padding="1rem",
            ),
            width="100%",
        ),
        width="100%",
        overflow_x="hidden",
        padding_x="1rem",
    )


def new_landing_page() -> rx.Component:
    return rx.flex(
        left_card(),
        main_content(),
        width="100%",
        # position="relative"
    )
