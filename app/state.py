"""State definitions for the marketing website Reflex app.

This module defines the application state classes and TypedDicts used by
the Reflex-based marketing website tests, including navigation items,
services, testimonials, and contact form handling.
"""
import asyncio
from typing import TypedDict
import reflex as rx


class NavItem(TypedDict):
    """TypedDict representing a navigation item.

    Attributes:
        name: The display name of the navigation link.
        href: The anchor or URL the navigation item points to.
    """

    name: str
    href: str


class Service(TypedDict):
    """TypedDict representing a service offered.

    Attributes:
        icon: Name of the icon to display for the service.
        title: Short title of the service.
        description: Detailed description of the service.
        url: URL for more information about the service.
    """

    icon: str
    title: str
    description: str
    url: str


class State(rx.State):
    """The main state for the marketing website."""

    nav_items: list[NavItem] = [
        {"name": "Home", "href": "#home"},
        {"name": "Services", "href": "#services"},
        {"name": "About", "href": "#about"},
        {"name": "Testimonials", "href": "#testimonials"},
        {"name": "Contact", "href": "#contact"},
    ]
    services: list[Service] = [
        {
            "icon": "graduation-cap",
            "title": "Training",
            "description": """Empower your team with cutting-edge skills. Our expert-led training 
programs cover the latest technologies to boost productivity and innovation.""",
            "url": "https://www.lipsum.org",
        },
        {
            "icon": "code",
            "title": "Custom Programming",
            "description": """Get software that fits your exact needs. 
We build scalable, robust, and custom applications 
to solve your most complex business challenges.""",
            "url": "https://www.wikipedia.org",
        },
        {
            "icon": "laptop",
            "title": "IT Consulting",
            "description": """Navigate the digital landscape with confidence. 
Our strategic IT consulting services provide a roadmap for your technological 
success and growth.""",
            "url": "https://www.archive.org",
        },
        {
            "icon": "database",
            "title": "Data/Application Migration",
            "description": """Seamlessly transition to modern platforms. We ensure a secure and 
efficient migration of your critical data and applications with minimal downtime.""",
            "url": "https://www.lipsum.org",
        },
        {
            "icon": "shield-check",
            "title": "IT Project Governance",
            "description": """Keep your projects on track and on budget. We provide expert oversight 
and turnaround strategies to ensure your IT initiatives deliver value.""",
            "url": "https://www.x.com",
        },
        {
            "icon": "wifi",
            "title": "Air Sniffing & Network Analysis",
            "description": """Uncover hidden insights in your network traffic. Our air sniffing and 
network analysis services help you optimize performance and security.""",
            "url": "https://www.github.com",
        },
    ]
    mobile_menu_open: bool = False
    active_nav_item: str = "Home"

    @rx.event
    def toggle_mobile_menu(self):
        """Toggles the mobile menu open and closed."""
        self.mobile_menu_open = not self.mobile_menu_open

    @rx.event
    def set_active_nav_item(self, item_name: str):
        """Sets the active navigation item when a link is clicked."""
        self.active_nav_item = item_name
        self.mobile_menu_open = False

    @rx.event
    def scroll_to(self, section_id: str):
        """Smoothly scrolls to the specified section."""
        return rx.call_script(
            f"document.querySelector('{section_id}').scrollIntoView({{ behavior: 'smooth' }})"
        )


class Testimonial(TypedDict):
    """TypedDict representing a customer testimonial.

    Attributes:
        quote: The testimonial text.
        name: The name of the person giving the testimonial.
        title: Their job title.
        company: The company they represent.
        avatar_seed: Seed string used to generate an avatar image.
    """

    quote: str
    name: str
    title: str
    company: str
    avatar_seed: str


class TestimonialState(rx.State):
    """State for the testimonials section."""

    testimonials: list[Testimonial] = [
        {
            "quote": """TechConsult's expertise in custom programming was a game-changer 
for our business. They delivered a robust, scalable solution that exceeded our expectations.""",
            "name": "Jane Doe",
            "title": "CTO",
            "company": "Innovate Corp",
            "avatar_seed": "JaneDoe",
        },
        {
            "quote": """The IT project governance they provided turned our failing project 
around. Their strategic oversight was invaluable and got us back on track.""",
            "name": "John Smith",
            "title": "Director of Operations",
            "company": "Solutions Inc.",
            "avatar_seed": "JohnSmith",
        },
        {
            "quote": """Their data migration service was seamless. We experienced zero 
downtime, and our systems are now more efficient than ever. Highly recommended!""",
            "name": "Emily White",
            "title": "IT Manager",
            "company": "DataDriven LLC",
            "avatar_seed": "EmilyWhite",
        },
    ]
    current_testimonial_index: int = 0
    _interval_id: rx.Var[int | None] = None

    @rx.event
    def next_testimonial(self):
        """Moves to the next testimonial."""
        self.current_testimonial_index = (self.current_testimonial_index + 1) % len(
            self.testimonials
        )

    @rx.event
    def set_testimonial(self, index: int):
        """Sets the current testimonial to a specific index."""
        self.current_testimonial_index = index

    @rx.event(background=True)  # pylint: disable=not-callable
    async def start_testimonial_rotation(self):
        """Starts the automatic rotation of testimonials."""

        while True:
            await asyncio.sleep(5)
            async with self:
                self.current_testimonial_index = (
                    self.current_testimonial_index + 1
                ) % len(self.testimonials)


class ContactState(rx.State):
    """State for the contact form."""

    form_data: dict[str, str] = {}
    form_status: str = ""
    is_loading: bool = False

    @rx.event
    async def handle_submit(self, form_data: dict):
        """Handles the form submission."""
        self.is_loading = True
        yield


        await asyncio.sleep(2)
        if not all(form_data.values()) or "@" not in form_data.get("email", ""):
            self.form_status = "error"
            self.is_loading = False
            yield rx.toast.error("Please fill out all fields correctly.")
            return
        self.form_data = form_data
        self.form_status = "success"
        self.is_loading = False
        yield rx.toast.success("Your message has been sent!")
