from kubernetes import client

# Insira o token de autenticação manualmente aqui
BEARER_TOKEN = "eyJhbGciOiJSUzI1NiIsImtpZCI6IlFKY2dra0wzSkhiNnpXQkRuUUhWWjQxUnBPeGlENW80TGUtNXB6eGE5VGcifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZWZhdWx0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6ImRlZmF1bHQtdG9rZW4tbDRkNmgiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoiZGVmYXVsdCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50LnVpZCI6IjIyMzUyZDQ5LWM3NjgtNDlhYS1iMjZiLThkNDU0N2ExMWIwNCIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRlZmF1bHQifQ.NdEhha7qVilG2KfsnvDuRf4duDSmd1_rBmwfMNbosIoYYIVXwttA6lL7IZbqghl-WBqRWjcoNo0ks-RgtDmjN__K1lipqfgOeazdkKC3BXx0JkqUshRDUnDkI4OFI0ppO6TNLpFfSZavvztYVSpXBQ0kz2EuzWfMG72U2VAX7qpQO5vZT1dZEkbJEsIMRiFJvN05MknaoF9nVXYa-Dz4fszuQU24DLOrPSg-fm_ZZ3pYqp1zShozNvsq183a1gXIIhosobpeQGwo3AysfqUfAtkFGnwpgj7sdWnpFYN7h3UxPpHFKtUACi2b1_jnI_j7DkWNfpOxUHjfJ1AzEfKZQw"

# Definir o endereço da API do Kubernetes (substitua pelo seu servidor API)
K8S_API_SERVER = "https://kubernetes.docker.internal:6443"

def listar_pods():
    # Configuração manual do Kubernetes usando o token
    configuration_object = client.Configuration()
    
    # Configurando a URL do servidor da API do Kubernetes
    configuration_object.host = K8S_API_SERVER
    
    # Configurando o token de autenticação Bearer
    configuration_object.verify_ssl = False  # Desabilitando SSL para clusters locais ou de teste
    configuration_object.api_key = {"authorization": f"Bearer {BEARER_TOKEN}"}
    
    # Aplicando a configuração manual para a API Kubernetes
    client.Configuration.set_default(configuration_object)
    
    # Criando uma instância da API para manipular Pods
    v1 = client.CoreV1Api()
    
    # Tentando listar os Pods no namespace 'default'
    try:
        pods = v1.list_namespaced_service(namespace="default")
        print("Pods no namespace 'default':")
        for pod in pods.items:
            print(f"- {pod.metadata.name}")
    except client.exceptions.ApiException as e:
        print(f"Erro ao listar Pods: {e}")

def criar_servico():
    # Configuração manual do Kubernetes usando o token
    configuration_object = client.Configuration()
    
    # Configurando a URL do servidor da API do Kubernetes
    configuration_object.host = K8S_API_SERVER
    
    # Configurando o token de autenticação Bearer
    configuration_object.verify_ssl = False  # Desabilitando SSL para clusters locais ou de teste
    configuration_object.api_key = {"authorization": f"Bearer {BEARER_TOKEN}"}
    
    # Aplicando a configuração manual para a API Kubernetes
    client.Configuration.set_default(configuration_object)
    
    # Criando uma instância da API para manipular Services
    v1 = client.CoreV1Api()

    # Definir o manifesto do Service
    service_manifest = client.V1Service(
        api_version="v1",
        kind="Service",
        metadata=client.V1ObjectMeta(name="my-service"),
        spec=client.V1ServiceSpec(
            selector={"app": "my-app"},
            ports=[client.V1ServicePort(port=80, target_port=80)],
            type="ClusterIP"  # Pode ser "ClusterIP", "NodePort", "LoadBalancer", dependendo do que você precisa
        )
    )

    service_manifest2 = client.V1Service(
        api_version="v1",
        kind="Service",
        metadata=client.V1ObjectMeta(name="my-service3"),
        spec=client.V1ServiceSpec(
            selector={"app": "my-app"},
            ports=[client.V1ServicePort(port=80, target_port=80)],
            type="ClusterIP"  # Pode ser "ClusterIP", "NodePort", "LoadBalancer", dependendo do que você precisa
        )
    )

    # Criar o Service no namespace 'default'
    try:
        response = v1.create_namespaced_service(namespace="default", body=service_manifest)
        print(f"Service '{response.metadata.name}' criado com sucesso!")

        response = v1.create_namespaced_service(namespace='default', body=service_manifest2)
    except client.exceptions.ApiException as e:
        print(f"Erro ao criar o Service: {e}")

if __name__ == "__main__":
    criar_servico()



