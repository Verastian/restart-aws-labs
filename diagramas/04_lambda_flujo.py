from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import Lambda
from diagrams.aws.storage import S3
from diagrams.aws.network import APIGateway
from diagrams.aws.database import Dynamodb
from diagrams.aws.integration import SNS
from diagrams.onprem.client import Users

output = "../LABS/servicios/imgs/04_lambda_flujo"

with Diagram(
    "AWS Lambda — Flujo de Invocación",
    filename=output,
    show=False,
    direction="LR",
    graph_attr={"fontsize": "16", "bgcolor": "white", "pad": "0.8"},
):
    with Cluster("Triggers (Disparadores)"):
        api = APIGateway("API Gateway\nPetición HTTP")
        s3_trigger = S3("S3 Event\nArchivo subido")
        sns = SNS("SNS\nMensaje")

    fn = Lambda("Función Lambda\nPython / Node.js\nMáx. 15 min")

    with Cluster("Destinos"):
        db = Dynamodb("DynamoDB\nBase de datos")
        s3_out = S3("S3\nResultado")

    api >> fn
    s3_trigger >> fn
    sns >> fn

    fn >> db
    fn >> s3_out
