from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.storage import S3
from diagrams.aws.security import IAM
from diagrams.onprem.client import Users

output = "../LABS/servicios/imgs/10_ec2_iam_s3"

with Diagram(
    "EC2 accediendo a S3 mediante IAM Role",
    filename=output,
    show=False,
    direction="LR",
    graph_attr={"fontsize": "15", "bgcolor": "white", "pad": "0.8"},
):
    with Cluster("Sin IAM Role ❌"):
        ec2_bad = EC2("EC2\nCredenciales\nhardcodeadas")
        s3_bad = S3("S3 Bucket")
        ec2_bad >> Edge(label="⚠️ Inseguro", color="red") >> s3_bad

    with Cluster("Con IAM Role ✅"):
        role = IAM("IAM Role\ns3:GetObject\ns3:PutObject")
        ec2_good = EC2("EC2\nSin credenciales")
        s3_good = S3("S3 Bucket")
        role >> ec2_good
        ec2_good >> Edge(label="✅ Seguro y recomendado", color="green") >> s3_good
