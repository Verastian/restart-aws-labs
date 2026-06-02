from diagrams import Diagram, Cluster, Edge
from diagrams.aws.storage import S3
from diagrams.aws.network import CloudFront, Route53
from diagrams.aws.security import CertificateManager
from diagrams.onprem.client import Users

output = "../LABS/servicios/imgs/02_sitio_web_estatico"

with Diagram(
    "Hosting de Sitio Web Estático en AWS",
    filename=output,
    show=False,
    direction="LR",
    graph_attr={"fontsize": "16", "bgcolor": "white", "pad": "0.8"},
):
    usuarios = Users("Usuarios")

    dns = Route53("Route 53\nrestart-labs.devera.cloud")
    ssl = CertificateManager("ACM\nCertificado SSL")
    cdn = CloudFront("CloudFront\nCDN + HTTPS")

    with Cluster("Región us-east-1"):
        bucket = S3("S3 Bucket\nHTML / CSS / JS\nImágenes")

    usuarios >> dns >> cdn
    ssl >> cdn
    cdn >> bucket
