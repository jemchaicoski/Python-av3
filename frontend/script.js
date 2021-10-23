$( document ).ready(function() {
    
    $("#conteudoInicial").removeClass("invisible");

    $("#link_listar_pessoas").click(function(){
        
        $.ajax({
            url: 'http://localhost:5000/listar_pessoas',
            method: 'GET',
            dataType: 'json', // os dados são recebidos no formato json
            success: listar_pessoas, // chama a função listar_pessoas para processar o resultado
            error: function() {
                alert("erro ao ler dados, verifique o backend");
            }
        });
        function listar_pessoas(pessoas) {
            // inicializar um acumulador
            linhas = ""
            // percorrer as pessoas retornadas em json
            for (var i in pessoas) {

              // montar uma linha da tabela de pessoas
              lin = "<tr>" + 
              "<td>" + pessoas[i].nome + "</th>" + 
              "<td>" + pessoas[i].email + "</th>" + 
              "<td>" + pessoas[i].telefone + "</th>" + 
              
              "</tr>";

              // adicionar a linha da tabela em um acumulador
              linhas = linhas + lin;
            }
            // colocar as linhas na tabela
            $("#corpoTabelaPessoas").html(linhas);

            // esconder todos os elementos da tela
            $("#conteudoInicial").addClass("invisible");
            $("#tabelaPessoas").addClass("invisible");

            // exibir a tabela
            $("#tabelaPessoas").removeClass("table invisible");
        }

    });

    $("#btn_incluir_pessoa").click(function(){

        // obter os dados da tela (do formulário modal)
        nome_pessoa = $("#nome_pessoa").val();
        email = $("#email").val();
        telefone = $("#telefone").val();

        // preparar os dados para envio (json)
        dados = JSON.stringify({nome : nome_pessoa, email: email, 
            telefone: telefone,});

        // mandar para o back-end
        $.ajax({
            url : 'http://localhost:5000/incluir_pessoa',
            type : 'POST',
            contentType : 'application/json', // enviando dados em json
            dataType: 'json',
            data: dados,
            success: incluirPessoa,
            error: erroIncluirPessoa
        });
        function incluirPessoa(resposta) {
            if (resposta.resultado == "ok") {
                // exibe mensagem de sucesso
                alert('Pessoa incluída com sucesso');
                // limpar valores dos campos do formulário
                $("#nome_pessoa").val("");
                $("#email").val("");
                $("#telefone").val("");
            } else {
                alert('erro na comunicação');
            }
        }
        function erroIncluirPessoa(resposta) {
            alert("Deu ruim na chamada ao back-end");
        }
    });
    

  });