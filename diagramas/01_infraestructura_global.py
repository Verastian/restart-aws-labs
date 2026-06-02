from diagrams import Diagram, Cluster, Edge
from diagrams.aws.general import General
from diagrams.aws.management import SystemsManager
from diagrams.aws.compute import EC2
from diagrams.aws.storage import S3
from diagrams.aws.network import CloudFront, Route53

output = "../LABS/servicios/imgs/01_infraestructura_global"

with Diagram(
    "Infraestructura Global AWS",
    filename=output,
    show=False,
    direction="TB",
    graph_attr={"fontsize": "18", "bgcolor": "white", "pad": "0.8"},
):
    dns = Route53("Route 53\n(DNS Global)")

    with Cluster("Región us-east-1\n(Norte de Virginia)"):
        with Cluster("Zona de Disponibilidad A"):
            ec2a = EC2("Servidor Web")
        with Cluster("Zona de Disponibilidad B"):
            ec2b = EC2("Servidor Web\n(Réplica)")
        s3 = S3("S3 Bucket")

    with Cluster("Región eu-west-1\n(Irlanda)"):
        with Cluster("Zona de Disponibilidad A"):
            ec2eu = EC2("Servidor Web")
        s3eu = S3("S3 Bucket")

    cdn = CloudFront("CloudFront CDN\n(Red Global)")

    dns >> cdn
    cdn >> ec2a
    cdn >> ec2b
    cdn >> ec2eu
    ec2a >> s3
    ec2eu >> s3eu
