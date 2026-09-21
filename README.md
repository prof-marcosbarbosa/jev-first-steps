# Primeiro exemplo com Jev IA

Exemplo mínimo em Python 3.10+ para classificar a urgência de um chamado
usando o SDK oficial da TypeSafe e o modelo `jev-latest`.

## Preparar

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export TYPESAFE_API_KEY="sua-chave"
```

## Executar

```bash
python main.py
```

Saída esperada, em uma escala de 0.0 a 1.0:

```text
1.0
```

`TypeSafeClient` lê `TYPESAFE_API_KEY` do ambiente e usa `jev-latest` por
padrão. `Noul` avalia quanto o texto expressa uma condição, neste caso a
urgência do chamado.

## Outros exemplos

Os exemplos abaixo usam a mesma chave configurada no ambiente:

```bash
python examples/classificar_chamado.py
python examples/analisar_estado.py
python examples/async_chamado.py
```

### Classificar um chamado

[classificar_chamado.py](examples/classificar_chamado.py) combina os três tipos
de pergunta em uma única chamada:

- `Choice` escolhe uma categoria, como `tecnico` ou `vendas`.
- `Score` calcula uma pontuação a partir de uma lista ordenada de critérios.
- `Noul` retorna a probabilidade de uma resposta sim, entre 0.0 e 1.0.

### Avaliar estado estruturado

[analisar_estado.py](examples/analisar_estado.py) envia um dicionário com dados
do cliente, histórico de mensagens e tarefa atual. O campo `state` pode ser uma
string, objeto ou lista.

### Fazer chamadas assíncronas

[async_chamado.py](examples/async_chamado.py) usa `AsyncTypeSafeClient` e
`await`, adequado para aplicações que já trabalham com `asyncio`.

## API consultada

- [Python SDK](https://docs.typesafe.ai/sdk/python)
- [Guia de uso](https://docs.typesafe.ai/sdk/python/usage)
- [Referência da API](https://docs.typesafe.ai/api)