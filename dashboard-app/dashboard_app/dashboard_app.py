
import reflex as rx

from rxconfig import config
from collections import Counter


class User(rx.Base):
    name: str 
    email: str
    gender: str
    id: int = 0  # Variable de classe pour suivre l'ID

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = User.id  # Attribuer l'ID actuel à l'instance
        User.id += 1  # Incrémenter l'ID pour la prochaine instance
    

class State(rx.State):
    users: list[User] = [
        User(name="Danilo Sousa",
             email="danilo@gmail.com",
             gender="Male"),  
        User(name="Zahra Ambessa",
             email="email2",
             gender="Female")
    ]

    user_for_graph: list[dict] = []

    @rx.event
    def add_user(self, form_data: dict):
        self.users.append(User(**form_data))
        self.transform_data()

    @rx.event
    def transform_data(self):
        gender_counts = Counter(
            user.gender for user in self.users
        )

        self.user_for_graph = [
            {"name": gender_group, "value": count}
            for gender_group, count in gender_counts.items()
        ]
    
    
def render_users(user: User):
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.email),
        rx.table.cell(user.gender),
        style={"hover":
            {"bg": rx.color("gray", 3)}
        },
        align="center"
    )


def dialog() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("plus", size=26),
                rx.text("Add user", size="4")
            )
        ),
        rx.dialog.content(
            rx.dialog.title("Add new users"),
            rx.dialog.description("Fill the form with the user's info"),
            
            rx.form(
                rx.flex(
                    rx.input(
                        placeholder="User name", name="name", required=True
                    ), 
                    rx.input(
                        placeholder="user;@reflex.dev",
                        name="email"
                    ),
                    rx.select(
                        ["Male", "Female"],
                        placeholder="Male",
                        name="gender"
                    ),
                    rx.flex(
                        rx.dialog.close(
                            rx.button("Cancel", variant="soft", color_scheme="gray"),
                        ),
                        rx.dialog.close(
                            rx.button("Submit", type="submit")
                        ),
                        spacing="3",
                        justify="end"
                    ),
                    direction="column",
                    spacing="4"
                ),
                on_submit= State.add_user,
                reset_on_submit=False,
            ),
            max_width="450px"
        ),
    )

def dashboard() ->rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Gender")
            )
        ),
        rx.table.body(
            rx.foreach(State.users, render_users)
        ),
        variant="surface",
        size="3"
    )

def graph():
    return rx.recharts.bar_chart(
        rx.recharts.bar(
            data_key="value",
            stroke=rx.color("accent", 9),
            fill=rx.color("accent", 8),
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        data=State.user_for_graph,
        width="100%",
        height=250,
    )

def index() -> rx.Component:
    return rx.vstack(
        dialog(),
        dashboard(),
        graph(),
        align="center"
    )


app = rx.App(theme=rx.theme(radius="large", accent_color="grass"))
app.add_page(
    index,
    title="Dashboard app",
    description="too lazy to write a description",
    on_load=State.transform_data
)
