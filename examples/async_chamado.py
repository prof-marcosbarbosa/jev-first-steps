import asyncio

from typesafe_sdk import AsyncTypeSafeClient, Noul, Score


async def main() -> None:
    async with AsyncTypeSafeClient() as client:
        resultado = await client.system_one(
            state="O sistema está fora do ar e preciso fechar a folha de pagamento hoje.",
            questions={
                "e_urgente": Noul(
                    instructions="O chamado precisa de atendimento urgente?",
                ),
                "impacto": Score(
                    instructions="Qual é o impacto operacional do problema?",
                    criteria=[
                        "Baixo, há uma alternativa simples",
                        "Médio, parte do trabalho está bloqueada",
                        "Alto, uma operação importante está parada",
                    ],
                ),
            },
        )

    print("Urgência:", resultado.nouls["e_urgente"].noul)
    print("Impacto:", resultado.scores["impacto"].score)


if __name__ == "__main__":
    asyncio.run(main())
