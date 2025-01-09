# task_controller.py
class TaskController:
    """
    Classe représentant le contrôleur dans le pattern MVC.
    Elle gère la communication entre le modèle et la vue.
    """

    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Connexion des actions de la vue aux méthodes du contrôleur
        self.view.add_button.clicked.connect(self.add_task)
        self.view.task_list_widget.itemDoubleClicked.connect(self.remove_task)

    def add_task(self):
        """Ajoute une tâche via l'entrée utilisateur."""
        task = self.view.task_input.text().strip()
        if task:
            self.model.create(task)
            self.update_task_list()
            self.view.task_input.clear()
        else:
            self.view.show_error("Veuillez entrer une tâche valide.")

    def remove_task(self, item):
        """Supprime une tâche en fonction de l'élément sélectionné."""
        index = self.view.task_list_widget.row(item)
        self.model.delete(index)
        self.update_task_list()

    def update_task_list(self):
        """Met à jour l'affichage des tâches dans la vue."""
        self.view.task_list_widget.clear()
        self.view.task_list_widget.addItems(self.model.reads())

