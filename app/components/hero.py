import reflex as rx
from app.state import State


def hero_section() -> rx.Component:
    """The hero section for the landing page."""
    return rx.el.section(
        rx.el.div(
            rx.el.h1(
                "Transform Your Business with Expert Technology Solutions",
                class_name="text-4xl md:text-5xl lg:text-6xl font-extrabold text-white text-center leading-tight tracking-tight",
            ),
            rx.el.p(
                "We provide comprehensive IT consulting, custom programming, and project governance to drive your success. Our tailored solutions and proven expertise ensure your technology works for you.",
                class_name="mt-6 max-w-3xl mx-auto text-lg md:text-xl text-purple-200 text-center font-medium",
            ),
            rx.el.button(
                "Request a Consultation",
                rx.icon("arrow_right", class_name="ml-2 h-5 w-5"),
                on_click=lambda: State.scroll_to("#contact"),
                class_name="mt-10 px-8 py-4 bg-white text-purple-600 font-semibold text-lg rounded-lg shadow-lg hover:shadow-xl hover:bg-gray-100 transform hover:-translate-y-1 transition-all duration-300 ease-in-out flex items-center justify-center group",
            ),
            class_name="flex flex-col items-center justify-center min-h-[70vh] px-4",
        ),
        id="home",
        class_name="w-full bg-gradient-to-br from-purple-600 to-purple-800 font-['Roboto']",
    )