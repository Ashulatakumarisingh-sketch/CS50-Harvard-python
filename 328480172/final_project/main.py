import flet as ft
from project import get_astronomy_title, get_mars_rover_status, get_live_iss_coords

def main(page: ft.Page):
    page.title = "AstroSpace Mobile App"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#0b0c10"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO

    header = ft.Text(
        "🌌 ASTROSPACE APP",
        size=28,
        weight=ft.FontWeight.BOLD,
        color="#66fcf1"
    )

    apod_card = ft.Container(
        content=ft.Column([
            ft.Text("Astronomy Picture of the Day", size=18, weight=ft.FontWeight.W_600, color="#66fcf1"),
            ft.Text(get_astronomy_title(), size=14, color=ft.colors.WHITE),
            ft.Image(src="https://unsplash.com", height=180, fit=ft.ImageFit.COVER, border_radius=8),
        ]),
        padding=20, bgcolor="#1f2833", border_radius=12, width=360
    )

    mars_card = ft.Container(
        content=ft.Column([
            ft.Text("Mars Curiosity Cam", size=18, weight=ft.FontWeight.W_600, color="#66fcf1"),
            ft.Text(get_mars_rover_status(), size=14, color=ft.colors.WHITE),
            ft.Image(src="https://unsplash.com", height=180, fit=ft.ImageFit.COVER, border_radius=8),
        ]),
        padding=20, bgcolor="#1f2833", border_radius=12, width=360
    )

    iss_card = ft.Container(
        content=ft.Column([
            ft.Text("🛰️ ISS Live Telemetry", size=18, weight=ft.FontWeight.W_600, color="#66fcf1"),
            ft.Text(get_live_iss_coords(), size=16, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
        ]),
        padding=20, bgcolor="#1f2833", border_radius=12, width=360
    )

    page.add(header, ft.Divider(height=10, color="transparent"), apod_card, ft.Divider(height=10, color="transparent"), mars_card, ft.Divider(height=10, color="transparent"), iss_card)

if __name__ == "__main__":
    ft.run(main, view=ft.AppiVew.web_BROWSER)
