<script>
  let email = '';
  let subscribed = false;

  function handleSubscribe() {
    if (email) {
      subscribed = true;
      email = '';
    }
  }
</script>

<main>
  <nav>
    <div class="logo">MinhaMarca</div>
    <div class="links">
      <a href="#features">Recursos</a>
      <a href="#about">Sobre</a>
      <a href="#contact">Contato</a>
    </div>
  </nav>

  <header class="hero">
    <h1>Bem-vindo à Minha Landing Page</h1>
    <p>Uma solução simples para seus problemas complexos.</p>
    <button on:click={() => document.getElementById('features').scrollIntoView({ behavior: 'smooth' })}>Saiba Mais</button>
  </header>

  <section id="features" class="features">
    <div class="feature-card">
      <h3>Rápido</h3>
      <p>Performance otimizada para a melhor experiência.</p>
    </div>
    <div class="feature-card">
      <h3>Seguro</h3>
      <p>Seus dados protegidos com a mais alta tecnologia.</p>
    </div>
    <div class="feature-card">
      <h3>Fácil de Usar</h3>
      <p>Interface intuitiva pensada no usuário.</p>
    </div>
  </section>

  <section class="newsletter">
    <h2>Fique por dentro</h2>
    <p>Inscreva-se para receber novidades.</p>
    
    {#if subscribed}
      <p class="success-message">Obrigado por se inscrever!</p>
    {:else}
      <div class="input-group">
        <input type="email" bind:value={email} placeholder="Seu melhor e-mail" />
        <button on:click={handleSubscribe}>Inscrever</button>
      </div>
    {/if}
  </section>

  <footer>
    <p>&copy; 2026 Minha Landing Page. Todos os direitos reservados.</p>
  </footer>
</main>

<style>
  :global(body) {
    margin: 0;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: #333;
    line-height: 1.6;
  }

  nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 2rem;
    background-color: #fff;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    position: sticky;
    top: 0;
  }

  .logo {
    font-weight: bold;
    font-size: 1.5rem;
    color: #ff3e00;
  }

  .links a {
    text-decoration: none;
    color: #333;
    margin-left: 1.5rem;
    transition: color 0.3s;
  }

  .links a:hover {
    color: #ff3e00;
  }

  .hero {
    background: linear-gradient(135deg, #ff3e00 0%, #ff8e53 100%);
    color: white;
    text-align: center;
    padding: 5rem 2rem;
  }

  .hero h1 {
    font-size: 3rem;
    margin-bottom: 1rem;
  }

  .hero button {
    background-color: white;
    color: #ff3e00;
    border: none;
    padding: 0.8rem 2rem;
    font-size: 1.2rem;
    border-radius: 5px;
    cursor: pointer;
    font-weight: bold;
    margin-top: 2rem;
    transition: transform 0.2s;
  }

  .hero button:hover {
    transform: scale(1.05);
  }

  .features {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
    padding: 4rem 2rem;
    max-width: 1200px;
    margin: 0 auto;
  }

  .feature-card {
    background: #f9f9f9;
    padding: 2rem;
    border-radius: 8px;
    text-align: center;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    transition: box-shadow 0.3s;
  }

  .feature-card:hover {
    box-shadow: 0 8px 12px rgba(0,0,0,0.1);
  }

  .newsletter {
    background-color: #333;
    color: white;
    text-align: center;
    padding: 4rem 2rem;
  }

  .input-group {
    margin-top: 1.5rem;
    display: flex;
    justify-content: center;
    gap: 10px;
  }

  input {
    padding: 0.8rem;
    border-radius: 4px;
    border: none;
    width: 300px;
    font-size: 1rem;
  }

  .newsletter button {
    padding: 0.8rem 1.5rem;
    background-color: #ff3e00;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 1rem;
    cursor: pointer;
  }

  .success-message {
    color: #4cd964;
    font-weight: bold;
    font-size: 1.2rem;
  }

  footer {
    text-align: center;
    padding: 2rem;
    background-color: #222;
    color: #888;
    font-size: 0.9rem;
  }
</style>
