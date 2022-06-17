import io
import os
import ssl

import torch
import torchvision
from PIL import Image
from torchvision.transforms import transforms

ssl._create_default_https_context = ssl._create_unverified_context

IMAGE_PREPROCESS = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225]),
])
MODEL_ARCHITECTURE = "resnet18", "resnet34", "resnet50", "resnet101", "resnet152"  # one by each

MODEL: torchvision.models.resnet.ResNet = torch.hub.load('pytorch/vision:v0.6.0',
                                                         os.getenv('ARCHITECTURE'),
                                                         pretrained=True)


def torch_image(img):
    # FILE_FIELD_NAME = 'file'
    image = Image.open(io.BytesIO(img))
    input_tensor = IMAGE_PREPROCESS(image)
    input_batch = input_tensor.unsqueeze(0)

    with torch.no_grad():
        output = MODEL(input_batch)

    result = torch.nn.functional.softmax(output[0],
                                         dim=0).tolist()  # needed result
    return result.index(max(result))
