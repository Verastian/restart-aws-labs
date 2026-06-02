from diagrams import Diagram, Cluster, Edge
from diagrams.aws.ml import Bedrock, Sagemaker
from diagrams.aws.storage import S3
from diagrams.aws.analytics import AmazonOpensearchService as Opensearch
from diagrams.onprem.client import Users

output = "../LABS/servicios/imgs/05_bedrock_rag"

with Diagram(
    "Amazon Bedrock — RAG con Knowledge Base",
    filename=output,
    show=False,
    direction="LR",
    graph_attr={"fontsize": "16", "bgcolor": "white", "pad": "0.8"},
):
    usuario = Users("Usuario")

    with Cluster("Amazon Bedrock"):
        agente = Bedrock("Agente\nBedrock")
        modelo = Bedrock("Foundation Model\nClaude 3 Sonnet")

    with Cluster("Knowledge Base"):
        docs = S3("S3\nDocumentos PDF\nMarkdown")
        index = Opensearch("Vector Store\nOpenSearch")
        docs >> index

    usuario >> agente
    agente >> Edge(label="1. Búsqueda semántica") >> index
    index >> Edge(label="2. Contexto relevante") >> agente
    agente >> Edge(label="3. Prompt + Contexto") >> modelo
    modelo >> Edge(label="4. Respuesta") >> usuario
