import os

def scrapTheme(theme, max_images):

    try:
        # Crear la carpeta
        os.mkdir(f"scrapped/{theme}")
        os.system(f"instagram-scraper {theme} --maximum {max_images} -d scrapped/{theme} -u benjaminmartincito341 -p supergoku")
        
        # Eliminar la foto de perfil
        directorio = os.listdir(f"scrapped/{theme}")
        directorio.sort()
        os.remove(f"scrapped/{theme}/{directorio[0]}")

    except:
        # Si falla
        return False


    return True

scrapTheme("memes_divertidoss_2.0", 3)  
