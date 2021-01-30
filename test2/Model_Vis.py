from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from new_Model import *


def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "Layer": 0}

    if agent.alive:
        portrayal["r"] = 0.5
        if agent.susceptible:
            portrayal["Color"] = "green"
        elif agent.severe:
            portrayal["Color"] = "red"
        elif agent.infected:
            portrayal["Color"] = "yellow"
    else:
        portrayal["r"] = 0.2
        portrayal["Color"] = "grey"

    return portrayal


grid = CanvasGrid(agent_portrayal, 15, 15, 300, 300)

server = ModularServer(new_COVID_model, [grid], "COVID-Model")
server.port = 8521
server.launch()
