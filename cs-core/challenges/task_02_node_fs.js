
const fs = require('fs');

const conteudo = fs.readdirSync('.');

conteudo.forEach((arquivo) => {
    if (arquivo.endsWith('.js')) {
        console.log(arquivo);
    }
});
