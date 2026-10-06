---
name: importar-produtos-backup-miniaturas
description: Importa produtos (CSV) para vendedor WooCommerce/Dokan com backup de banco antes, deduplicacao segura, criacao de categorias, foto do vendedor em produtos sem imagem, publicacao/rascunho e regeneracao de miniaturas em todas as resolucoes.
triggers: ['importar csv', 'importar produtos', 'backup banco', 'mysqldump', 'miniaturas', 'regenerar thumbnails', 'criar categorias', 'vendedor dokan', 'publicar produtos', 'rascunho', 'deduplicar', 'produtos sem foto']
---

# Skill: Importar Produtos com Backup de BD e Miniaturas

Skill de importacao de produtos (CSV) em loja WooCommerce + Dokan, com:
backup obrigatorio antes de qualquer escrita, deduplicacao segura, criacao de
categorias, atribuicao ao vendedor correto, foto do vendedor para produtos sem
imagem, publicacao (ou rascunho) e regeneracao de miniaturas em todas as
resolucoes.

## Fluxo obrigatorio (nesta ordem)

### 1. Backup ANTES de tocar em qualquer dado

- Banco: `mysqldump --single-transaction --quick -h 127.0.0.1 -u <user> -p'<pass>' <db> | gzip > /www/backups/<db>-db-<STAMP>.sql.gz`
- Arquivos: `tar czf /www/backups/<db>-files-<STAMP>.tar.gz -C <raiz> wp-content wp-config.php <csv>`
- Guarde o STAMP: `echo "STAMP=..." > /tmp/backup_stamp`
- O dump tambem serve para RESTAURAR itens apagados por engano (extrair linha do backup).

### 2. Identificar o vendedor (Dokan usa post_author)

- `SELECT u.ID, u.display_name FROM wp_<prefix>_users u ... WHERE display_name LIKE '%<nome>%'`
- Produtos do vendedor: `post_type='product' AND post_author=<ID>`
- Nao existe meta especial: o vinculo vendedor-produto e o post_author.

### 3. Ler o CSV com header normalizado

- O CSV costuma ter BOM (`\xEF\xBB\xBF`) e aspas literais no header.
- SEMPRE normalizar o header antes de `array_combine`:
  `$header = array_map(fn($h) => trim($h, "\"\xEF\xBB\xBF "), $header);`
- Se nao normalizar, `$r['Código']` nao casa com a chave real `"Código"` e o SKU
  nunca e salvo -> a dedup por SKU falha e produtos sao duplicados na re-execucao.

### 4. Criar categorias que faltam

- `wp_insert_term($cat, 'product_cat')` exige admin. No WP-CLI setar usuario admin
  no inicio: `wp_set_current_user(2);` (ou o ID admin do site).
- Sem isso: "You do not have permission to create product category".

### 5. Deduplicar com filtro de autor CORRETO

- ATENCAO: `get_posts(['post_author' => X])` NAO filtra por autor! O parametro
  correto e `'author' => X`. Usar `post_author` varre a loja INTEIRA e pode
  apagar produtos de outros vendedores (falso positivo).
- Dedup por SKU (`wc_get_product_id_by_sku`) E por titulo+preco do MESMO autor.

### 6. Importar produtos

- Inserir com `wp_insert_post(['post_type'=>'product','post_status'=>'publish',
  'post_title'=>$titulo,'post_author'=>$seller])` + `wp_set_object_terms($id,'simple','product_type')`
  + metas `_regular_price`, `_price`, `_manage_stock=yes`, `_stock`, `_stock_status`,
  `_visibility=visible`, `_sku`.
- Categoria: `wp_set_object_terms($id, $term_id, 'product_cat')`.
- Imagem: baixar URL com wp_remote_get (timeout 25, user-agent browser, sslverify
  false), media_handle_sideload + set_post_thumbnail. Falhas sao aceitaveis.

### 7. Foto do vendedor em produtos sem foto

- Produto sem `_thumbnail_id` recebe a foto do vendedor:
  `set_post_thumbnail($pid, $avatar_id)` onde $avatar_id = `dokan_profile_settings.gravatar`.
- Se a regra de negocio for "sem foto = rascunho", mover para draft DEPOIS de
  aplicar a foto: `wp_update_post(['ID'=>$pid,'post_status'=>'draft'])`.

### 8. Regenerar miniaturas (todas resolucoes)

- `wp_generate_attachment_metadata($att_id, $file)` + `wp_update_attachment_metadata`.
- IMPORTANTE: o PHP CLI padrao (8.1) pode nao ter GD (so Imagick); o WP cai para
  GD em alguns formatos e morre com "Call to undefined function imagecreatefromstring()".
- Rodar com PHP que tenha GD: `/usr/bin/php83 /usr/local/bin/wp eval-file <script>`.
- Verificar antes: `php -r "var_dump(function_exists('imagecreatefromstring'));"`.

### 9. Verificar por observacao

- Contagens no banco: produtos por status, com/sem `_thumbnail_id`, categorias.
- Testar pagina real no navegador (Playwright) quando envolver frontend.
- Cache pode servir HTML antigo: testar com `?cb=1` para confirmar.

## Armadilhas conhecidas

- Header CSV com BOM/aspas -> SKU nunca salvo -> duplicacao.
- `post_author` no get_posts -> varre loja inteira -> apaga produto de outro vendedor.
- wp_insert_term sem admin -> permission denied.
- PHP CLI sem GD -> fatal ao regenerar webp/png.
- Preloader/cache stale pode esconder correcoes de frontend (testar com cache-buster).

## Output esperado

- Relatorio final com: total importado, duplicados pulados, imagens baixadas,
  sem-foto tratados (foto do vendedor ou rascunho), miniaturas regeneradas,
  backup criado com caminho.
