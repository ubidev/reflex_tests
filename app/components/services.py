"""Components for the services section of the landing page."""
import reflex as rx
from app.state import State


def service_card(service: dict) -> rx.Component:
    """A card for a single service."""
    # un lien complet autour de la carte, comme défini actuellement
    # fonctionne mais empêche la sélection de texte à l'intérieur de la carte
    return rx.el.a(
        rx.el.div(
            rx.icon(service["icon"], class_name="h-10 w-10 stroke-purple-600"),
            class_name="mb-4 flex justify-center items-center h-16 w-16 rounded-full bg-purple-100",
        ),
        rx.el.h3(
            service["title"],
            class_name="text-2xl font-bold text-gray-800 mb-2 font-['Roboto']",
        ),
        rx.el.p(
            service["description"],
            class_name="text-base font-medium text-gray-600 font-['Roboto']",
        ),
        href=service["url"],
        class_name="bg-white p-8 rounded-lg shadow-sm hover:shadow-lg hover:bg-purple-50 " \
                   "transition-all duration-300 ease-in-out border " \
                   "border-gray-100 flex flex-col items-start text-left",
    )


def services_section() -> rx.Component:
    """The services section of the landing page."""
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Our Services",
                class_name="text-3xl md:text-4xl font-bold " \
                "text-gray-900 text-center mb-4 font-['Roboto']",
            ),
            rx.el.p(
                "We offer a comprehensive suite of technology services to meet your needs.",
                class_name="text-lg text-gray-600 text-center " \
                "max-w-2xl mx-auto mb-12 font-medium font-['Roboto']",
            ),
            rx.el.div(
                rx.foreach(State.services, service_card),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20",
        ),
        id="services",
        class_name="bg-gray-50",
    )


def value_prop_section() -> rx.Component:
    """A section to highlight the company's value proposition."""
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Why Choose Us?",
                    class_name="text-3xl font-bold text-white mb-4 tracking-tight",
                ),
                rx.el.p(
                    """We are not just another tech company. We are your partners in 
innovation and success. Our commitment to excellence sets us apart.""",
                    class_name="text-lg text-purple-200 max-w-3xl",
                ),
                class_name="mb-10 text-center",
            ),
            rx.el.div(
                rx.foreach(
                    [
                        "Proven Track Record of Success",
                        "Deep Industry Expertise",
                        "Tailored, Client-Centric Solutions",
                        "Commitment to Long-Term Partnership",
                    ],
                    lambda item: rx.el.div(
                        rx.icon(
                            "check_check", class_name="h-6 w-6 stroke-green-400 mr-3"
                        ),
                        rx.el.span(item, class_name="text-lg font-semibold text-white"),
                        class_name="flex items-center bg-white/10 p-4 rounded-lg",
                    ),
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-4xl mx-auto",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20 flex flex-col items-center",
        ),
        class_name="bg-gradient-to-br from-purple-700 to-purple-800 font-['Roboto']",
    )
