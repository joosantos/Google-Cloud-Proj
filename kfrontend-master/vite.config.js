import { fileURLToPath } from "node:url";
import { resolve, dirname } from "node:path";
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import VueI18nPlugin from "@intlify/unplugin-vue-i18n/vite";

// https://vitejs.dev/config/
export default defineConfig({
	define: {
		// enable hydration mismatch details in production build
		__VUE_PROD_HYDRATION_MISMATCH_DETAILS__: "false",
	},
	plugins: [
		vue(),
		VueI18nPlugin({
			include: resolve(dirname(fileURLToPath(import.meta.url)), "./src/locales/**"),
		}),
	],
	server: {
		port: parseInt(process.env.VITE_PORT) || 3000,
		cors: true,
		strictPort: true,
		hmr: true,
		proxy: {
			"^/graphql": {
				target: process.env.VITE_API_URL || "http://127.0.0.1:8000",
				changeOrigin: true,
				rewrite: (path) => path.replace(/^\/graphql/, "/graphql"),
				ws: true,
			},
		},
		watch: {
			usePolling: true,
			useFsEvents: true,
		},
	},
	resolve: {
		alias: {
			"@": resolve(__dirname, "src"),
		},
	},
});
