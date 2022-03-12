"""
AUTHOR: Luis Robbe Toichoa Sautoho AKA Doctor32
Aquí hemos hecho nuestro primer comentario larg  para documentar el archivo py.

Es importante tener en cuenta dos aspectos importantes:

1** A la hora de dibujar (y basándonos en los ejes cartesianos X Y) lo vamos a hacer
en el primer cuadrante (+X, +Y), es decir, el superior derecho. Nuestro origen (0, 0)
quedará por tanto en la parte izquierda más baja. Por tanto, todas las coordenadas
negativas quedarán fuera de la pantalla.

2** Cada punto es un pixel. Nuestra referencia es la dimensión de nuestra ventana.
Por ejemplo, si una ventana tiene un ancho de 800 píxeles, en coordenadas del eje X
iria de 0 a 799; en otras palabras, 800 píxeles. Sería un error no contar el 0 como pixel.
"""

# Importación librería arcade
import arcade

# Gracias a la librería arcade, abrimos una ventana
# Añadimos las dimensiones (anchura y altura)
# Añadimos el nombre la de ventana (Primer diseño)
arcade.open_window(600, 600, "Primer diseño")

# Añade color al fondo de la ventana
# No se mostrará si no añadimos las siguientes funciones de abajo
# Enlace para colores CSS: https://api.arcade.academy/en/latest/arcade.csscolor.html
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Esto indica que estamos preparados para dibujar
arcade.start_render()

# En este espacio haremos nuestro diseño

# Rectángulo
# Desde izquierda 0 a derecha 600
# Desde arriba 300 a abajo 0
arcade.draw_lrtb_rectangle_filled(0, 600, 300, 0, arcade.csscolor.DARK_OLIVE_GREEN)

# Tronco de arbol
# Centro de 100, 320
# Width of 20
# Height of 60
arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.csscolor.SIENNA)

# Esto delimita la función dibujar, indicando el fin del diseño
arcade.finish_render()

# La función run de arcade permite mantener abierta la ventana que hemos creado
# Tuve un error y no me mostraba el color de la ventana porque run estaba en la línea 15
# Por tanto, debe ir siempre al final para que así se mantenga la ventana que queremos
arcade.run()
