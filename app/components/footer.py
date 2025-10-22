import reflex as rx
from app.state import State


def footer_link_group(title: str, links: list[dict]) -> rx.Component:
    """A group of links for the footer."""
    return rx.el.div(
        rx.el.h3(
            title,
            class_name="text-sm font-semibold text-gray-400 tracking-wider uppercase",
        ),
        rx.el.ul(
            rx.foreach(
                links,
                lambda link: rx.el.li(
                    rx.el.a(
                        link["name"],
                        href=link["href"],
                        on_click=lambda: State.scroll_to(link["href"]),
                        class_name="text-base text-gray-300 hover:text-white transition-colors duration-300 cursor-pointer",
                    ),
                    class_name="mt-4",
                ),
            ),
            role="list",
            class_name="mt-4 space-y-4",
        ),
    )


def footer() -> rx.Component:
    """The main footer for the website."""
    service_links = [
        {"name": "Training", "href": "#services"},
        {"name": "Custom Programming", "href": "#services"},
        {"name": "IT Consulting", "href": "#services"},
        {"name": "Data Migration", "href": "#services"},
        {"name": "Project Governance", "href": "#services"},
    ]
    company_links = [
        {"name": "About", "href": "#about"},
        {"name": "Testimonials", "href": "#testimonials"},
        {"name": "Contact", "href": "#contact"},
    ]
    legal_links = [
        {"name": "Privacy Policy", "href": "#"},
        {"name": "Terms of Service", "href": "#"},
    ]
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                footer_link_group("Services", service_links),
                footer_link_group("Company", company_links),
                footer_link_group("Legal", legal_links),
                rx.el.div(
                    rx.el.h3(
                        "Contact Us",
                        class_name="text-sm font-semibold text-gray-400 tracking-wider uppercase",
                    ),
                    rx.el.div(
                        rx.el.p(
                            "123 Tech Avenue, Suite 500",
                            class_name="text-base text-gray-300",
                        ),
                        rx.el.p(
                            "Innovation City, TX 75001",
                            class_name="text-base text-gray-300",
                        ),
                        rx.el.p(
                            "Email: contact@techconsult.com",
                            class_name="text-base text-gray-300 mt-4",
                        ),
                        rx.el.p(
                            "Phone: (123) 456-7890",
                            class_name="text-base text-gray-300",
                        ),
                        class_name="mt-4 space-y-2",
                    ),
                ),
                class_name="grid grid-cols-2 md:grid-cols-4 gap-8",
            ),
            rx.el.div(
                rx.el.p(
                    "© 2024 TechConsult. All rights reserved.",
                    class_name="text-base text-gray-400",
                ),
                rx.el.div(class_name="flex space-x-6"),
                class_name="mt-12 border-t border-gray-700 pt-8 flex justify-between items-center",
            ),
            class_name="max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:px-8",
        ),
        class_name="bg-gray-900 font-['Roboto']",
    )