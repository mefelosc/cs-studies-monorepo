

class BrowserHistory {
    constructor() {
        this.backStack = [];    // Pilha para páginas anteriores
        this.forwardStack = []; // Pilha para páginas seguintes
        this.currentPage = "google.com";
    }

    // Visitar uma nova página
    visit(url) {
        this.backStack.push(this.currentPage);
        this.currentPage = url;
        this.forwardStack = []; // Sempre que visitamos algo novo, limpamos o futuro
        console.log(`Visitou: ${this.currentPage}`);
    }

    // Voltar na navegação
    back() {
        if (this.backStack.length > 0) {
            this.forwardStack.push(this.currentPage);
            this.currentPage = this.backStack.pop();
            console.log(`Voltou para: ${this.currentPage}`);
        } else {
            console.log("Sem histórico para voltar.");
        }
    }

    // Avançar na navegação
    forward() {
        if (this.forwardStack.length > 0) {
            this.backStack.push(this.currentPage);
            this.currentPage = this.forwardStack.pop();
            console.log(`Avançou para: ${this.currentPage}`);
        } else {
            console.log("Sem histórico para avançar.");
        }
    }
}

const nav = new BrowserHistory();
nav.visit("github.com");
nav.visit("youtube.com");
nav.back();    // Deve voltar para github.com
nav.forward(); // Deve avançar para youtube.com
