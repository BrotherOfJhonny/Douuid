import os
import uuid
import hashlib

def generate_uuid_v1_from_cpf_or_cnpj(cpf_or_cnpj):
    # Remova qualquer caractere não numérico do CPF ou CNPJ
    cpf_or_cnpj = ''.join(filter(str.isdigit, cpf_or_cnpj))

    # Verifique se a string não está vazia
    if not cpf_or_cnpj:
        return None

    # Use a função uuid.uuid1() para gerar o UUID Version 1
    generated_uuid = uuid.uuid1(node=int(cpf_or_cnpj), clock_seq=int(cpf_or_cnpj[:2]))

    return generated_uuid

def main():
    input_file = input("Digite o nome do arquivo contendo a lista de CPFs ou CNPJs: ")

    # Obtenha o caminho completo do arquivo, combinando com o diretório do script
    input_file_path = os.path.join(os.path.dirname(__file__), input_file)

    if not os.path.exists(input_file_path):
        print("Arquivo não encontrado. Verifique o nome do arquivo e tente novamente.")
        return

    output_file = "uuid_list.txt"

    with open(input_file_path, "r") as file:
        cpf_cnpj_list = file.read().splitlines()

    uuid_list = [generate_uuid_v1_from_cpf_or_cnpj(cpf_cnpj) for cpf_cnpj in cpf_cnpj_list]

    # Remova os UUIDs inválidos (caso algum CPF ou CNPJ não tenha dígitos após a remoção dos caracteres não numéricos)
    uuid_list = [str(uuid) for uuid in uuid_list if uuid is not None]

    with open(output_file, "w") as file:
        for uuid in uuid_list:
            file.write(str(uuid) + "\n")

    print(f"Lista de UUIDs gerada com sucesso. Os UUIDs foram salvos em '{output_file}'.")

if __name__ == "__main__":
    main()
