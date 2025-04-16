transform camera_shake:
    linear 0.05 xoffset -10 yoffset 5
    linear 0.05 xoffset 8 yoffset -5
    linear 0.05 xoffset -6 yoffset 4
    linear 0.05 xoffset 4 yoffset -4
    linear 0.05 xoffset 0 yoffset 0

    transform shock:
        linear 0.05 xoffset -10
        linear 0.05 xoffset 10
        linear 0.05 xoffset -10
        linear 0.05 xoffset 10
        linear 0.05 xoffset 0

    define heroe = Character("Fact", color="#0062f5")
    define yuri = Character("Yuri", color="#e419b1")
    define campesina = Character("Campesina", color="#e419b1")
    define des = Character("???", color="#e419b1")
    define alex = Character("Alex", color="#e60000")
    define mounstro = Character("Mounstro", color="#e60000")


    label start:

        scene fondo1

        "Qué lindo día."
        "Todo muy tranqui y..."

        show fondo1 at camera_shake  

        des "¡AYUDAAA!"

        "!!"
        "al parecer alguien necesita mi ayuda!"

        show fondo_arbol
        
        show hombre_normal 
        hide hombre_normal
        
        show hombre_enojado at center
        
        des "¡Ayudaaaa!"

        mounstro "¡Ya!"

        hide hombre_normal
        show hombre_enojado at center with shock

        mounstruo "¡CALLATE!"

        return
