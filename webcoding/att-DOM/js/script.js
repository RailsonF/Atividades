function mudarBG(cor) {
    document.body.style.backgroundColor = cor
    let h1 = document.querySelector("h1")
    if (cor == "black" || cor == "#000000") {
        h1.style.color = "white"
    } else {
        h1.style.color = "black"
    }
}
let cor = prompt("informe o nome de uma cor ou o hexadecimal para ela ser aplicada ao fundo da página:")
mudarBG(cor)