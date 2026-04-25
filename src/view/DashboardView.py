import flet as ft


def DashboardView(page):

    user = getattr(page, "user_data", None)

    def mostrar_perfil(e):
        if not user:
            return

        dialogo = ft.AlertDialog(
            title=ft.Text("Perfil de Usuario"),
            content=ft.Column(
                [
                    ft.Text(f"ID: {user.get('id_usuario', '')}"),
                    ft.Text(f"Nombre: {user.get('nombre', '')}"),
                    ft.Text(f"Email: {user.get('email', '')}"),
                ],
                tight=True
            ),
        )

        page.overlay.append(dialogo)
        dialogo.open = True
        page.update()

    return ft.View(
        route="/dashboard",
        controls=[
            ft.AppBar(
                title=ft.Text(f"Bienvenido, {user.get('nombre', 'Usuario') if user else 'Usuario'}"),
                actions=[
                    ft.IconButton(ft.Icons.PERSON, on_click=mostrar_perfil),
                    ft.IconButton(ft.Icons.EXIT_TO_APP, on_click=lambda _: page.go("/"))
                ],
            ),
            ft.Container(
                content=ft.Column([], expand=True),  
                padding=20,
                expand=True
            ),
        ]
    )