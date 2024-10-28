import requests
import json
import urllib3
from kubernetes import config

# Desabilitar warnings de SSL (não recomendado em produção)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Carregar as configurações do arquivo kubeconfig
config_data = config.load_kube_config()

# Pega o contexto atual (o contexto ativo)
current_context = config.list_kube_config_contexts()[1]

# Extrai o token e o servidor API do contexto atual
bearer_token = current_context['context']['user']['token']
k8s_api_server = current_context['context']['cluster']['server']

# Cabeçalhos para a requisição HTTP com autenticação Bearer
headers = {
    "Authorization": f"Bearer {bearer_token}",
    "Content-Type": "application/json"
}

# Função para fazer uma requisição GET para listar os Pods no namespace 'default'
def listar_pods():
    url = f"{k8s_api_server}/api/v1/namespaces/default/pods"
    
    # Fazer a requisição GET para a API Kubernetes
    response = requests.get(url, headers=headers, verify=False)

    # Verificar o status da requisição
    if response.status_code == 200:
        print("Pods no namespace 'default':")
        print(json.dumps(response.json(), indent=4))
    else:
        print(f"Erro ao listar os Pods: {response.status_code}")
        print(response.json())

# Função para criar um novo Pod via requisição POST
def criar_pod():
    url = f"{k8s_api_server}/api/v1/namespaces/default/pods"
    
    # Manifesto do Pod em formato JSON
    pod_manifest = {
        "apiVersion": "v1",
        "kind": "Pod",
        "metadata": {
            "name": "my-nginx-pod"
        },
        "spec": {
            "containers": [
                {
                    "name": "nginx",
                    "image": "nginx:latest",
                    "ports": [
                        {
                            "containerPort": 80
                        }
                    ]
                }
            ]
        }
    }
    
    # Fazer a requisição POST para criar o Pod
    response = requests.post(url, headers=headers, data=json.dumps(pod_manifest), verify=False)

    # Verificar o status da requisição
    if response.status_code == 201:
        print("Pod criado com sucesso!")
        print(json.dumps(response.json(), indent=4))
    else:
        print(f"Erro ao criar o Pod: {response.status_code}")
        print(response.json())

if __name__ == "__main__":
    # Listar os Pods no namespace 'default'
    listar_pods()

    # Criar um novo Pod
    
