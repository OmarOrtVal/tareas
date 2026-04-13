import flet as ft 
from src.controllers.UsuariosController import AuthController
from src.controllers.TareaController import TareaController
from src.views.LoginView import LoginView
from src.views dashboard import DashboardView

def main(page: ft.Page):
    auth_ctrl=AuthController()
    task_ctrl=TareaController()
    
    def route_change(route):
        page.view.clear()
        if
