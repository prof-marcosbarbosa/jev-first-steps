from typesafe_sdk import Noul, TypeSafeClient


def main() -> None:
    client = TypeSafeClient()

    response = client.system_one(
        state=(
            "Não consigo acessar o SUAP desde esta manhã. Tenho que lançar as "
            "notas dos alunos até hoje e o sistema informa que minha senha está incorreta."
        ),
        questions={
            "e_urgente": Noul(
                instructions="Este chamado precisa de atendimento urgente?",
            ),
        },
    )

    print(response.answers["e_urgente"].noul)


if __name__ == "__main__":
    main()