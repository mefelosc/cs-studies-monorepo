#!/usr/bin/env node

const note = process.argv[2]
const newNote = {
    content: note,
    id: Date.now(),     
    description: 'A simple note'
}

console.log(newNote);