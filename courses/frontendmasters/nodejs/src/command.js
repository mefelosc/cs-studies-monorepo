#!/usr/bin/env node
import yargs from 'yargs';
import { hideBin } from 'yargs/helpers';

yargs(hideBin(process.argv))
  .command('curl <url> ', 'Fetch content from a URL', () => {}, (argv) => {
    console.info(argv)
  })  
    .demandCommand(1)
    .parse()