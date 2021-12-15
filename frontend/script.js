$( document ).ready(function() {
    
    $("#conteudoInicial").removeClass("invisible");

    $("#link_listar_estudantes").click(function(){
        
        $.ajax({
            url: 'http://localhost:5000/listar_estudantes',
            method: 'GET',
            dataType: 'json', // os dados são recebidos no formato json
            success: listar_estudantes, // chama a função listar_estudantes para processar o resultado
            error: function() {
                alert("erro ao ler dados, verifique o backend");
            }
        });
        function listar_estudantes(estudantes) {
            // inicializar um acumulador
            linhas = ""
            // percorrer as estudantes retornadas em json
            for (var i in estudantes) {

              // montar uma linha da tabela de estudantes
              lin = "<tr>" + 
              "<td>" + estudantes[i].nome + "</th>" + 
              "<td>" + estudantes[i].email + "</th>" + 
              "<td>" + estudantes[i].cpf + "</th>" + 
              
              "</tr>";

              // adicionar a linha da tabela em um acumulador
              linhas = linhas + lin;
            }
            // colocar as linhas na tabela
            $("#corpoTabelaEstudantes").html(linhas);

            // esconder todos os elementos da tela
            $("#conteudoInicial").addClass("invisible");
            $("#tabelaEstudantes").addClass("invisible");

            // exibir a tabela
            $("#tabelaEstudantes").removeClass("table invisible");
        }

    });

    $("#btn_incluir_estudante").click(function(){

        // obter os dados da tela (do formulário modal)
        nome_estudante = $("#nome_pessoa").val();
        email = $("#email").val();
        cpf = $("#cpf").val();
        disciplina = $("#nome_disciplina").val();
        cargaHoraria = $("#carga_horaria").val();
        ementa = $("#ementa").val();
        mediaFinal = $("#media_final").val();
        frequencia = $("#frequencia").val();

        // preparar os dados para envio (json)
        dados = JSON.stringify({nome : nome_estudante, email: email, 
            cpf: cpf, disciplina: disciplina, cargaHoraria: cargaHoraria, 
            ementa: ementa, mediaFinal: mediaFinal, frequencia: frequencia});

        // mandar para o back-end
        $.ajax({
            url : 'http://localhost:5000/incluir_pessoa',
            type : 'POST',
            contentType : 'application/json', // enviando dados em json
            dataType: 'json',
            data: dados,
            success: incluirEstudante,
            error: erroIncluirEstudante
        });
        function incluirEstudante(resposta) {
            if (resposta.resultado == "ok") {
                // exibe mensagem de sucesso
                alert('Estudante incluída com sucesso');
                // limpar valores dos campos do formulário
                $("#nome_pessoa").val("");
                $("#email").val("");
                $("#cpf").val("");
                $("#nome_disciplina").val("");
                $("#carga_horaria").val("");
                $("#ementa").val("");
                $("#media_final").val("");
                $("#frequencia").val("");
            } else {
                alert(resposta.resultado);
            }
        }
        function erroIncluirEstudante(resposta) {
            alert(resposta);
        }
    });
    

  });