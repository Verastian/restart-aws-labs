from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.storage import EBS
from diagrams.aws.network import VPC, InternetGateway
from diagrams.aws.security import IAM
from diagrams.onprem.client import Users

output = "../LABS/servicios/imgs/03_ec2_basico"

with Diagram(
    "Amazon EC2 — Estructura Básica",
    filename=output,
    show=False,
    direction="TB",
    graph_attr={"fontsize": "16", "bgcolor": "white", "pad": "0.8"},
):
    usuario = Users("Usuario SSH\n/ Navegador")
    igw = InternetGateway("Internet Gateway")

    with Cluster("VPC — Virtual Private Cloud"):
        with Cluster("Subred Pública\nZona de Disponibilidad A"):
            instancia = EC2("Instancia EC2\nt3.micro\nAmazon Linux 2023")
            disco = EBS("EBS Volume\n8 GB gp3")
            instancia - disco

    rol = IAM("IAM Role\nPermisos del servidor")

    usuario >> igw >> instancia
    rol >> instancia
