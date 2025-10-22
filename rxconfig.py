"""Reflex configuration file."""
import reflex as rx

config = rx.Config(
    app_name="app",
    frontend_port=3001,
    backend_port=8001,
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
    # Disable the "Built with Reflex" badge site-wide
    show_built_with_reflex=False,
)
