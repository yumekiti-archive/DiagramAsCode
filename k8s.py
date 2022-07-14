# diagram.py
from diagrams import Diagram
from diagrams.k8s.compute import Pod
from diagrams.k8s.infra import Node

with Diagram("Web Service", show=False):
  Node() >> Pod("web")