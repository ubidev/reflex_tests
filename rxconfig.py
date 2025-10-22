"""Reflex configuration file."""
import reflex as rx

config = rx.Config(
    app_name="app",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
    # Disable the "Built with Reflex" badge site-wide
    show_built_with_reflex=False,
)
