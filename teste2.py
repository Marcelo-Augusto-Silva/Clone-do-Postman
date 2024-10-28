import requests
import json
import urllib3

# Desabilitar warnings de SSL (não recomendado em produção)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Insira o token de autenticação manualmente aqui
BEARER_TOKEN = "eyJhbGciOiJSUzI1NiIsImtpZCI6IlFKY2dra0wzSkhiNnpXQkRuUUhWWjQxUnBPeGlENW80TGUtNXB6eGE5VGcifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZWZhdWx0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6ImRlZmF1bHQtdG9rZW4tbDRkNmgiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoiZGVmYXVsdCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50LnVpZCI6IjIyMzUyZDQ5LWM3NjgtNDlhYS1iMjZiLThkNDU0N2ExMWIwNCIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRlZmF1bHQifQ.NdEhha7qVilG2KfsnvDuRf4duDSmd1_rBmwfMNbosIoYYIVXwttA6lL7IZbqghl-WBqRWjcoNo0ks-RgtDmjN__K1lipqfgOeazdkKC3BXx0JkqUshRDUnDkI4OFI0ppO6TNLpFfSZavvztYVSpXBQ0kz2EuzWfMG72U2VAX7qpQO5vZT1dZEkbJEsIMRiFJvN05MknaoF9nVXYa-Dz4fszuQU24DLOrPSg-fm_ZZ3pYqp1zShozNvsq183a1gXIIhosobpeQGwo3AysfqUfAtkFGnwpgj7sdWnpFYN7h3UxPpHFKtUACi2b1_jnI_j7DkWNfpOxUHjfJ1AzEfKZQw"

# Definir o endereço da API do Kubernetes (substitua pelo seu servidor API)
K8S_API_SERVER = "https://kubernetes.docker.internal:6443"

# Cabeçalhos para a requisição HTTP com autenticação Bearer
headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}",
    "Content-Type": "application/json"
}

# Função para fazer uma requisição GET para listar os Pods no namespace 'default'
def listar_pods():
    url = f"{K8S_API_SERVER}/api/v1/namespaces/default/services"
    
    # Fazer a requisição GET para a API Kubernetes
    response = requests.get(url, headers=headers, verify=False)

    # Verificar o status da requisição
    if response.status_code == 200:
        print("Pods no namespace 'default':")
        print(json.dumps(response.json(), indent=4))
    else:
        print(f"Erro ao listar os Pods: {response.status_code}")
        print(response.json())

if __name__ == "__main__":
    listar_pods()
