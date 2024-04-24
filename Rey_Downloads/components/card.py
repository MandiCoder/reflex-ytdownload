import reflex as rx
from Rey_Downloads.states.my_state import FormState

def my_card() -> rx.Component:
    return rx.card(
        rx.flex(
            rx.inset(
                rx.image(src=FormState.thumb, width="100%", height="auto"),
                side="top",  
                pb="current",
            ),
            rx.chakra.progress(
                is_indeterminate=True, 
                width="100%", 
                has_stripe=True, 
                is_animated=True, 
                border_radius="5px",
                visibility=FormState.ver_bar),
            
            rx.vstack(
                rx.text(FormState.title, href=FormState.url, size="3", color_scheme="sky"),
                rx.button(
                    rx.icon(tag="download"), 
                    "Download", 
                    color_scheme="sky",
                    variant="soft",
                    disabled=FormState.btn_disabled,
                    on_click=FormState.download_video
                ),
            ),
            direction="column",
        ),
        width="30vw",
        visibility=FormState.ver_card,
    ),