# task_view.py
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QMessageBox
)

class TaskView(QWidget):
    """
    Classe représentant la vue dans le pattern MVC.
    Elle gère l'interface utilisateur (UI) pour afficher
    et manipuler une liste de tâches.
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task Manager - MVC Example")

        # Layout principal
        self.layout = QVBoxLayout()

        # Composants de l'UI
        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText("Entrez une nouvelle tâche")
        self.add_button = QPushButton("Ajouter une tâche", self)
        self.task_list_widget = QListWidget(self)

        # Ajouter les composants au layout
        self.layout.addWidget(self.task_input)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.task_list_widget)

        self.setLayout(self.layout)

    def show_error(self, message: str):
        """Affiche une boîte de dialogue pour les erreurs."""
        QMessageBox.critical(self, "Erreur", message)

