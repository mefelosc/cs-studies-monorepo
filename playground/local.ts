// Criar uma interface `Person` com name, age e hobbies
// Preencher os 2 com seus dados

interface Person {
    name: string;
    age: number;
    hobbies: string[];
}

const user: Person = {
    name: "Carlos Felipe",
    age: 24,
    hobbies: ["futebol", "música", "viagens"]
};

function greet(user: Person): string {
    return `Olá, meu nome é ${user.name}, tenho ${user.age} anos e meus hobbies são: ${user.hobbies.join(", ")}.`;
}

console.log(greet(user));