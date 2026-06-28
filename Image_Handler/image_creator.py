from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def create_task_entry(text):
    width, height = 512, 256
    img = Image.new('L', (width, height), "white")
    pixels = img.load()
    line_thickness = 16
    for i in range(64, 192):
        for j in range(64, 192):
            if (i - 64 < line_thickness or i + line_thickness > 192):
                pixels[i,j] = 0
            if (j - 64 < line_thickness or j + line_thickness > 192):
                pixels[i,j] = 0
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 16)
    draw.text((256, 128), text, 0, font=font)
    return img

def create_task_list_img(list):
    task_img_list = []
    for x in list:
        task_img = create_task_entry(x)
        task_img_list.append(task_img)
    
    #imgs = [Image.open(i) for i in task_img_list]
    imgs = task_img_list
    height = len(task_img_list) * 256
    img_merge = Image.new(imgs[0].mode, (512, height))
    y = 0
    for img in imgs:
        img_merge.paste(img, (0,y))
        y+= img.height
    img_merge.save("./taskList.png")

create_task_list_img(["Task 1", "Task 2"])
#img.show()
