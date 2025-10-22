import reflex as rx
from app.state import State


def nav_item(item: dict) -> rx.Component:
    """A single navigation item for the header."""
    return rx.el.a(
        item["name"],
        on_click=[
            lambda: State.set_active_nav_item(item["name"]),
            lambda: State.scroll_to(item["href"]),
        ],
        class_name=rx.cond(
            State.active_nav_item == item["name"],
            "px-3 py-2 text-sm font-semibold text-white bg-purple-700 rounded-md transition-all duration-300",
            "px-3 py-2 text-sm font-semibold text-gray-200 hover:text-white hover:bg-purple-600/50 rounded-md transition-all duration-300",
        ),
        cursor="pointer",
    )


def mobile_nav_item(item: dict) -> rx.Component:
    """A single navigation item for the mobile menu."""
    return rx.el.a(
        item["name"],
        on_click=[
            lambda: State.set_active_nav_item(item["name"]),
            lambda: State.scroll_to(item["href"]),
            State.toggle_mobile_menu,
        ],
        class_name="block px-4 py-3 text-base font-medium text-gray-200 hover:bg-purple-700 hover:text-white rounded-md transition-colors duration-200",
        cursor="pointer",
    )


def header() -> rx.Component:
    """The main header component with navigation."""
    return rx.el.header(
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    rx.icon("zap", class_name="h-6 w-6 stroke-white"),
                    rx.el.span(
                        "TechConsult", class_name="text-xl font-bold text-white"
                    ),
                    href="#home",
                    on_click=lambda: State.set_active_nav_item("Home"),
                    class_name="flex items-center gap-2 cursor-pointer",
                ),
                rx.el.div(
                    rx.foreach(State.nav_items, nav_item),
                    class_name="hidden md:flex items-center gap-1",
                ),
                rx.el.div(
                    rx.el.button(
                        rx.icon(
                            tag=rx.cond(State.mobile_menu_open, "x", "menu"),
                            class_name="h-6 w-6 stroke-white",
                        ),
                        on_click=State.toggle_mobile_menu,
                        class_name="p-2 rounded-md hover:bg-purple-700 focus:outline-none focus:ring-2 focus:ring-white transition-all duration-200",
                    ),
                    class_name="md:hidden flex items-center",
                ),
            ),
            rx.cond(
                State.mobile_menu_open,
                rx.el.div(
                    rx.foreach(State.nav_items, mobile_nav_item),
                    class_name="md:hidden mt-4 space-y-1 px-2 pb-3 pt-2 bg-purple-800/50 rounded-b-lg border-t border-purple-700/50",
                ),
                None,
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
        ),
        class_name="sticky top-0 z-50 w-full bg-purple-600/95 backdrop-blur-sm shadow-md py-3 font-['Roboto']",
    )