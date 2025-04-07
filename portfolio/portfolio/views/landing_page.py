import reflex as rx
from reflex_simpleicons import simpleicons

def left_card() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.hstack(
                rx.icon(tag="bird", size=30, align_self="center"),
                rx.heading(
                    "Daniel Ghr64", 
                    size="7",
                    color=rx.color_mode_cond(light="gray.800", dark="white")
                ),
                align_items="center",
            ),
            
            rx.avatar(src="/identity picture.png", size="9"),
            rx.text(
                "Python Developer",
                color=rx.color_mode_cond(light="gray.600", dark="gray.300")
            ),
            rx.divider(),
            rx.vstack(
                rx.text(
                    "Specialisation: ", 
                    color=rx.color_mode_cond(light="gray.500", dark="gray.400")
                ),
                rx.list.unordered(
                    rx.list_item(
                        rx.text("Machine-learning", font_weight="bold")
                    ),
                    rx.list_item(
                        rx.text("Front-end Developper", font_weight="bold")
                    ),
                    spacing="2",
                    color=rx.color_mode_cond(light="gray.700", dark="gray.200")
                ),
                padding_left="1rem",
                align_items="start",
                width="100%",
            ),
            rx.vstack(
                rx.link(
                    rx.hstack(
                        rx.icon(tag="github"),
                        rx.text(
                            "GitHub",
                            color=rx.color_mode_cond(light="gray.700", dark="white")
                        ),
                    ),
                    href="#",
                    _hover={"text_decoration": "none"}
                ),
                rx.link(
                    rx.hstack(
                        rx.icon(tag="linkedin"),
                        rx.text(
                            "LinkedIn",
                            color=rx.color_mode_cond(light="gray.700", dark="white")
                        ),
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
            height="calc(100vh - 2rem)",
            padding_y="1rem"
        ),
        width="20%",
        height="calc(100vh - 2rem)",
        margin="1rem",
        box_shadow="lg",
        position="sticky",
        top="0",
        left="0",
        bg=rx.color_mode_cond(light="white", dark="gray.800")
    )

def navbar() -> rx.Component:
    return rx.hstack(
        rx.flex(
            rx.link(
                rx.button(
                    "Home",
                    color=rx.color_mode_cond(light="gray.800", dark="white"),
                    bg="transparent",
                    border=rx.color_mode_cond(light="1px solid #E2E8F0", dark="1px solid #2D3748"),
                    radius="full",
                    _hover={
                        "bg": rx.color_mode_cond(light="rgba(0,0,0,0.05)", dark="rgba(255,255,255,0.08)"),
                        "transform": "scale(1.02)",
                        "transition": "all 0.2s ease"
                    },
                    padding_x="1.5rem",
                    padding_y="0.75rem"
                ),
                href="#"
            ),
            rx.link(
                "About Me", 
                color=rx.color_mode_cond(light="gray.600", dark="gray.400"),
                _hover={
                    "color": rx.color_mode_cond(light="gray.800", dark="white"),
                    "transform": "translateX(2px)",
                    "transition": "all 0.2s ease"
                },
                href="#"
            ),
            rx.link(
                "Resume",
                color=rx.color_mode_cond(light="gray.600", dark="gray.400"),
                _hover={
                    "color": rx.color_mode_cond(light="gray.800", dark="white"),
                    "transform": "translateX(2px)",
                    "transition": "all 0.2s ease"
                },
                href="#"
            ),
            rx.link(
                "Contact",
                color=rx.color_mode_cond(light="gray.600", dark="gray.400"),
                _hover={
                    "color": rx.color_mode_cond(light="gray.800", dark="white"),
                    "transform": "translateX(2px)",
                    "transition": "all 0.2s ease"
                },
                href="#"
            ),
            spacing="4",
        ),
        rx.spacer(),
        rx.hstack(
            rx.color_mode.button(),
            rx.button(
                rx.hstack(
                    rx.text(
                        "Let's Talk", 
                        color=rx.color_mode_cond(light="gray.800", dark="white")
                    ),
                    simpleicons(
                        "whatsapp", 
                        size=16, 
                    ),
                    spacing="2",
                    align_items="center"
                ),
                bg="transparent",
                border=rx.color_mode_cond(light="1px solid #E2E8F0", dark="1px solid #2D3748"),
                radius="full",
                _hover={
                    "bg": rx.color_mode_cond(light="rgba(0,0,0,0.05)", dark="rgba(255,255,255,0.08)"),
                    "transform": "scale(1.02)",
                    "transition": "all 0.2s ease"
                },
                padding_x="1.5rem",
                padding_y="0.75rem"
            ),
            spacing="4",
        ),
        width="100%",
        max_width="100vw",
        padding_y="1em",
        position="sticky",
        top="0",
        z_index="1000",
        bg=rx.color_mode_cond(light="rgba(255,255,255,0.8)", dark="rgba(26,32,44,0.8)"),
        backdrop_filter="blur(10px)"
    )

def ghost_button(text: str, icon: str) -> rx.Component:
    return rx.button(
        rx.hstack(
            rx.text(
                text, 
                color=rx.color_mode_cond(light="gray.800", dark="white")
            ),
            rx.icon(
                tag=icon, 
                size=16, 
                color=rx.color_mode_cond(light="gray.600", dark="gray.400")
            ),
            spacing="2",
            align_items="center"
        ),
        bg="transparent",
        border=rx.color_mode_cond(light="1px solid #E2E8F0", dark="1px solid #2D3748"),
        radius="full",
        _hover={
            "bg": rx.color_mode_cond(light="rgba(0,0,0,0.05)", dark="rgba(255,255,255,0.08)"),
            "transform": "scale(1.02)",
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
                color=rx.color_mode_cond(light="gray.600", dark="gray.400"),
                _hover={
                    "color": rx.color_mode_cond(light="gray.800", dark="white"),
                    "text_decoration": "underline"
                }
            ),
            rx.icon(
                tag=icon, 
                size=16, 
                color=rx.color_mode_cond(light="gray.600", dark="gray.400")
            ),
            spacing="2",
            align_items="center"
        ),
        bg="transparent",
        _hover={
            "bg": "transparent",
            "transform": "translateX(2px)",
            "transition": "all 0.2s ease"
        },
        padding_x="0.5rem",
        padding_y="0.5rem",
        box_shadow="none"
    )

def main_content() -> rx.Component:
    return rx.box(
        rx.vstack(
            navbar(),
            rx.flex(
                rx.vstack(
                    rx.button(
                        rx.hstack(
                            rx.icon(tag="mail", size=20),
                            rx.text(
                                "Let's meet",
                                color="white"
                            ),
                            spacing="2",
                            align_items="center",
                        ),
                        bg=rx.color_mode_cond(light="gray.800", dark="blue.600"),
                        color="white",
                        _hover={"bg": rx.color_mode_cond(light="gray.700", dark="blue.500")},
                    ),
                    rx.heading(
                        "Hello I'm Daniel Ghr64", 
                        size="9",
                        color=rx.color_mode_cond(light="gray.800", dark="white")
                    ),
                    rx.text(
                        "Développeur Python passionné par la création web", 
                        size="4",
                        color=rx.color_mode_cond(light="gray.600", dark="gray.300")
                    ),
                    rx.hstack(
                        ghost_button("My Works", "grid-2x2"),
                        text_link_button("Download CV", "download"),
                        spacing="4",
                    ),
                    spacing="4",
                    flex="1",
                    align_items="start",
                    justify_content="flex-start",
                ),
                height="80vh",
                width="100%",
                align_items="center",
                justify_content="flex-start",
            ),
            width="100%",
        ),
        width="100%",
        overflow_x="hidden",
        padding_x="1rem",
        bg=rx.color_mode_cond(light="gray.50", dark="gray.900")
    )
    

def new_landing_page() -> rx.Component:
    return rx.flex(
        left_card(),
        main_content(),
        width="100%",
        bg=rx.color_mode_cond(light="gray.50", dark="gray.900")
    )