document.querySelectorAll('.simbolo, .simbolo_segundo, .numero_zero, .numero, .virgula').forEach(button => {
    button.addEventListener('click', function() {
        const valor = this.getAttribute('data-op');
        document.getElementById('valor').value = valor;
        document.getElementById('calculator-form').submit();
    });
});


const resposta = document.getElementById('resposta');

        // Configura um evento para verificar o overflow ao pressionar as setas direita e esquerda
        window.addEventListener('keydown', (event) => {
            if (event.key === 'ArrowRight') {
                resposta.scrollLeft += 10; // desloca o texto para a direita
            } else if (event.key === 'ArrowLeft') {
                resposta.scrollLeft -= 10; // desloca o texto para a esquerda
            }
        });