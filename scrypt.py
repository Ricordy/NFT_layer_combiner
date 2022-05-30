from PIL import Image

group1 = [
    r"src_files/backgound/1.png",
    r"src_files/backgound/2.png",
    r"src_files/backgound/3.png"
]
group2 = [
    r"src_files/characters/1.png",
    r"src_files/characters/2.png",
    r"src_files/characters/3.png",
    r"src_files/characters/4.png"
]
group3 = [
    r"src_files/hats/1.png",
    r"src_files/hats/2.png",
    r"src_files/hats/3.png"
]
counter = 0

def createImage(a,b,c,counter):
    first = group1[a]
    second = group2[b]
    third = group3[c]

    print("Vamos no A:", c ,  "B: " , b, "C: " , c, ". Total já craciado:" ,counter )


    image01 = Image.open(first).convert("RGBA")
    image02 = Image.open(second).convert("RGBA")
    image03 = Image.open(third).convert("RGBA")



    image01 = image01.resize((1000,1000))
    image02 = image02.resize((1000,1000))
    image03 = image03.resize((1000,1000))



    intermediate = Image.alpha_composite(image01, image02)
    intermediate2 = Image.alpha_composite(intermediate,image03)






    name = "saved_files/" + str(counter) + ".png"
    intermediate2.save(name)


for a in range(3):
    for b in range(4):
        for c in range(3):
            createImage(a,b,c,counter)
            counter += 1

