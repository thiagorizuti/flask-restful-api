# flask-restful-api

* Iniciar servidor: python server.py

* Cliente que usei para testes: https://goo.gl/tLOIVI

* endpoint /
  GET: retorna mensagem 
  POST: retorna mensagem 
  
* endpoint /info
  GET: retorna descrição
  POST: retorna inforamações solicitadas
    exemplo JSON de entrada: { "cpu": true, "memory": true, "hostname": false, "os": false}

* endpoint /arquivo
  GET: retorna descrição.
    acrescentando /nomedoarquivo: faz download do arquivo.
  POST: armazena arquivo
    arquivos .zip, nome do campo: file

* endpoint /arquivos
  GET: retorna lista de arquivos armazenados
  
