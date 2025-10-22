import reflex as rx
from app.state import TestimonialState


def testimonial_card(testimonial: dict, index: int) -> rx.Component:
    """A card for a single testimonial."""
    return rx.el.div(
        rx.el.blockquote(
            rx.el.p(
                f'''"{testimonial["quote"]}"''',
                class_name="text-lg font-medium text-gray-800 leading-relaxed",
            ),
            class_name="relative p-6 bg-white rounded-lg shadow-md border-l-4 border-purple-500",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.img(
                    src=f"https://api.dicebear.com/9.x/initials/svg?seed={testimonial['avatar_seed']}",
                    class_name="h-12 w-12 rounded-full bg-gray-200",
                ),
                rx.el.div(
                    rx.el.p(testimonial["name"], class_name="font-bold text-gray-900"),
                    rx.el.p(
                        f"{testimonial['title']}, {testimonial['company']}",
                        class_name="text-sm text-gray-500",
                    ),
                ),
                class_name="flex items-center gap-4",
            ),
            class_name="mt-4 flex items-center justify-between",
        ),
        class_name=rx.cond(
            TestimonialState.current_testimonial_index == index,
            "flex-col w-full max-w-2xl mx-auto transition-opacity duration-500 ease-in-out opacity-100",
            "absolute top-0 left-0 w-full max-w-2xl mx-auto transition-opacity duration-500 ease-in-out opacity-0 pointer-events-none",
        ),
    )


def testimonials_section() -> rx.Component:
    """The testimonials section of the landing page."""
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "What Our Clients Say",
                class_name="text-3xl md:text-4xl font-bold text-gray-900 text-center mb-4",
            ),
            rx.el.p(
                "We are proud to have partnered with innovative companies and leaders.",
                class_name="text-lg text-gray-600 text-center max-w-2xl mx-auto mb-12 font-medium",
            ),
            rx.el.div(
                rx.foreach(
                    TestimonialState.testimonials,
                    lambda item, i: testimonial_card(item, i),
                ),
                class_name="relative w-full h-64 md:h-56 flex items-center justify-center",
            ),
            rx.el.div(
                rx.foreach(
                    TestimonialState.testimonials,
                    lambda _, i: rx.el.button(
                        on_click=lambda: TestimonialState.set_testimonial(i),
                        class_name=rx.cond(
                            TestimonialState.current_testimonial_index == i,
                            "w-3 h-3 bg-purple-600 rounded-full transition-all duration-300",
                            "w-3 h-3 bg-gray-300 rounded-full hover:bg-purple-400 transition-all duration-300",
                        ),
                    ),
                ),
                class_name="flex justify-center gap-3 mt-8",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20",
        ),
        id="testimonials",
        class_name="bg-gray-50 font-['Roboto']",
        on_mount=TestimonialState.start_testimonial_rotation,
    )