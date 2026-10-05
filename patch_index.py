import re

with open('index.html', 'r') as f:
    content = f.read()

# The currently featured article snippet
old_featured = """    <section class="featured">
      <div class="label">Último artículo</div>
      <h2><a href="articles/ia-anticristo.html">La IA es el anticristo, o eso queremos creer</a></h2>
      <div class="meta">15 de septiembre, 2026 &nbsp;·&nbsp; Tecnología y sociedad</div>
      <p>
        Del miedo a Skynet al "anticristo" de Peter Thiel: el verdadero riesgo de la inteligencia artificial no es que se rebele, sino que le entreguemos, sin darnos cuenta, el criterio.
      </p>
      <a href="articles/ia-anticristo.html" class="read-more">Leer artículo &rarr;</a>
    </section>"""

new_featured = """    <section class="featured">
      <div class="label">Último artículo</div>
      <h2><a href="articles/crisis-vivienda-medellin.html">La crisis de la vivienda en Medellín: ¿hacia un colapso?</a></h2>
      <div class="meta">20 de octubre, 2026 &nbsp;·&nbsp; Sociedad colombiana</div>
      <p>
        Medellín se convirtió en la ciudad con el suelo más caro de Colombia. En la última década, el precio promedio de la vivienda se disparó entre un 80% y un 120%, según el sector.
      </p>
      <a href="articles/crisis-vivienda-medellin.html" class="read-more">Leer artículo &rarr;</a>
    </section>"""

# Replace featured section
content = content.replace(old_featured, new_featured)

new_article_item = """      <li class="article-item">
        <div class="date-block">
          <span class="day">15</span>
          sep.<br>2026
        </div>
        <div>
          <span class="tag">Tecnología y sociedad</span>
          <h3><a href="articles/ia-anticristo.html">La IA es el anticristo, o eso queremos creer</a></h3>
          <p class="snippet">Del miedo a Skynet al "anticristo" de Peter Thiel: el verdadero riesgo de la inteligencia artificial no es que se rebele, sino que le entreguemos, sin darnos cuenta, el criterio.</p>
        </div>
      </li>
"""

# Insert the old featured article into the article list
content = content.replace('<ul class="article-list">', '<ul class="article-list">\n' + new_article_item)

with open('index.html', 'w') as f:
    f.write(content)
