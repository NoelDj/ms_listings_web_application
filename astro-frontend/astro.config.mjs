import { defineConfig } from 'astro/config';
import react from '@astrojs/react';
import svelte from '@astrojs/svelte';
import tailwind from "@astrojs/tailwind";

import node from "@astrojs/node";

export default defineConfig({
  output: 'server',
  site: 'https://example.com',
  adapter: node({
    mode: "standalone"
  }),
  integrations: [svelte(), react(), tailwind()]
});
