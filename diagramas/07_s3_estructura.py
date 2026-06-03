from diagrams import Diagram, Cluster, Edge
from diagrams.aws.storage import S3
from diagrams.onprem.client import Users
from diagrams.aws.management import SystemsManager

output = "../LABS/servicios/imgs/07_s3_estructura"

with Diagram(
    "Estructura de Amazon S3",
    filename=output,
    show=False,
    direction="LR",
    graph_attr={"fontsize": "15", "bgcolor": "white", "pad": "0.8"},
):
    usuario = Users("Aplicación / Usuario")

    with Cluster("S3 Bucket\nmi-empresa-backups-prod"):
        with Cluster("Objeto 1\nKey: docs/contrato.pdf"):
            obj1 = S3("Value: contenido\nMetadata: fecha, tipo\nVersionID: abc123")
        with Cluster("Objeto 2\nKey: imgs/logo.png"):
            obj2 = S3("Value: contenido\nMetadata: fecha, tipo\nVersionID: xyz789")
        with Cluster("Objeto 3\nKey: videos/demo.mp4"):
            obj3 = S3("Value: contenido\nMetadata: fecha, tipo")

    usuario >> obj1
    usuario >> obj2
    usuario >> obj3
