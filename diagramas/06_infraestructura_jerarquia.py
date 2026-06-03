from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.storage import S3
from diagrams.aws.network import CloudFront, Route53, GlobalAccelerator
from diagrams.aws.general import General
from diagrams.onprem.compute import Server

output = "../LABS/servicios/imgs/06_infraestructura_jerarquia"

with Diagram(
    "Infraestructura Global de AWS",
    filename=output,
    show=False,
    direction="TB",
    graph_attr={"fontsize": "15", "bgcolor": "white", "pad": "0.8", "ranksep": "0.8"},
):
    edge = CloudFront("Edge Locations\nCloudFront · Route 53\nAWS WAF · Shield")

    with Cluster("Región us-east-1  (Norte de Virginia)"):
        with Cluster("AZ  us-east-1a"):
            dc1a = Server("Data Center A1")
            dc1b = Server("Data Center A2")
        with Cluster("AZ  us-east-1b"):
            dc2a = Server("Data Center B1")
        with Cluster("AZ  us-east-1c"):
            dc3a = Server("Data Center C1")

    with Cluster("Región eu-west-1  (Irlanda)"):
        with Cluster("AZ  eu-west-1a"):
            dc4a = Server("Data Center D1")
        with Cluster("AZ  eu-west-1b"):
            dc5a = Server("Data Center E1")

    edge >> dc1a
    edge >> dc4a
