from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.storage import EBS
from diagrams.aws.network import InternetGateway
from diagrams.onprem.client import Users

output = "../LABS/laboratorios/labs-11/imgs/LAB-11-arquitectura"

with Diagram(
    "Lab 11 — Servidor Web en Amazon EC2",
    filename=output,
    show=False,
    direction="LR",
    graph_attr={
        "fontsize": "16",
        "bgcolor": "white",
        "pad": "1.0",
        "splines": "ortho",
    },
):
    usuario = Users("Usuario\nNavegador")
    igw = InternetGateway("Internet\nGateway")

    with Cluster("Lab VPC"):
        with Cluster("Grupo de Seguridad\n✅ Puerto 80 HTTP habilitado"):
            with Cluster("Subred Pública — Zona de Disponibilidad"):
                servidor = EC2("Web Server\nt3.micro → t3.small\nAmazon Linux 2023\nApache httpd")
                disco = EBS("EBS Volume\n8 GiB → 10 GiB\ngp2")
                servidor - disco

    usuario >> Edge(label="HTTP :80") >> igw >> Edge(label="HTTP :80") >> servidor
