import flet as ft
import re
from models.schemasModel import UsuarioSchema  
import shutil
import os
from datetime import datetime

def RegisterView(page: ft.Page, auth_controller):
    
    nombre = ft.TextField(
        label="Nombre(s)",
        prefix_icon=ft.Icons.PERSON,
        width=400,
        border_radius=10
    )
    
    apellido = ft.TextField(
        label="Apellidos",
        prefix_icon=ft.Icons.PERSON,
        width=400,
        border_radius=10
    )
    
    email = ft.TextField(
        label="Correo electrónico",
        prefix_icon=ft.Icons.EMAIL,
        width=400,
        border_radius=10,
        keyboard_type=ft.KeyboardType.EMAIL
    )
    
    password = ft.TextField(
        label="Contraseña",
        prefix_icon=ft.Icons.LOCK,
        password=True,
        can_reveal_password=True,
        width=400,
        border_radius=10
    )
    
    confirm_password = ft.TextField(
        label="Confirmar contraseña",
        prefix_icon=ft.Icons.LOCK,
        password=True,
        can_reveal_password=True,
        width=400,
        border_radius=10
    )
    
    foto_perfil = ft.CircleAvatar(
        content=ft.Icon(ft.Icons.PERSON, size=40),
        radius=40,
        bgcolor=ft.Colors.BLUE_100
    )
    
    selected_image_path = None
    
    def pick_image(e):
        file_picker.pick_files(
            allowed_extensions=["jpg", "jpeg", "png", "gif", "bmp"],
            dialog_title="Seleccionar foto de perfil"
        )
    
    def on_file_selected(e: ft.FilePickerResultEvent):
        nonlocal selected_image_path
        if e.files:
            try:
                selected_image_path = e.files[0].path
                
                foto_perfil.content = ft.Image(
                    src=selected_image_path,
                    width=80,
                    height=80,
                    fit=ft.ImageFit.COVER
                )
                foto_perfil.update()
                
                print(f"Foto seleccionada: {selected_image_path}")
                
            except Exception as ex:
                print(f"Error al cargar imagen: {ex}")
                page.snack_bar = ft.SnackBar(
                    content=ft.Text(f"Error al cargar imagen: {ex}"),
                    bgcolor="red"
                )
                page.snack_bar.open = True
                page.update()
    
    file_picker = ft.FilePicker(on_result=on_file_selected)
    page.overlay.append(file_picker)
    
    btn_select_photo = ft.ElevatedButton(
        "Seleccionar foto de perfil",
        icon=ft.Icons.PHOTO_CAMERA,
        on_click=pick_image,
        width=250
    )
    
    mensaje = ft.Text("", color="red", size=12)
    
    def mostrar_snackbar(mensaje_texto, color=ft.Colors.GREEN):
        page.snack_bar = ft.SnackBar(
            content=ft.Text(mensaje_texto),
            bgcolor=color,
            duration=2000,
        )
        page.snack_bar.open = True
        page.update()
    
    def registrar_click(e):
        nonlocal selected_image_path
        if not nombre.value or not apellido.value or not email.value or not password.value or not confirm_password.value:
            mensaje.value = "Todos los campos son obligatorios"
            mensaje.color = "red"
            page.update()
            return
        
        if password.value != confirm_password.value:
            mensaje.value = "Las contraseñas no coinciden"
            mensaje.color = "red"
            page.update()
            return
        
        if len(password.value) < 6:
            mensaje.value = "La contraseña debe tener al menos 6 caracteres"
            mensaje.color = "red"
            page.update()
            return
        
        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email.value):
            mensaje.value = "Correo electrónico inválido"
            mensaje.color = "red"
            page.update()
            return
        
        fotos_dir = "fotos_perfil"
        if not os.path.exists(fotos_dir):
            os.makedirs(fotos_dir)
            print(f"Directorio creado: {fotos_dir}")
        
        foto_destino = None
        if selected_image_path and os.path.exists(selected_image_path):
            try:
                extension = os.path.splitext(selected_image_path)[1]
                nombre_foto = f"usuario_{datetime.now().strftime('%Y%m%d_%H%M%S')}{extension}"
                foto_destino = os.path.join(fotos_dir, nombre_foto)
                
                shutil.copy2(selected_image_path, foto_destino)
                print(f"Foto copiada a: {foto_destino}")
                
            except Exception as ex:
                print(f"Error al copiar foto: {ex}")
                mostrar_snackbar("Error al guardar la foto", ft.Colors.RED)
        
        usuario_data = UsuarioSchema(
            nombre=nombre.value,
            apellido=apellido.value,
            email=email.value,
            password=password.value,
            foto_perfil=foto_destino  
        )
        
        exito, msg = auth_controller.registrar(usuario_data)
        
        if exito:
            mostrar_snackbar("¡Registro exitoso! Ahora inicia sesión", ft.Colors.GREEN)
            nombre.value = ""
            apellido.value = ""
            email.value = ""
            password.value = ""
            confirm_password.value = ""
            selected_image_path = None
            mensaje.value = ""
            foto_perfil.content = ft.Icon(ft.Icons.PERSON, size=40)
            page.update()
            page.go("/")
        else:
            mensaje.value = msg or "Error al registrar usuario"
            mensaje.color = "red"
            page.update()
    
    def ir_login(e):
        page.go("/")
    
    btn_registrar = ft.ElevatedButton(
        "Registrarse",
        width=250,
        on_click=registrar_click,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.GREEN_500,
            color=ft.Colors.WHITE,
            padding=20,
            shape=ft.RoundedRectangleBorder(radius=12),
        ),
    )
    
    btn_login = ft.TextButton(
        "¿Ya tienes cuenta? Inicia sesión",
        on_click=ir_login
    )
    
    return ft.View(
        route="/register",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        appbar=ft.AppBar(
            title=ft.Text("SIGE - Registro"),
            bgcolor=ft.Colors.BLACK,
            color=ft.Colors.WHITE,
            leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda _: page.go("/"))
        ),
        controls=[
            ft.Column(
                [
                    ft.Text("Crear Nueva Cuenta", size=20, weight="bold"),
                    ft.Container(height=10),
                    foto_perfil,
                    btn_select_photo,
                    ft.Container(height=5),
                    nombre,
                    apellido,
                    email,
                    password,
                    confirm_password,
                    mensaje,
                    ft.Container(height=5),
                    btn_registrar,
                    ft.Container(height=5),
                    btn_login
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                tight=True,
                spacing=10
            )
        ]
    )