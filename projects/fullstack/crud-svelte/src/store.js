import { writable } from 'svelte/store';

function createTodos() {
	const { subscribe, set, update } = writable([
    { id: 1, text: 'Aprender Svelte', completed: false },
    { id: 2, text: 'Criar um CRUD', completed: false }
  ]);

	return {
		subscribe,
		add: (text) => update(n => {
      const newId = n.length > 0 ? Math.max(...n.map(t => t.id)) + 1 : 1;
      return [...n, { id: newId, text, completed: false }];
    }),
    remove: (id) => update(n => n.filter(t => t.id !== id)),
    toggle: (id) => update(n => {
      return n.map(t => {
        if (t.id === id) return { ...t, completed: !t.completed };
        return t;
      });
    }),
    edit: (id, newText) => update(n => {
       return n.map(t => {
        if (t.id === id) return { ...t, text: newText };
        return t;
       });
    })
	};
}

export const todos = createTodos();
