import { Readability } from '@mozilla/readability';
import { JSDOM } from 'jsdom';
import fetch from 'node-fetch';
import { readFileSync } from 'fs';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const PROXY_FILE = join(__dirname, '..', 'proxies.txt');

function carregarProxies(caminhoArquivo) {
    const conteudo = readFileSync(caminhoArquivo, 'utf-8');
    const proxies = [];
    
    for (const linha of conteudo.split('\n')) {
        const linhaLimpa = linha.trim();
        if (!linhaLimpa) continue;
        
        const partes = linhaLimpa.split(':');
        if (partes.length === 4) {
            const [ip, porta, usuario, senha] = partes;
            proxies.push({
                http: `http://${usuario}:${senha}@${ip}:${porta}`,
                https: `http://${usuario}:${senha}@${ip}:${porta}`
            });
        }
    }
    return proxies;
}

async function lerPagina(url, proxies) {
    for (const proxy of proxies) {
        try {
            const resposta = await fetch(url, {
                proxy: proxy.http,
                timeout: 10000
            });
            
            if (resposta.ok) {
                const html = await resposta.text();
                const dom = new JSDOM(html, { url });
                const reader = new Readability(dom.window.document);
                const artigo = reader.parse();
                
                return {
                    titulo: artigo.title,
                    conteudo: artigo.content,
                    autor: artigo.byline,
                    url: url
                };
            }
        } catch (erro) {
            continue;
        }
    }
    return null;
}

async function main() {
    const url = process.argv[2];
    
    if (!url) {
        console.log('Uso: node script/index.js <url>');
        process.exit(1);
    }
    
    console.log(`Carregando proxies de: ${PROXY_FILE}`);
    const proxies = carregarProxies(PROXY_FILE);
    console.log(`${proxies.length} proxies carregados`);
    
    console.log(`Lendo pagina: ${url}`);
    const resultado = await lerPagina(url, proxies);
    
    if (resultado) {
        console.log('\n=== RESULTADO ===');
        console.log(`Titulo: ${resultado.titulo}`);
        console.log(`Autor: ${resultado.autor}`);
        console.log(`Conteudo:\n${resultado.conteudo}`);
    } else {
        console.log('Nenhum proxy funcionou para esta URL.');
        process.exit(1);
    }
}

main();
