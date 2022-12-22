from infrastructure.repo_points import RepoPoints
from business.service_points import ServicePoints
from ui_layer.ui import UI

def main():

    repo_points = RepoPoints()
    service_point = ServicePoints(repo_points)
    consola = UI(service_point)
    consola.run()

main()