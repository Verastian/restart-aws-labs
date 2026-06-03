from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB

output = "../LABS/servicios/imgs/09_ec2_escalado"

with Diagram(
    "Escalado EC2 — Vertical vs Horizontal",
    filename=output,
    show=False,
    direction="TB",
    graph_attr={"fontsize": "14", "bgcolor": "white", "pad": "1.0"},
):
    with Cluster("Escalado Vertical (Scale Up)\nAumentar recursos de la misma instancia"):
        v1 = EC2("t3.micro\n2 vCPU · 1 GiB")
        v2 = EC2("t3.large\n2 vCPU · 8 GiB")
        v1 >> Edge(label="detener → cambiar tipo → iniciar") >> v2

    with Cluster("Escalado Horizontal (Scale Out)\nAgregar más instancias"):
        lb = ELB("Load Balancer")
        h1 = EC2("Instancia 1")
        h2 = EC2("Instancia 2")
        h3 = EC2("Instancia 3")
        lb >> h1
        lb >> h2
        lb >> h3
