<script>
  // 1. Reatividade Simples (Svelte 5 usa $state)
  let count = $state(0);

  function increment() {
    count += 1;
  }

  // 2. Declarações Reativas ($derived)
  // No Svelte 5, usamos $derived em vez de $:
  let double = $derived(count * 2);

  // Efeitos colaterais ($effect)
  $effect(() => {
    if (count >= 10) {
      console.log("Chegamos a 10!");
    }
  });

  // 3. Two-way Binding
  let name = $state("");
</script>

<main>
  <h1>Svelte 5 é incrível!</h1>

  <section>
    <h2>1. Reatividade</h2>
    <p>O contador é: {count}</p>
    <button onclick={increment}>
      Incrementar
    </button>
  </section>

  <hr />

  <section>
    <h2>2. Declaração Reativa</h2>
    <p>{count} dobrado é {double}</p>
  </section>

  <hr />

  <section>
    <h2>3. Binding (Ligação de Dados)</h2>
    <input bind:value={name} placeholder="Digite seu nome" />
    <p>Olá, {name ? name : 'estranho'}!</p>
  </section>
</main>

<style>
  main {
    padding: 1em;
  }
  section {
    margin: 20px 0;
  }
  input {
    padding: 8px;
    border-radius: 4px;
    border: 1px solid #ccc;
  }
</style>
