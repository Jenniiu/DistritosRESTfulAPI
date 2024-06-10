
# RESTful API em Python com FastAPI

RESTFul API em Python utilizando o
framework FastAPI que consuma dados de uma API. 


API escolhida: https://servicodados.ibge.gov.br/api/v1/localidades/distritos.


#### Funcionalidades
- Filtragem
- Agregação
- Containerização

### Executar aplicativo em contêiner

```
sudo docker build -t distritos-api .
sudo docker run -d -p 8000:8000 distritos-api
sudo docker logs <CONTAINER_ID>
```


## Documentação da API

#### Retorna todos os itens

```http
  GET /localidades/distritos
```

#### Retorna um distritos por id

```http
  GET /localidades/distritos/id/{id}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `int` | **Obrigatório**. O ID do item que você quer |


#### Retorna um distritos por nome

```http
  GET /localidades/distritos/nome/{nome}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `nome`      | `str` | **Obrigatório**. O nome do item que você quer |

#### Retorna um distritos por intervalo

```http
  GET /localidades/distritos/paginas
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `offset`      | `int` | **Obrigatório**. Número de distritos a pular |
| `limit`      | `int` | **Obrigatório**. Número de distritos a retornar|

#### Retorna um distritos pelo id do município

```http
  GET /localidades/distritos/municipio/{id_municipio}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `int` | **Obrigatório**. O ID do item que você quer |

#### Retorna um distritos por nome do município

```http
  GET /localidades/distritos/municipio/nome/{nome_municipio}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `nome`      | `str` | **Obrigatório**. O nome do item que você quer |

#### Retorna um distritos pelo id da microrregião

```http
  GET /localidades/distritos/microrregiao/{id_microrregiao}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `int` | **Obrigatório**. O ID do item que você quer |

#### Retorna um distritos por nome da microrregião

```http
  GET /localidades/distritos/microrregiao/nome/{nome_microrregiao}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `nome`      | `str` | **Obrigatório**. O nome do item que você quer |

#### Retorna um distritos pelo id da mesorregião

```http
  GET /localidades/distritos/mesorregiao/{id_mesorregiao}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `int` | **Obrigatório**. O ID do item que você quer |

#### Retorna um distritos por sigla da microrregião

```http
  GET /localidades/distritos//mesorregiao/UF/sigla/{sigla_UF}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `sigla`      | `str` | **Obrigatório**. O nome do item que você quer |


#### Retorna um distritos pelo id da mesorregião

```http
  GET /localidades/distritos/mesorregiao/nome/{nome_mesorregiao}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `nome`      | `str` | **Obrigatório**. O nome do item que você quer |

#### Retorna um distritos pelo id da unidade federativa do município

```http
  GET /localidades/distritos/mesorregiao/UF/nome/{nome_UF}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `int` | **Obrigatório**. O ID do item que você quer |

#### Retorna um distritos pela sigla da unidade federativa do município

```http
  GET /localidades/distritos/mesorregiao/UF/sigla/{sigla_UF}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `sigla`      | `str` | **Obrigatório**. O nome do item que você quer |


#### Retorna um distritos pelo nome da unidade federativa do município

```http
  GET /localidades/distritos/mesorregiao/UF/nome/{nome_UF}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `nome`      | `str` | **Obrigatório**. O nome do item que você quer |

#### Retorna um distritos pelo id da região do município

```http
  GET /localidades/distritos/mesorregiao/regiao/{id_regiao}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `int` | **Obrigatório**. O ID do item que você quer |

#### Retorna um distritos pela sigla da região do município

```http
  GET /localidades/distritos/mesorregiao/regiao/sigla/{sigla_regiao}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `sigla`      | `str` | **Obrigatório**. O nome do item que você quer |


#### Retorna um distritos pelo nome da sigla do municipio

```http
  GET /localidades/distritos/mesorregiao/regiao/nome/{nome_regiao}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `nome`      | `str` | **Obrigatório**. O nome do item que você quer |

#### Retorna um distritos pelo id da região imediata

```http
  GET /localidades/distritos/regiao-imediata/{id_regiaoimediata}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `int` | **Obrigatório**. O ID do item que você quer |

#### Retorna um distritos pelo nome da região imediata

```http
  GET /localidades/distritos/regiao-imediata/nome/{nome_regiao_imediata}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `nome`      | `str` | **Obrigatório**. O nome do item que você quer |

#### Retorna um distritos pelo id da região intermediária

```http
  GET /localidades/distritos/regiao-intermediaria/{id_regiaointermediaria}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `int` | **Obrigatório**. O ID do item que você quer |

#### Retorna um distritos pelo nome da região intermediária

```http
  GET /localidades/distritos/regiao-intermediaria/nome/{nome_regiaointermediaria}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `nome`      | `str` | **Obrigatório**. O nome do item que você quer |

#### Retorna um distritos pelo id da unidade federativa da região imediata

```http
  GET /localidades/distritos/regiao-imediata/UF/{id_UF_RI}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `int` | **Obrigatório**. O ID do item que você quer |

#### Retorna um distritos pela sigla da unidade federativa da região imediata

```http
  GET /localidades/distritos/regiao-imediata/UF/sigla/{sigla_UF_RI}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `sigla`      | `str` | **Obrigatório**. O nome do item que você quer |


#### Retorna um distritos pelo nome da unidade federativa da região imediata

```http
  GET /localidades/distritos/regiao-imediata/UF/nome/{nome_UF_RI}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `nome`      | `str` | **Obrigatório**. O nome do item que você quer |

#### Retorna um distritos pelo id da região da região imediata

```http
  GET /localidades/distritos/regiao-imediata/regiao/{id_regiao}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `int` | **Obrigatório**. O ID do item que você quer |

#### Retorna um distritos pela sigla da unidade federativa da região imediata

```http
  GET /localidades/distritos/regiao-imediata/regiao/sigla/{sigla_regiao_RI}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `sigla`      | `str` | **Obrigatório**. O nome do item que você quer |


#### Retorna um distritos pelo nome da unidade federativa da região imediata

```http
  GET /localidades/distritos/regiao-imediata/regiao/nome/{nome_regiao_RI}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `nome`      | `str` | **Obrigatório**. O nome do item que você quer |