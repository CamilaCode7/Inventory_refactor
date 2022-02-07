# Boas vindas ao repositório do projeto de Relatório de Estoque!

Lista de requisitos:
- [Requisitos obrigatórios]
- [1 - Criar um método `generate` numa classe `SimpleReport` do módulo `inventory_report/reports/simple_report.py`. Esse método deverá receber dados numa lista contendo estruturas do tipo `dict` e deverá retornar uma string formatada como um relatório](#1---criar-um-método-generate-numa-classe-simplereport-do-módulo-inventory_reportreportssimple_reportpy-esse-método-deverá-receber-dados-numa-lista-contendo-estruturas-do-tipo-dict-e-deverá-retornar-uma-string-formatada-como-um-relatório)
- [2 - Criar um método `generate` numa classe `CompleteReport` do módulo `inventory_report/reports/complete_report.py`. Esse método deverá receber dados numa lista contendo estruturas do tipo `dict` e deverá retornar uma string formatada como um relatório](#2---criar-um-método-generate-numa-classe-completereport-do-módulo-inventory_reportreportscomplete_reportpy-esse-método-deverá-receber-dados-numa-lista-contendo-estruturas-do-tipo-dict-e-deverá-retornar-uma-string-formatada-como-um-relatório)
- [3 - Criar um método `import_data` dentro de uma classe `Inventory` do módulo `inventory_report/inventory/inventory.py`, capaz de ler um arquivo CSV o qual o caminho é passado como parâmetro](#3---criar-um-método-import_data-dentro-de-uma-classe-inventory-do-módulo-inventory_reportinventoryinventorypy-capaz-de-ler-um-arquivo-csv-o-qual-o-caminho-é-passado-como-parâmetro)
- [4 - Criar um método `import_data` dentro de uma classe `Inventory` do módulo `inventory_report/inventory/inventory.py`, capaz de ler um arquivo JSON o qual o caminho é passado como parâmetro](#4---criar-um-método-import_data-dentro-de-uma-classe-inventory-do-módulo-inventory_reportinventoryinventorypy-capaz-de-ler-um-arquivo-json-o-qual-o-caminho-é-passado-como-parâmetro)
- [5 - Criar um método `import_data` dentro de uma classe `Inventory` do módulo `inventory_report/inventory/inventory.py`, capaz de ler um arquivo XML o qual o caminho é passado como parâmetro](#5---criar-um-método-import_data-dentro-de-uma-classe-inventory-do-módulo-inventory_reportinventoryinventorypy-capaz-de-ler-um-arquivo-xml-o-qual-o-caminho-é-passado-como-parâmetro)
- [6 - Criar uma classe abstrata `Importer` no módulo `inventory_report/importer/importer.py`, que terá três classes herdeiras: `CsvImporter`, `JsonImporter` e `XmlImporter`, cada uma definida em seu respectivo módulo](#6---criar-uma-classe-abstrata-importer-no-módulo-inventory_reportimporterimporterpy-que-terá-três-classes-herdeiras-csvimporter-jsonimporter-e-xmlimporter-cada-uma-definida-em-seu-respectivo-módulo)
- [7 - Criar uma classe `InventoryIterator` no módulo `inventory_report/inventory/inventory_iterator.py`, que implementa a interface de um iterator (`Iterator`). A classe `InventoryRefactor` deve implementar o método `__iter__`, que retornará este iterador](#7---criar-uma-classe-inventoryiterator-no-módulo-inventory_reportinventoryinventory_iteratorpy-que-implementa-a-interface-de-um-iterator-iterator-a-classe-inventoryrefactor-deve-implementar-o-método-__iter__-que-retornará-este-iterador)


## O que deverá ser desenvolvido

No projeto passado você implementou algumas funções que faziam leitura e escrita de arquivos `JSON` e `CSV`, correto? Neste projeto nós vamos fazer algo parecido, mas utilizando a Programação Orientada a Objetos! Você implementará um gerador de relatórios que recebe como entrada arquivos com dados de um estoque e gera, como saída, um relatório acerca destes dados.

Esses dados de estoque poderão ser obtidos de diversas fontes:

- Através da importação de um arquivo `CSV`;

- Através da importação de um arquivo `JSON`;

- Através da importação de um arquivo `XML`;

Além disso, o relatório final deverá poder ser gerado em duas versões: simples e completa.
