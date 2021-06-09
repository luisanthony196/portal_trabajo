def listar(cur):
    cur.execute("SELECT ofertaperfil_id, descripcion_normalizada, count(*) FROM oferta_detalle WHERE ofertaperfil_id=4 GROUP BY ofertaperfil_id, descripcion_normalizada ORDER BY 1,2,3 DESC;")

def remover_espacios(cur):
    cur.execute("UPDATE oferta_detalle SET descripcion_normalizada = TRIM(descripcion_normalizada) WHERE ofertaperfil_id=4;")

def remover_acentos(cur):
    cur.execute("UPDATE oferta_detalle SET descripcion_normalizada = REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(descripcion_normalizada, 'á', 'a'), 'é', 'e'), 'í', 'i'), 'ó', 'o'), 'ú', 'u') WHERE ofertaperfil_id=4;")

def remover_numeracion(cur):
    cur.execute("UPDATE oferta_detalle SET descripcion_normalizada = REGEXP_REPLACE(descripcion_normalizada, '^\(?[A-Z0-9]+(\)|\.)+\s*', '') WHERE ofertaperfil_id=4;")

def remover_vinetas(cur):
    cur.execute("UPDATE oferta_detalle SET descripcion_normalizada = REGEXP_REPLACE(descripcion_normalizada, '^[^[a-zA-Z0-9\(\<\¿\&]+', '') WHERE ofertaperfil_id=4;")