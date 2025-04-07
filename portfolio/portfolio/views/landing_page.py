import reflex as rx
from reflex_simpleicons import simpleicons

def left_card() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.hstack(
                rx.icon(tag="bird", size=30, align_self="center"),
                rx.heading("Daniel Ghr64", size="7"),
                align_items="center",
            ),
            
            rx.avatar(src="/identity picture.png", size="9"),
            rx.text("Python Developer"),
            rx.divider(),
            rx.vstack(
                rx.text("Specialisation: ", color="gray.500"),
                rx.list.unordered(
                    rx.list_item(
                        rx.text("Machine-learning", font_weight="bold")
                    ),
                    rx.list_item(
                        rx.text("Front-end Developper", font_weight="bold")
                    ),
                    spacing="2",
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
                    _hover={"text_decoration": "none"}
                ),
                rx.link(
                    rx.hstack(
                        rx.icon(tag="linkedin"),
                        rx.text("LinkedIn"),
                    ),
                    href="#",
                    _hover={"text_decoration": "none"}
                ),
                spacing="3",
                align_items="start",
                padding_left="1rem"
            ),
            align="center",
            spacing="4",
            height="calc(100vh - 2rem)",  # Ajustement de la hauteur
            padding_y="1rem"  # Marge interne haut/bas
        ),
        width="20%",
        height="calc(100vh - 2rem)",  # Réduit la hauteur de 2rem
        margin="1rem",
        box_shadow="lg",
        position="sticky",
        top="0",  # Ancrage en haut
        left="0"  # Ancrage à gauche
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
                        "transition": "all 0.2s ease"
                    },
                    padding_x="1.5rem",
                    padding_y="0.75rem"
                ),
            ),
            rx.link("About Me", color="gray.500",
                    _hover={
                        "bg": "transparent",
                        "transform": "translateX(2px)",  # Petit déplacement horizontal
                        "transition": "all 0.2s ease"
                    },
                    href="#"),
            rx.link("Resume", color="gray.500",
                    _hover={
                        "bg": "transparent",
                        "transform": "translateX(2px)",  # Petit déplacement horizontal
                        "transition": "all 0.2s ease"
                    },
                    href="#"),
            rx.link("Con", color="gray.500",
                    _hover={
                        "bg": "transparent",
                        "transform": "translateX(2px)",  # Petit déplacement horizontal
                        "transition": "all 0.2s ease"
                    },
                    href="#"),
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
                align_items="center"
                ),
                bg="transparent",
                border="1px solid #E2E8F0",  # Bordure grise légère
                radius="full",  # Forme ovale
                _hover={
                    "bg": "rgba(255, 255, 255, 0.08)",  # Léger effet au survol
                    "transform": "scale(1.02)",  # Micro animation
                    "transition": "all 0.2s ease"
                },
                padding_x="1.5rem",
                padding_y="0.75rem"
            ),
            spacing="4",
        ),
        width="100%",
        max_width="100vw",  # Nouvelle propriété importante
        # padding_x="1em",    # Padding horizontal seulement
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
            align_items="center"
        ),
        bg="transparent",
        border="1px solid #E2E8F0",  # Bordure grise légère
        radius="full",  # Forme ovale
        _hover={
            "bg": "rgba(255, 255, 255, 0.08)",  # Léger effet au survol
            "transform": "scale(1.02)",  # Micro animation
            "transition": "all 0.2s ease"
        },
        padding_x="1.5rem",
        padding_y="0.75rem"
    )

def text_link_button(text: str, icon: str) -> rx.Component:
    return rx.button(
        rx.hstack(
            rx.text(
                text, 
                color="gray.500",
                _hover={"text_decoration": "underline"}
            ),
            rx.icon(tag=icon, size=16, color="gray.500"),
            spacing="2",
            align_items="center"
        ),
        bg="transparent",
        _hover={
            "bg": "transparent",
            "transform": "translateX(2px)",  # Petit déplacement horizontal
            "transition": "all 0.2s ease"
        },
        padding_x="0.5rem",
        padding_y="0.5rem",
        box_shadow="none"  # Supprime tout effet d'ombre
    )

def main_content() -> rx.Component:
    return rx.box(
        rx.vstack(
            navbar(),
            rx.flex( # Utilisation de flex pour l'espacement
                rx.vstack(
                    rx.button(
                        rx.hstack(
                            rx.icon(tag="mail", size=20),
                            rx.text("Let's meet"),
                            spacing="2",
                            align_items="center",
                        ),
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
                    flex="1", # Le contenu prendra l'espace restant
                    align_items="start", # Aligner au début
                    justify_content="flex-start", # Aligner au début
                ),
                height="80vh",
                width="100%",
                align_items="center",
                justify_content="flex-start", # Aligner le contenu au début verticalement
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

