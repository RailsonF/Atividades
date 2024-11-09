//Declarando as constantes que vão ser utilizada nas funções 
const desconto = 0.1;
const juros = 0.02;

//Criando os objetos
let product1 = {
    dsc_nome: "Teclado gamer Mechanike Pro",
    cod_produto: '123456',
    valor: 500
}

let product2 = {
    dsc_nome: "Mouse Atack Shark 11",
    cod_produto: '456789',
    valor: 300
}
//Crindo a função que vai calcular o preço do produto em função da quantidade de parcelas escohidas
function CalcularCompra(produto, numParcelas) {
    //Vai checar se a quantidade de parcelas está entre o permitido, se sim vai para a próxima condição
    if (numParcelas <= 12) {
        if (numParcelas <= 10) {
            if (numParcelas == 0) {
                let valor = produto.valor; //CRIANDO UMA VARIÁVEL QUE VAI RECEBER APENAS O VALOR DO PRODUTO
                let valorDescontado = valor * desconto;  // CRIANDO UMA VARIÁVEL QUE VAI RECEBER O VALOR DO PRODUTO VEZES O VALOR DA CONST DESCONTO QUE DEFINIMOS NO INÍCIO DO CÓDIGO
                console.log(`O valor com desconto é: ${valor - valorDescontado}`) // VAI EXIBIR NA TELA O VALOR DO PRODUTO COM O DESCONTO APLICADO
            } else {
                let valorParcelado = produto.valor / numParcelas
                console.log(`O valor da parcela é: ${valorParcelado}`)
            }

        } else {
            let valorDoJuros = produto.valor * juros
            let valorProdutoComJuros = produto.valor + valorDoJuros
            let valorParcelado = valorProdutoComJuros / numParcelas
            console.log(`O valor da parcela com juros é: ${valorParcelado}`)
        }
    } else {
        console.log("O número máximo de parcelas é 12")
    }

}
//Fazendo a chamada das funções para o produto 1 
CalcularCompra(product1,12)
CalcularCompra(product2,0)