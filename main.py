import flet as ft

def main(page: ft.Page):
    page.title = "A&E PrintHouse"
    page.window_width = 400
    page.window_height = 600
    page.theme_mode = ft.ThemeMode.DARK

    content_text = ft.Text("Welcome to A&E PrintHouse Home!", size=20)

    def set_content(new_text):
        content_text.value = new_text
        page.update()
    def nav_changed(e):
        selected_index = e.control.selected_index
        if selected_index == 0:
            content_text.value = "Welcome to A&E PrintHouse Home!"
        elif selected_index == 1:
            content_text.value = "Let's Chat!"
        elif selected_index == 2:
            content_text.value = "Settings Page"
        page.update()

    # Title with Image
    title_row = ft.Row(
    controls=[
        ft.Image(src="logo.jpg", width=40, height=40),
        ft.Text("A&E PrintHouse", size=25, weight="bold"),
    ],
    alignment=ft.MainAxisAlignment.CENTER,
    spacing=10
)

    # Use NavigationBar (not BottomNavigationBar)
    nav_bar = ft.Row(
    controls=[
        ft.ElevatedButton("🏠 Home", expand=True, on_click=lambda e: set_content("Welcome to A&E PrintHouse Home!")),
        ft.ElevatedButton("💬 Chat", expand=True, on_click=lambda e: set_content("Let's Chat!")),
        ft.ElevatedButton("⚙️ Settings", expand=True, on_click=lambda e: set_content("Settings Page")),
    ],
    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    spacing=10
)

    page.add(
    title_row,
    ft.Divider(),
    ft.Container(content_text, alignment=ft.alignment.center, expand=True),
    ft.Divider(),
    nav_bar
)

ft.app(target=main, assets_dir="static", view=ft.WEB_BROWSER)