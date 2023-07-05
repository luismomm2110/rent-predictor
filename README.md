# Preditor de Aluguel 

RandomForestRegressor para predizer valores de alugueis com os parâmetros

- `area`: Representa a área da propriedade.
- `rooms`: Representa o número de quartos na propriedade.
- `bathroom`: Representa o número de banheiros na propriedade.
- `parking spaces`: Representa o número de vagas de estacionamento na propriedade.
- `hoa`: Representa a taxa do condomínio.
- `property tax`: Representa o valor do imposto predial.
- `fire insurance`: Representa o valor do seguro contra incêndio.
- `city`: cidade da propriedade. Precisa ser Belo Horizonte, Campinas, Porto Alegre, Rio de Janeiro ou São Paulo.
- `animal`: Indica se a propriedade não aceita animais. Valores aceitos: "acept" ou "not acept".
- `furniture`: Indica se a propriedade não está mobiliada. Valores aceitos: "furnished" ou "not furnished".


exemplo de valor válido 

```
{
  "city": "São Paulo",
  "area": 100,
  "rooms": 3,
  "bathroom": 2,
  "parking spaces": 1,
  "animal": "acept",
  "furniture": "furnished",
  "hoa": 800,
  "property tax": 300,
  "fire insurance": 80
}

```
