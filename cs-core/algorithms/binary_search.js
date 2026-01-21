function binarySearch(arr, target) {
    let left = 0;
    let right = arr.length - 1;

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        
        if (arr[mid] === target) return arr[mid]; // Retorna o elemento encontrado
        
        if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return "Não Encontrado"; // Retorna mensagem se o elemento não for encontrado
}

const fruits = ["maçã", "banana", "cereja", "figo", "laranja", "manga", "pera"];

console.log(`Nós temos o seguinte item em estoque: ${binarySearch(fruits, "pera")}`); 
console.log(`Nós temos o seguinte item em estoque: ${binarySearch(fruits, "figo")}`); 
