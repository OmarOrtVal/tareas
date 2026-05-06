import flet as ft
import base64

def UserView(page, auth_controller):
    page.title = "Perfil"
    user = getattr(page, "user_data", None)
    
    avatar = ft.CircleAvatar(
        radius=60,
        bgcolor=ft.Colors.BLUE_100
    )
    
    if user and user.get('foto_perfil'):
        avatar.foreground_image_src_base64 = user['foto_perfil']
    else:
        avatar.content = ft.Icon(ft.Icons.PERSON, size=60)
    
    nombre = ft.Text(f"Nombre: {user['nombre'] if user else 'Usuario'}", size=20)
    apellido = ft.Text(f"Apellido: {user['apellido'] if user else 'Usuario'}", size=20)
    email = ft.Text(f"Email: {user['email'] if user else 'Usuario'}", size=20)
    fecha_registro = ft.Text(f"Fecha de creación de la cuenta: {user['fecha_registro'] if user else 'Usuario'}", size=20)
    ultimo_acceso = ft.Text(f"Último acceso: {user['ultimo_acceso'] if user else 'Usuario'}", size=20)

    return ft.View(
        route="/perfil",
        controls=[
            ft.AppBar(
                title=ft.Text(f"Perfil de Usuario", size=30),
                actions=[
                    ft.IconButton(ft.Icons.BOOK, on_click=lambda _: page.go("/dashboard")),
                    ft.IconButton(ft.Icons.EXIT_TO_APP, on_click=lambda _: page.go("/"))
                ],
            ),
            ft.Container(
                ft.Column([
                    ft.Divider(thickness=8, color=ft.Colors.BLUE),
                    ft.Row([avatar], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Divider(thickness=6, color=ft.Colors.BLUE),
                    ft.Row([nombre], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Divider(thickness=6, color=ft.Colors.BLUE),
                    ft.Row([apellido], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Divider(thickness=6, color=ft.Colors.BLUE),
                    ft.Row([email], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Divider(thickness=6, color=ft.Colors.BLUE),
                    ft.Row([fecha_registro], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Divider(thickness=6, color=ft.Colors.BLUE),
                    ft.Row([ultimo_acceso], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Divider(thickness=8, color=ft.Colors.BLUE),
                ], expand=True),
                padding=20, expand=True, alignment=ft.MainAxisAlignment.CENTER,
            ),
        ]
    )