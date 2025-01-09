# main.py
import sys
from PyQt5.QtWidgets import QApplication
from model.task_model import TaskModel
from view.task_view import TaskView
from controller.task_controller import TaskController

if __name__ == "__main__":
    # Initialiser l'application PyQt
    app = QApplication(sys.argv)

    # Initialiser le modèle, la vue et le contrôleur
    model = TaskModel()
    view = TaskView()
    controller = TaskController(model, view)

    # Afficher l'interface utilisateur
    view.show()

    # Lancer l'application
    sys.exit(app.exec_())

