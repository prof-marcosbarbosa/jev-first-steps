from typesafe_sdk import Choice, Noul, Score, TypeSafeClient


chamado = (
    "Estou tentando integrar minha conta Stripe há 3 dias e a integração "
    "continua falhando. Estou perdendo vendas. Preciso de ajuda o quanto antes."
)

with TypeSafeClient() as client:
    resultado = client.system_one(
        state=chamado,
        questions={
            "departamento": Choice(
                instructions="Qual equipe deve atender este chamado?",
                criteria={
                    "financeiro": "Pagamentos, cobranças ou assinaturas",
                    "tecnico": "Bugs, falhas ou problemas de integração",
                    "vendas": "Preços, upgrades ou novas contas",
                },
            ),
            "frustracao": Score(
                instructions="Quão frustrado o cliente parece estar?",
                criteria=[
                    "Calmo, apenas descrevendo os fatos",
                    "Frustrado, mas cordial",
                    "Muito irritado, usando linguagem forte",
                ],
            ),
            "e_urgente": Noul(
                instructions="A mensagem demonstra urgência ou sensibilidade ao tempo?",
            ),
        },
    )

print("Departamento:", resultado.choices["departamento"].choice)
print("Frustração:", resultado.scores["frustracao"].score)
print("Urgência:", resultado.nouls["e_urgente"].noul)
print("Resultado completo:", resultado)
