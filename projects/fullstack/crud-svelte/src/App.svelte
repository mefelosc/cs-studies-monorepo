<script>
  import { todos } from './store.js';
  
  let newTodoText = '';
  let editingId = null;
  let editingText = '';

  function handleAdd() {
    if (newTodoText.trim()) {
      todos.add(newTodoText);
      newTodoText = '';
    }
  }

  function startEditing(todo) {
    editingId = todo.id;
    editingText = todo.text;
  }

  function saveEdit() {
    if (editingText.trim()) {
      todos.edit(editingId, editingText);
      editingId = null;
      editingText = '';
    }
  }

  function cancelEdit() {
    editingId = null;
    editingText = '';
  }
</script>

<main>
  <h1>Svelte CRUD Básico</h1>
  
  <div class="card">
    <div style="display: flex; margin-bottom: 2rem;">
      <input 
        type="text" 
        placeholder="Adicionar nova tarefa..." 
        bind:value={newTodoText} 
        on:keydown={(e) => e.key === 'Enter' && handleAdd()}
      />
      <button on:click={handleAdd}>Adicionar</button>
    </div>

    <ul class="item-list">
      {#each $todos as todo (todo.id)}
        <li class="item">
          {#if editingId === todo.id}
            <div style="display: flex; flex-grow: 1;">
              <input 
                type="text" 
                bind:value={editingText}
                on:keydown={(e) => {
                  if (e.key === 'Enter') saveEdit();
                  if (e.key === 'Escape') cancelEdit();
                }}
                style="flex-grow: 1;"
              />
            </div>
            <div class="actions">
              <button on:click={saveEdit}>Salvar</button>
              <button on:click={cancelEdit}>Cancelar</button>
            </div>
          {:else}
            <div style="display: flex; align-items: center; gap: 10px;">
              <input 
                type="checkbox" 
                checked={todo.completed} 
                on:change={() => todos.toggle(todo.id)}
              />
              <span style:text-decoration={todo.completed ? 'line-through' : 'none'}>
                {todo.text}
              </span>
            </div>
            <div class="actions">
              <button on:click={() => startEditing(todo)}>Editar</button>
              <button on:click={() => todos.remove(todo.id)}>Excluir</button>
            </div>
          {/if}
        </li>
      {:else}
        <p>Nenhuma tarefa encontrada.</p>
      {/each}
    </ul>
  </div>
</main>

<style>
  main {
    max-width: 600px;
    margin: 0 auto;
  }
</style>
