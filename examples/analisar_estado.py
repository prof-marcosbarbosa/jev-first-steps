from typesafe_sdk import Choice, Noul, TypeSafeClient


estado = {
    "cliente": {"nome": "Ana", "plano": "Pro"},
    "mensagens": [
        {"autor": "cliente", "texto": "Minha exportação está parada há duas horas. Preciso que seja resolvido urgentemente para entrega até às 17 horas."},
        {"autor": "suporte", "texto": "Estamos verificando o processamento."},
    ],
    "tarefa": "Exportar o relatório financeiro do mês",
}

with TypeSafeClient() as client:
    resultado = client.system_one(
        state=estado,
        questions={
            "tema": Choice(
                instructions="Qual é o tema principal da solicitação?",
                criteria={
                    "relatorio": "Relatórios ou exportação de dados",
                    "acesso": "Login, senha ou permissões",
                    "cobranca": "Pagamento, plano ou fatura",
                },
            ),
            "precisa_intervencao": Noul(
                instructions="A equipe de suporte precisa intervir manualmente agora?",
            ),
        },
    )

print("Tema:", resultado.choices["tema"].choice)
print("Precisa de intervenção:", resultado.nouls["precisa_intervencao"].noul)
print("Resultado completo:", resultado)
