import flet as ft 
from controllers.UsuariosController import AuthController
from controllers.TareaController import TareaController
from views.LoginView import LoginView
from views.dashboard import DashboardView

def main(page: ft.Page):
    auth_ctrl=AuthController()
    task_ctrl=TareaController()
    
    def route_change(route):
        page.view.clear()
        if page.route == "/":
            page.views.append(LoginView(page,auth_ctrl))
        elif page.route =="/dashboard":
            page.views.append(DashboardView(page,task_ctrl))
        page.update()
        
    page.on_route_change=route_change
    page.go("/")
    
    def star(page: ft.Page):
        def route_change(e):
        page.views.append(DashboardView())
    
if __name__ =="__main__":
    ft.run(main)
