$(function () {
    $.ajax({
        url: 'http://localhost:5000/criar_tabelas',
        type: 'GET',
    });

    $(document).on("click", "#bt_submeter", function () {

        // coletar os dados
        var vetor_dados = $("#meu_formulario").serializeArray();

        // exemplo de retorno:
        // [{"name":"email","value":"soueu@gmail.com"},{"name":"time","value":"2"},
        // {"name":"nasci_brasil","value":"True"},{"name":"turno","value":"2"},...]

        // converter para chave:valor
        var chave_valor = {};
        for (var i = 0; i < vetor_dados.length; i++){
            chave_valor[vetor_dados[i]['name']] = vetor_dados[i]['value'];
        }
        
        // tratamento especial para o CHECKBOX nasci_brasil
        // verificar se ele está marcado ou não
        chave_valor['nasci_brasil'] = $("#nasci_brasil").is(":checked") ? '1' : '0'
        chave_valor['filho_unico'] = $("#filho_unico").is(":checked") ? '1' : '0'

        //alert(dados);
        var dados_json = JSON.stringify(chave_valor);
        console.log(dados_json);
        
        $.ajax({
            url: 'http://localhost:5000/incluir',
            type: 'POST',
            dataType: 'json', // dados recebidos em json
            contentType: 'application/json', // dados enviados em json
            data: dados_json,
            success: pessoaIncluida,
            error: erroAoIncluir
        });
        function pessoaIncluida (retorno) {
            if (retorno.resultado == "ok") { // a operação deu certo?
                alert("Pessoa incluída com sucesso!");
            } else {
                alert("ERRO na inclusão: "+retorno.resultado + ":" + retorno.detalhes);
            }            
        }
        function erroAoIncluir (retorno) {
            alert("ERRO ao contactar back-end: "+retorno.resultado + ":" + retorno.detalhes);
        }

        
    });

    $(document).on("click", "#bt_preencher", function () {

        $("#email").val("soueu@gmail.com");

        // usar \n para quebra de linha
        $("#habilidades").val("tocar teclado\n nadar os quatro estilos\n jogar fluft");

        // informa o VALUE do OPTION selecionado
        $("#time").val("2"); 

        // definido os checkboxes
        $("#nasci_brasil").prop('checked', true);
        $("#filho_unico").prop('checked', false);

        // definindo o radiobutton pelo ID, em vez de pelo valor
        $("#turno2").prop('checked', true);

        // definindo o valor de um checkbox estilizado
        $("#viajou_fora_sc").prop('checked', true);

        // definindo o valor de um checkbox em forma de botão
        $("#viajou_fora_sc").prop('checked', true);

        // definindo o valor do radiobutton pelo VALOR    
        $('input:radio[name=restricao]').val(['Vegana']);
        
        // definindo o valor o range e do outout
        $("#expectativa_vida").val("67"); 
        $("#saida_valor_expectativa").val("67");

        // definindo outros campos
        $("#cor_preferida").val("verde");
        $("#musicas_preferidas").val("haleluia \n xote dos milagres");
        $("#livros_por_ano").val("2");
    });


});