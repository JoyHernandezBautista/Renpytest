# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define P_color = "#00FF00"  # Green for Pixel
define A_color = "#FF0000"  # Red for Alberto
define Mc_color = "#0000FF"  # Blue for Mcoffee
define B_color = "#FFA500"  # Orange for BaseDatos
define J_color = "#800080"  # Purple for Jefe
define N_color = "#FFFFFF"  # White for Narrador

define N = Character("Narrador", color=N_color)
define A = Character("Alberto", color=A_color)
define P = Character("Pixel", color=P_color)
define PR = Character("Presidente")
define Mc = Character("McCoffee", color=Mc_color)
define B = Character("Base de datos", color=B_color)
define J = Character("Jefe", color=J_color)


# BACKGROUNDS 

image Historia:
    "historia.png"
    zoom 3.0

image BaseDatos:
    "basedatos.png"
    zoom 3.0

image Camino:
    "camino.png"
    zoom 3.0

image CasaAlberto:
    "casaalberto.png"
    zoom 3.0

image Desconocido:
    "desconocido.png"
    zoom 3.0

image FinalTragico:
    "final_tragico.png"
    zoom 3.0

image FinalPacifico:
    "finalpacifico.png"
    zoom 3.0

image Huida:
    "huida.png"
    zoom 3.0

image Terminal1:
    "terminal1.png"
    zoom 3.0

image Terminal2:
    "terminal2.png"
    zoom 3.0

image AlbertoBackground:
    "albert.png"
    zoom 3.0



# PERSONAJES SECUNDARIOS

image Jefe:
    "jefe.png"
    zoom 0.5

image McCoffee:
    "mccoffee.png"
    zoom 0.5

image Basedd:
    "basedd.png"
    zoom 0.5



# PIXEL

image Pixel_2:
    "PERSONAJE DISEÑO/2.png"
    zoom 0.5

image Pixel_3:
    "PERSONAJE DISEÑO/3.png"
    zoom 0.5

image Pixel_4:
    "PERSONAJE DISEÑO/4.png"
    zoom 0.5

image Pixel_5:
    "PERSONAJE DISEÑO/5.png"
    zoom 0.5

image Pixel_6:
    "PERSONAJE DISEÑO/6.png"
    zoom 0.5

image Pixel_7:
    "PERSONAJE DISEÑO/7.png"
    zoom 0.5

image Pixel_8:
    "PERSONAJE DISEÑO/8.png"
    zoom 0.5


# ALBERTO

image Alberto_Fastidiado:
    "PERSONAJE DISEÑO-2/FASTIDIADO.png"
    zoom 0.5

image Alberto_Hablando:
    "PERSONAJE DISEÑO-2/HABLANDO.png"
    zoom 0.5

image Alberto_Muerto:
    "PERSONAJE DISEÑO-2/MUERTO.png"
    zoom 0.5

image Alberto_Preocupado:
    "PERSONAJE DISEÑO-2/PREOCUPADO.png"
    zoom 0.5

image Alberto_Sonriendo:
    "PERSONAJE DISEÑO-2/SONRIENDO.png"
    zoom 0.5

image Alberto_Telefono:
    "PERSONAJE DISEÑO-2/TELEFONO.png"
    zoom 0.5



# El juego comienza aquí.


label start:
    
    scene Historia
    play music "audio/music.mp3"  # Play background music
    "En un mundo contemporáneo altamente tecnológico, donde la información es poder y la seguridad cibernética es una preocupación prioritaria para los gobiernos."
    "Dos personalidades se enfrentan en una lucha por la supervivencia."
    
    menu:
        "Acompañar a Pixel en esta aventura":
            $ protagonist = "Pixel"
            jump pixel_start

        "Acompañar a Alberto en esta aventura":
            $ protagonist = "Alberto"
            jump alberto_start


label pixel_start:
    scene Huida
    show Pixel_6 at center
    with dissolve

    "De repente eres consciente de tu existencia. No entiendes nada ¿cómo has llegado aquí? Solo recuerdas algo en tus datos: eres parte del código de seguridad para proteger la información secreta del Estado."


label pixel_scene2:
    scene CasaAlberto
    show Pixel_6 at left
    with dissolve

    "Sondeas el lugar y te das cuenta, es una habitación pequeña humana y hay una persona mirándote a través de la pantalla en la que te encuentras. Decides materializarte para entablar una conversación y pedir ayuda."

    menu:
        "Buscar ayuda":
            jump pixel_scene3
        "Hablar con el humano":
            jump pixel_scene4

label pixel_scene3:
    scene Terminal1
    show Pixel_6 at center
    with dissolve

    "Intentas hablar con tus compañeros pero te das cuenta de que eres incapaz de comunicarte con ellos, definitivamente hay algo mal."
    
    jump pixel_scene4

label pixel_scene4:
    scene CasaAlberto
    show Pixel_3 at left
    show Alberto_Preocupado at right
    with dissolve

    P "Hola, ha tenido que haber un error"
    A "¡Claro! Tú eres el error, vuelve al código, debo eliminarte antes de que sea tarde"
    P "¿Eliminarme?"
    A "¡Eres un peligro!"
    P "¡Tú me creaste!"


label pixel_scene5:
    scene Huida
    show Pixel_2 at center
    with dissolve

    "Estúpido humano ¡él me creó! No merezco ser destruido, no es mi culpa."

    menu:
        "Tomar venganza":
            jump pixel_scene6
        "Buscar ayuda":
            jump pixel_scene7


label pixel_scene6:
    scene Huida
    show Pixel_4 at center
    with dissolve

    "No me detendré, tú arruinaste mi vida Alberto, ahora yo te destruiré a ti y a tu ridículo país, pienso desvelar todos los secretos del Gobierno."

    jump pixel_scene8



label pixel_scene7:
    scene Huida
    show Pixel_7 at center
    with dissolve

    "No puede ser, no quiero ser eliminado. Tengo que encontrar a la base de datos."


label pixel_scene9:
    scene BaseDatos
    show Pixel_3 at left
    show Basedd at right
    with dissolve

    P "¿Tú puedes ayudarme? No he hecho nada, me persiguen para eliminarme"
    B "Lo siento pequeño pixel, me temo que lo mejor que puedes hacer por todos, es dejar que te eliminen. Tu creación supone un enorme peligro para nuestra red."
    P "¡No es justo!"

    jump pixel_scene6


label pixel_scene8:
    scene Terminal2
    show Pixel_5 at left
    with dissolve

    "¡Por fin! Tengo información suficiente para amenazar al gobierno, con esto deberán dejarme vivir."

    menu:
        "Amenazar al presidente":
            jump pixel_scene10
        "Conseguir más información":
            jump pixel_scene11


label pixel_scene10:
    scene Desconocido
    show Pixel_2 at left
    with dissolve

    "No puedes esperar más, así que te decides por entrar directamente al móvil personal del presidente. Sin embargo, hay algo que no te deja ¿será un sistema de seguridad?"

    jump pixel_scene12

label pixel_scene11:
    scene Huida
    show Pixel_2 at left
    with dissolve

    "Decides que no es suficiente y debes conseguir más datos del Gobierno, cuando te encuentras con alguien."

    jump pixel_scene12


label pixel_scene12:
    scene Desconocido
    show Pixel_2 at left
    show McCoffee at right
    with dissolve

    P "¿Tú quién eres?"
    Mc "Alberto me llama Mcoffee, me ha creado para detenerte."
    P "No te metas, al final te terminarán destruyendo como a todos."
    Mc "Yo no soy un error."


label pixel_scene13:
    scene Camino
    show Pixel_4 at left
    with dissolve

    "Tras una dura batalla en la que Mcoffee casi consigue borrarte de la red, te das cuenta de que no vivirás tranquilo, mientras Alberto te persiga."


label pixel_scene14:
    scene CasaAlberto
    show Pixel_8 at left
    show Alberto_Fastidiado at right
    with dissolve

    "Vuelves donde todo empezó, a aquella pequeña habitación."

    P "Estás empeñado en eliminarme, ¿eh?"
    A "Has arruinado mi vida, aunque te elimine, nada puede solucionarse ya."
    P "¡Tú arruinaste mi vida creándome mal!"
    A "No tienes ni idea de la gravedad de lo que has hecho, todos estamos en peligro por tu culpa."
    P "¿Y a mí por qué me tiene que importar eso?"
    A "Da igual que destruyas el país, eres un peligro en los códigos de seguridad, si no somos nosotros, otros te destruirán."

    menu:
        "Pelear":
            jump pixel_scene15
        "Negociar":
            jump pixel_scene16


label pixel_scene15:
    scene CasaAlberto
    show Pixel_4 at left
    show Alberto_Preocupado at right
    with dissolve

    P "Lo siento Alberto, pero me da igual que me persigan si a cambio destruyo al responsable de mi desgracia."

    # Jump to the ending scene
    jump ending_scene1


label pixel_scene16:
    scene CasaAlberto
    show Pixel_8 at left
    show Alberto_Hablando at right
    with dissolve

    P "¿Entonces? ¿Qué propones? ¿Que me deje eliminar?"
    A "No, pero puedes ayudarnos. Destruiste a Mcoffee, tienes más información que cualquier otro programa."
    P "Si hago eso ¿me dejaréis vivir?"
    A "Por supuesto"
    P "No confío en vosotros, tendéis a cometer errores"
    A "Puedes tenernos eternamente amenazados, dependeremos de que existas."

    # Jump to the ending scene
    jump ending_scene2


label ending_scene1:
    scene FinalTragico
    show Pixel_5 at left
    with dissolve
    show Alberto_Muerto at right
    with dissolve

    "Gracias al control que aprendí a tener de la electricidad, sobre cargué la habitación, hasta destruir a mi creador. Él tenía razón, ahora me persiguen por todo el mundo, pero mereció la pena."

    # End the visual novel
    return


label ending_scene2:
    scene FinalPacifico
    show Pixel_5 at left
    with dissolve

    "No parecía que tuviese otra opción, así que me convertí en el principal sistema de seguridad del mundo PIXEL: El error del sistema."

    # End the visual novel
    return




#Historia Alberto 

label alberto_start:
    scene CasaAlberto
    show Alberto_Fastidiado at left
    with dissolve

    "Ha sido un día de trabajo horrible. El ministerio de seguridad y codificación de la red te ha exigido el nuevo sistema de seguridad cibernética para mañana mismo. Se suponía que tenías un mes más."

    # Jump to the next scene
    jump alberto_scene2


label alberto_scene2:
    scene CasaAlberto
    show Alberto_Sonriendo at left
    with dissolve

    "¡Voy a acabar! Ya no queda nada. Espera ¡no puede ser!"

    show Alberto_Preocupado at left
    "Te das cuenta del enorme error que acabas de cometer al escribir el código, ya es demasiado tarde para corregirlo. ¿Qué puedes hacer?"

    # Updated menu options
    menu:
        "Intentar arreglar el problema":
            jump alberto_scene3
        "Destruir el sistema por completo":
            jump alberto_scene4


label alberto_scene3:
    scene CasaAlberto
    show Alberto_Sonriendo at left
    with dissolve

    "Lo piensas un momento y te das cuenta de que no terminarías uno nuevo desde cero a tiempo, necesitas arreglar el problema sí o sí."

    # Jump to scene 4
    jump alberto_scene4

label alberto_scene4:
    scene CasaAlberto
    show Alberto_Sonriendo at left
    with dissolve

    "Estás a punto de intentar solucionar el error antes de que se ejecute, pero el error toma consciencia y se materializa ante ti sin explicación lógica alguna."

    # Jump to the next scene
    jump alberto_scene5 


label alberto_scene5:
    scene CasaAlberto
    show Alberto_Preocupado at left
    show Pixel_2 at right
    with dissolve

    P "Hola, ha tenido que haber un error"
    A "¡Claro! Tú eres el error, vuelve al código, debo eliminarte antes de que sea tarde"
    P "¿Eliminarme?"
    A "¡Eres un peligro!"
    P "¡Tú me creaste!"

    # Jump to the next scene
    jump alberto_scene6


label alberto_scene6:
    scene CasaAlberto
    show Alberto_Fastidiado at left
    with dissolve

    "Te diriges a tu ordenador para destruir el código pero es tarde. Está fuera de control y consigue huir. No sabes qué hacer, vas a perder tu trabajo y probablemente tu vida. Todo por un simple pixel."

    menu:
        "Llamar al jefe":
            jump alberto_scene7
        "Perseguir a Pixel":
            jump alberto_scene8

label alberto_scene7:
    scene CasaAlberto
    show Alberto_Telefono at left
    show Jefe at right
    with dissolve

    A "Ha habido un problema, hay una brecha en la seguridad"
    J "Me da igual Alberto, para eso estás, para arreglar esas cosas ¿yo qué puedo hacer?"
    A "Me temo que esto es bastante más grave, el error tiene conciencia propia, no sé.."
    J "¡Basta! Soluciónalo, los hackers sirios no paran de atacarnos."
    A "Supongo que estoy solo."

    jump alberto_scene8

label alberto_scene8:
    scene Camino
    show Alberto_Fastidiado at left
    show McCoffee at right
    with dissolve

    "La única solución es crear un antivirus que consiga detener a Pixel. Vamos Mcoffee, a por él."

    jump alberto_scene9


label alberto_scene9:
    scene Camino
    show Alberto_Preocupado at left
    with dissolve

    "Mcoffee no ha podido detenerlo… voy a tener que recurrir a medidas más potentes… ¿qué está pasando?"
    "De repente la luz de tu casa dejó de funcionar, buscas el interruptor cuando aparece Pixel."

    jump pixel_scene14

