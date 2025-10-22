import reflex as rx
from app.state import ContactState


def form_field(
    label: str, placeholder: str, field_name: str, field_type: str = "text"
) -> rx.Component:
    """A reusable form field component."""
    return rx.el.div(
        rx.el.label(
            label,
            html_for=field_name,
            class_name="block text-sm font-medium text-gray-700 mb-1",
        ),
        rx.el.input(
            type=field_type,
            id=field_name,
            name=field_name,
            placeholder=placeholder,
            class_name="w-full px-4 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:ring-purple-500 focus:border-purple-500 transition-all duration-200",
            required=True,
        ),
    )


def contact_form() -> rx.Component:
    """The contact form component."""
    return rx.el.div(
        rx.el.h2(
            "Request a Consultation",
            class_name="text-3xl md:text-4xl font-bold text-gray-900 text-center mb-4",
        ),
        rx.el.p(
            "Let's discuss how we can help your business grow. Fill out the form below to get in touch.",
            class_name="text-lg text-gray-600 text-center max-w-2xl mx-auto mb-12 font-medium",
        ),
        rx.el.form(
            rx.el.div(
                form_field("Full Name", "John Doe", "name"),
                form_field("Email Address", "you@example.com", "email", "email"),
                form_field("Company", "Your Company Inc.", "company"),
                rx.el.div(
                    rx.el.label(
                        "Message",
                        html_for="message",
                        class_name="block text-sm font-medium text-gray-700 mb-1",
                    ),
                    rx.el.textarea(
                        id="message",
                        name="message",
                        placeholder="How can we help you?",
                        rows=4,
                        class_name="w-full px-4 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:ring-purple-500 focus:border-purple-500 transition-all duration-200",
                        required=True,
                    ),
                    class_name="md:col-span-2",
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 gap-6",
            ),
            rx.el.div(
                rx.el.button(
                    rx.cond(
                        ContactState.is_loading,
                        rx.fragment(
                            rx.spinner(class_name="h-5 w-5 mr-3"), "Sending..."
                        ),
                        "Send Message",
                    ),
                    type="submit",
                    disabled=ContactState.is_loading,
                    class_name="w-full md:w-auto flex items-center justify-center px-8 py-3 bg-purple-600 text-white font-semibold text-lg rounded-lg shadow-md hover:bg-purple-700 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2 transform hover:-translate-y-1 transition-all duration-300 ease-in-out disabled:opacity-75 disabled:cursor-not-allowed",
                ),
                class_name="mt-8 flex justify-end",
            ),
            on_submit=ContactState.handle_submit,
            reset_on_submit=rx.cond(ContactState.form_status == "success", True, False),
            class_name="max-w-3xl mx-auto",
        ),
        id="contact",
        class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20 font-['Roboto'] bg-white",
    )