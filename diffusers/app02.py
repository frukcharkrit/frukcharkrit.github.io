from diffusers import DiffusionPipeline as dp
from PIL import Image, ImageDraw, ImageFont
import torch

def text_to_image(text, diffuser_model):
    #diffuser = diffusers.load_diffuser(diffuser_model)
    #image_data = diffuser.generate(text)
    #image = Image.fromarray(image_data)
    #image.show()
    df = dp.from_pretrained("runwaym1/stable-diffusion-v1-5", torch_dtype=torch.float16)
    image_data = dp(text).images[0]
    image = Image.fromarray(image_data)
    image.show()

#if __name__ == "__main__"
#input_text = "Hello World!"
#diffuser_model = "example_diffuser_model"
#text_to_image(input_text, diffuser_model)
