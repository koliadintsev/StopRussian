"""
Главный обработчик ElasticSearch
"""
from elasticsearch import Elasticsearch
import elasticsearch_dsl
import concurrent.futures
import uuid
from elasticsearch_dsl import connections, Index, Search, analyzer, Q
import re
import jsons
from DataImport import import_sanctions_eu, import_sanctions_uk, import_sanctions_usa

from settings import STATIC_ROOT

SERVER_URL = "https://localhost:9200"  # Тест
#SERVER_URL = "https://search-lexcovery-dev-glueefgtrwhrhwln3es3dscawm.eu-central-1.es.amazonaws.com/" # Основа
#SERVER_URL = "http://elasticsearch:9200"  # Docker
INDEX_NAME = "sanction"
#SERVER_URL = "https://stoprussian.es.us-central1.gcp.cloud.es.io:9243"

# Password for the 'elastic' user generated by Elasticsearch
ELASTIC_PASSWORD = "tjkwrXgtwvK8kmtxUqE2"
HTTP_CA_fingerprint = '835009b97f1643505f429aeb80acbdb4f7a01de1c3d360219f4f9b7933384a20'
HTTP_CA_FILENAME = STATIC_ROOT + "/ca_certs/http_ca.crt"
api_key = "sanctions"
api_key_pass = "Z0hHTTBIOEJURDllSmF2OHlwZ3k6cjRlTnBBbGVSTGEzLV9kczU5N1J5Zw=="
# Found in the 'Manage Deployment' page
#CLOUD_ID = "StopRussian:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvJDVjNTNjY2U0Yjk4YTQzNzI4ZDAyYWIyMzA4OGJkMDQ5JGJkZDcxZDcwZWIxNzQwZDc5ZDc2OTQ1NjQzMTM2MDA3"


def ping(client):
    # Successful response!
    # {'name': 'instance-0000000000', 'cluster_name': ...}
    return client.ping()


def initialize_client():
    # Create the client instance
    client = Elasticsearch(
        SERVER_URL,
        ca_certs=HTTP_CA_FILENAME,
        http_auth=("elastic", ELASTIC_PASSWORD)
    )
    return client


def create_index():

    sanctions_USA = import_sanctions_usa.import_data_from_xml()
    sanctions_EU = import_sanctions_eu.import_data_from_xml()
    sanctions_UK = import_sanctions_uk.import_data_from_xml()

    client = initialize_client()
    # Создаем индекс
    client.indices.create(index="sanctions_usa")
    client.indices.create(index="sanctions_uk")
    client.indices.create(index="sanctions_eu")

    # Вносим имена в индекс
    for sanction in sanctions_USA:
        dict = jsons.dump(sanction)
        client.index(index="sanctions_usa", document=dict)

    for sanction in sanctions_UK:
        dict = jsons.dump(sanction)
        client.index(index="sanctions_uk", document=dict)

    for sanction in sanctions_EU:
        dict = jsons.dump(sanction)
        client.index(index="sanctions_eu", document=dict)

def delete_index():
    client = initialize_client()
    client.indices.delete(index="sanctions_usa")
    client.indices.delete(index="sanctions_uk")
    client.indices.delete(index="sanctions_eu")