import ast
import pandas as pd
import numpy as np
import seaborn as sns

generos = {
        'Drama', 'Comedy', 'Documentary', 'Horror', 'Thriller', 
        'Western', 'Action', 'Animation', 'Science Fiction', 
        'Crime', 'Music', 'Adventure'
    }

def generos_validos(genres_str,genre_field='name'):
    try:
        if pd.isna(genres_str) or genres_str.strip() == '[]':
            return False
        genres_list = ast.literal_eval(genres_str)
        genre_names = {g[genre_field] for g in genres_list}
        return len(genre_names) == 1 and genre_names.pop() in generos
    except:
        return False


def preprocesamiento_datos(df, overview_col='overview', genres_col='genres', genre_name='name'):
    mask_nonempty = df[overview_col].notna() & (df[overview_col].str.strip() != '')
    df = df[mask_nonempty]
    
    mascara_generos = df[genres_col].apply(generos_validos)
    df_filtrado = df[mascara_generos].copy()

    df_filtrado['genre'] = df_filtrado[genres_col].apply(lambda x: ast.literal_eval(x)[0][genre_name])
    
    return df_filtrado

def codificar_genero(df):
    genre2code = {g: idx for idx, g in enumerate(sorted(generos))}
    df["genre_code"] = df["genre"].map(genre2code)
    
    print("Diccionario género → código:", genre2code)
    
    return df

def test_data():
  paragraphs = [
        
    {"overview": "Cuando una abuela viral en redes sociales se muda con su nieto programador, el caos doméstico y los malentendidos digitales desatan una ola de risas, memes y momentos inolvidables.", "genre":"Comedy","label": 0, "title": "Cosas de Familia"},
    {"overview": "Tras la muerte de su padre, Elena encuentra una carta sin abrir que revela un amor prohibido. En su búsqueda por descubrir la verdad, enfrentará recuerdos dolorosos, secretos familiares y la posibilidad de una nueva vida.", "genre":"Drama","label": 1, "title": " La Última Carta"},
    {"overview": "Después de una tragedia que sacudió a su familia, Julián regresa a su pueblo natal para cuidar a su hermano menor. Enfrentado al peso del pasado y a viejas heridas, deberá reconciliarse con lo que fue y decidir quién quiere ser.", "genre":"Drama","label": 1, "title": "Ecos del Silencio"},

  ]
  return pd.DataFrame(paragraphs)
