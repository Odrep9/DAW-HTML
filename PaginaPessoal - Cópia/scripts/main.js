console.log("JavaScript carregado com sucesso!");

function saudar(nome) {
    return "Olá, " + nome + "!";
}
console.log(saudar("Pedro"));

//Contador Simples
document.addEventListener('DOMContentLoaded', function () {

    let contadorElemento = document.getElementById('contador');
    let botaoIncrementar = document.getElementById('botao-incrementar');
    let botaoReset = document.getElementById('botao-reset');
    let contagem = 0;

    function incrementar() {
        contagem++;

        contadorElemento.textContent = contagem;
        console.log("Contador:", contagem);
    }
    function reiniciar() {
        contagem = 0;
        contadorElemento.textContent = contagem;
        console.log("Contador reiniciado");
    }
    botaoIncrementar.addEventListener('click', incrementar);
    botaoReset.addEventListener('click', reiniciar);

    // Relógio Digital
    function atualizarRelogio() {
        console.log("Atualizando relógio...");
        let agora = new Date();

        let horas = agora.getHours();
        let minutos = agora.getMinutes();
        let segundos = agora.getSeconds();

        horas = horas < 10 ? '0' + horas : horas;
        minutos = minutos < 10 ? '0' + minutos : minutos;
        segundos = segundos < 10 ? '0' + segundos : segundos;

        let horaFormatada = `${horas}:${minutos}:${segundos}`;

        let relogioElemento = document.getElementById('relogio');
        if (relogioElemento) {
            relogioElemento.textContent = horaFormatada;
        }
    }

    atualizarRelogio();
    setInterval(atualizarRelogio, 1000);
    elemento.addEventListener ('click', funcaoCallback);
});





