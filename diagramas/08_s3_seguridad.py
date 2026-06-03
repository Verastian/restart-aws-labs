from diagrams import Diagram, Cluster, Edge
from diagrams.aws.storage import S3
from diagrams.aws.security import IAM
from diagrams.onprem.client import Users, User

output = "../LABS/servicios/imgs/08_s3_seguridad"

with Diagram(
    "Modelo de Seguridad — Amazon S3",
    filename=output,
    show=False,
    direction="LR",
    graph_attr={"fontsize": "15", "bgcolor": "white", "pad": "0.8"},
):
    with Cluster("Acceso interno AWS"):
        user_iam = Users("Usuario IAM\n/ Rol")
        policy = IAM("IAM Policy\nPermisos de usuario")

    with Cluster("Acceso externo / cross-account"):
        ext = User("Cuenta externa\n/ Público")

    bucket = S3("S3 Bucket\n+ Bucket Policy")

    user_iam >> Edge(label="1. ¿Qué puede hacer?") >> policy
    policy >> Edge(label="2. Evalúa permisos") >> bucket
    ext >> Edge(label="Bucket Policy\ncontrola acceso") >> bucket
