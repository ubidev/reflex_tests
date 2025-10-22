import reflex as rx
from app.components.header import header
from app.components.hero import hero_section
from app.components.services import services_section, value_prop_section
from app.components.testimonials import testimonials_section
from app.components.footer import footer
from app.components.contact import contact_form


def index() -> rx.Component:
    """The main landing page component."""
    return rx.el.main(
        header(),
        hero_section(),
        services_section(),
        value_prop_section(),
        rx.el.section(id="about", class_name="py-20 bg-white"),
        testimonials_section(),
        contact_form(),
        footer(),
        class_name="font-['Roboto'] bg-white",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700;900&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index)