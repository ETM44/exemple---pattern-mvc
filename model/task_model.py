# task_model.py
class TaskModel:
    """
    Classe représentant le modèle dans le pattern MVC.
    Elle gère une liste de tâches et fournit des méthodes
    pour ajouter, supprimer et récupérer des tâches.
    """

    def __init__(self):
        self.task_list = []

    def create(self, task: str):
        """Ajoute une tâche à la liste."""
        self.task_list.append(task)

    def delete(self, index: int):
        """Supprime une tâche de la liste en fonction de son index."""
        if 0 <= index < len(self.task_list):
            self.task_list.pop(index)

    def reads(self):
        """Retourne la liste des tâches."""
        return self.task_list

