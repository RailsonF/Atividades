function fazerPedido() {
    let nomeinput = document.getElementById("nomever")
    let nome = nomeinput.value.trim()

    if (nome === '') {
        alert("Por favor, preencha o nome antes de fazer o pedido")
    }

    let selecionado = document.querySelector("input[name='tamanho']:checked");
    console.log('Tamanho:' + selecionado.value);
    let selecionados = document.querySelectorAll("input[name='adicionais']:checked");
    console.log('Quantidade de adicionais: ' + selecionados.length)

    // Definir os preços de cada tamanho usando if e else
    let precoPizza
    let tamanho = selecionado.value

    if (tamanho === "Pequena") {
        precoPizza = 25
    } else if (tamanho === "Média") {
        precoPizza = 35
    } else if (tamanho === "Grande") {
        precoPizza = 50
    } else {

        // Caso o tamanho não seja válido
        console.error("Tamanho inválido");
        return;
    }
    // Calculando o valor total 
    let valorAdicionais = 0
    for (let i = 0; i < selecionados.length; i++) {
        valorAdicionais += 5;
    }
    let valorTotal = precoPizza + valorAdicionais;
    valorTotal.textContent = `R$ ${valorTotal.toFixed(2)}`

    // Atualizando o valor total na página
    let total = document.getElementById("total");
    total.textContent = `R$ ${valorTotal.toFixed(2)}`;
    console.log('Valor total: ' + valorTotal)
}
