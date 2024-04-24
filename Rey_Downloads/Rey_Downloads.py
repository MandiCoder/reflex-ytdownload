from .components.card import my_card
from .states.my_state import FormState
import reflex as rx


def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Descargar Videos de YouTube", color_scheme="jade"),
            rx.form(
                    rx.flex(
                    rx.input(
                        placeholder="URL...",
                        name="url",
                    ),
                    rx.button("Aceptar", type="submit"),
                    spacing="2"
                ),
                on_submit=FormState.handle_submit,
                reset_on_submit=True,
            ),
            my_card(),
            align="center",
            spacing="7",
            font_size="2em",
        ),
        height="100vh",
    )


app = rx.App(
    theme = rx.theme(appearance="dark", accentColor="plum", radius="large")
)
app.add_page(index)
