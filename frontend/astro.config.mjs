import { defineConfig } from 'astro/config';
import react from '@astrojs/react';
import netlify from '@astrojs/netlify/functions';
import tailwind from "@astrojs/tailwind";

import node from "@astrojs/node";

export default defineConfig({
  output: 'server',
  site: 'https://example.com',
  adapter: node({
    mode: "standalone"
  }),
  integrations: [react(), tailwind()]
});
