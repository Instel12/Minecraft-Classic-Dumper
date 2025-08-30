import os
import requests

root_assets_dir = os.path.join(os.getcwd(), 'assets')

index = '''
<!doctype html>
<!--[if lt IE 7]><html class="no-js ie ie6 lt-ie9 lt-ie8 lt-ie7" lang="sv-SE"> <![endif]-->
<!--[if IE 7]><html class="no-js ie ie7 lt-ie9 lt-ie8" lang="sv-SE"> <![endif]-->
<!--[if IE 8]><html class="no-js ie ie8 lt-ie9" lang="sv-SE"> <![endif]-->
<!--[if gt IE 8]><!-->
<html class="no-js" lang="sv-SE" prefix="og: http://ogp.me/ns#"> <!--<![endif]-->
<head>
    <meta charset="UTF-8"/>
    <title>Minecraft Classic</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="google" content="notranslate" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <link href="/assets/css/style.css" rel="stylesheet">
</head>
<body>
    <div class="page-content">
        <main role="main" class="u-main"></main>
    </div>
    <div id="hide"><textarea class="js-copytextarea">url_to_copy</textarea></div>
    <div id="version"></div>
    <div id="hotbar"></div>
    <div id="previewWindow"></div>
    <div id="chat"></div>
    <div id="menu"></div>
    <div id="progress"></div>
    <div id="overlay"></div>
    <div id="mobile">
        <div id="text_vertical">
            <p><h2>Sorry!</h2></p>
            <p>This version of Minecraft<br>requires a keyboard.</p>
            <p>Please try again on another device.</p>
        </div>
    </div>
    <div id="webgl_webrtc">
        <div id="text_vertical">
            <p><h2>Sorry!</h2></p>
            <p>It seems like your browser doesn’t support<br>WebGL or WebRTC that is required to run this game.</p>
            <p>Find a new one at <a href="https://browsehappy.com" target="_blank">https://browsehappy.com</a></p>
        </div>
    </div>
    <script src="/assets/js/app.js"></script>
</body>
</html>
'''

dirs = [
    "css",
    "fonts",
    "js",
    "sounds",
    "textures",
    "textures/previews"
]

downloads = [
    "css/style.css",
    "fonts/minecraftfont.woff",
    "js/app.js",
    "sounds/calm1.mp3",
    "sounds/calm2.mp3",
    "sounds/calm3.mp3",
    "sounds/grass1.mp3",
    "sounds/grass2.mp3",
    "sounds/grass3.mp3",
    "sounds/grass4.mp3",
    "sounds/gravel1.mp3",
    "sounds/gravel2.mp3",
    "sounds/gravel3.mp3",
    "sounds/gravel4.mp3",
    "sounds/stone1.mp3",
    "sounds/stone2.mp3",
    "sounds/stone3.mp3",
    "sounds/stone4.mp3",
    "sounds/wood1.mp3",
    "sounds/wood2.mp3",
    "sounds/wood3.mp3",
    "sounds/wood4.mp3",
    "textures/bedrock.png",
    "textures/brown_mushroom.png",
    "textures/bush.png",
    "textures/button.png",
    "textures/button_over.png",
    "textures/clouds.png",
    "textures/color0.png",
    "textures/color1.png",
    "textures/color10.png",
    "textures/color11.png",
    "textures/color12.png",
    "textures/color13.png",
    "textures/color14.png",
    "textures/color15.png",
    "textures/color2.png",
    "textures/color3.png",
    "textures/color4.png",
    "textures/color5.png",
    "textures/color6.png",
    "textures/color7.png",
    "textures/color8.png",
    "textures/color9.png",
    "textures/crosshair.png",
    "textures/dirt.png",
    "textures/glass.png",
    "textures/gold.png",
    "textures/grass.png",
    "textures/grass_dirt.png",
    "textures/gravel.png",
    "textures/hotbar_bg.png",
    "textures/hotbar_selection.png",
    "textures/lava.png",
    "textures/leaves_opaque.png",
    "textures/red_flower.png",
    "textures/red_mushroom.png",
    "textures/rock.png",
    "textures/rock_bronze.png",
    "textures/rock_coal.png",
    "textures/rock_gold.png",
    "textures/sand.png",
    "textures/sponge.png",
    "textures/stone.png",
    "textures/tree_side.png",
    "textures/tree_top.png",
    "textures/water.png",
    "textures/wood.png",
    "textures/yellow_flower.png",
    "textures/previews/11.png",
    "textures/previews/12.png",
    "textures/previews/13.png",
    "textures/previews/14.png",
    "textures/previews/15.png",
    "textures/previews/16.png",
    "textures/previews/2.png",
    "textures/previews/21.png",
    "textures/previews/22.png",
    "textures/previews/23.png",
    "textures/previews/24.png",
    "textures/previews/25.png",
    "textures/previews/26.png",
    "textures/previews/27.png",
    "textures/previews/28.png",
    "textures/previews/29.png",
    "textures/previews/3.png",
    "textures/previews/30.png",
    "textures/previews/31.png",
    "textures/previews/32.png",
    "textures/previews/33.png",
    "textures/previews/34.png",
    "textures/previews/35.png",
    "textures/previews/36.png",
    "textures/previews/37.png",
    "textures/previews/38.png",
    "textures/previews/39.png",
    "textures/previews/4.png",
    "textures/previews/5.png",
    "textures/previews/6.png",
    "textures/previews/8.png",
    "textures/previews/9.png",
    "js/RandomLevelWorker.js",
    "textures/steveleg.png",
    "textures/stevehead.png",
    "textures/stevetorso.png",
    "textures/stevearm.png"
]

code = '''import http.server
import socketserver
import webbrowser

webbrowser.open(f'http://localhost:8080')

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", 8080), Handler) as httpd:
    httpd.serve_forever()
'''

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

print("Minecraft Classic Dumper\nBy: Instel\n")

print("\033[33mThis program just came out, expect some issues.\033[0m\n")

print("\033[31m" + "="*60 + "\033[0m")
print("\033[31mREAD ME PLEASE!\033[0m")
print("\033[31mDo NOT distribute your dump of the game; this may cause legal issues due to distributing copyrighted content.")
print("You may distribute this dumper only if you do NOT tamper with the code.")
print("To edit the code and distribute it, please fork this project on GitHub.\033[0m")
print("\033[31m" + "="*60 + "\033[0m\n")

print('\033[32mIf you agree, type "I agree"\033[0m')
if (input().lower() == "i agree"):
    clear()
    print("Thank you for your interest in Minecraft Classic Dumper!\n")
    
    with open("index.html", 'w') as f:
        f.write(index)
    print("Generated index.html in the current directory.")

    print("Would you like to generate the host file to host this dump? (y/n)")

    if (input().lower() == "y"):
        print("Generating the host.py file...")
        with open('host.py', 'w') as file:
            file.write(code)
        print("Done making host file!")
    else:
        print("Skipping host.py...")

    print("\nMaking dirs...")
    for directory in dirs:
        dir_path = os.path.join(root_assets_dir, directory)
        os.makedirs(dir_path, exist_ok=True)
        print(f"Made the {dir_path} directory.")
    
    print("\nDownloading files...")
    for item in downloads:
        url = f'https://classic.minecraft.net/assets/{item}'
        
        local_path = os.path.join(root_assets_dir, item)
        
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        
        response = requests.get(url)

        if response.status_code == 200:
            with open(local_path, 'wb') as file:
                file.write(response.content)
            print(f'Downloaded {item} to {local_path}')
        else:
            print(f"Failed to download {item}. Status code: {response.status_code}")
    
    input("Press enter to exit.")
else:
    clear()
    print("Thank you for your interest in Minecraft Classic Dumper!\n")
    print("\033[32mIf you change your mind later and do agree to the terms, you may relaunch the program\033[0m\n")
    input("\033[31mPress enter to exit.\033[0m")