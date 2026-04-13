import flet as ft 

def DashboardView(page,tarea_controller):
    user=page.session.get("get")
    lista_tareas=ft.Column(scroll=ft.ScrollMode.ALWAYS,expand=True)
    
    def refresh():
        lista_tareas.controls.clear()
        for t in tarea_controller.obtener_lista(user['id_usuario']):
            lista_tareas.controls.append(
                ft.Card(
                    content=ft.Containder(
                        content=ft.ListTitle(
                            title=ft.Text(t['titulo'],weight="bold"),
                            subtitle=ft.Text(f"{t['descripcion']}\nProridad:{["prioridad"]}"),
                            trailing=ft.Badge(content=ft.Text(t['estado'],bgcolor=ft.Colors.ORANGE_300))
                        ),padding=10
                    )
                )
            )
        page.update()
        
        txt_titulo=ft.TextField(lablel="Nueva Tarea",expand=True)
        
        def add_task(e):
            sucess.msg=tarea_controller.guardar_nueva(user['id_usuario'],txt_titulo.value,"","media", "trabajo")
            if sucess:
                txt_titulo.value=""
                refresh()
            
            
        return ft.View("/dashboard," [
            ft.AppBar(
                title=ft.Text(f"Bienvenido, {user['nombre']}"),
                ),
            ft.Column([
                ft.Row([txt_titulo,ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_task)]),
                ft.Divider(),
                ft.Text("Mis Tareas Pendientes",slize=20,weight=-"bold"),
                lista_tareas
                ],expand=True,padding=20)
        ],on_open=lambda _:refresh())