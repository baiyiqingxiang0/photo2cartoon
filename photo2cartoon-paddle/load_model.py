import numpy as np
import paddle
from PIL import Image



def load_model():
    print("Loading model...")
    model = paddle.jit.load("model/photo2cartoon/ugatitmodel_genA2B")
    print("Model loaded.")
    return model


def tensor_to_image(tensor):
    # 这里将tensor形式用numpy()函数转为数组形式，
    # 并且用transpose将数组转置为PIL能够处理的WxHxC形式。
    if tensor.dim()==4:
        tensor=tensor.squeeze(0)  ###去掉batch维度
    nimg = tensor.numpy()
    nimg =nimg.transpose(1, 2, 0)
    img = (nimg+1)/2*255
    img = Image.fromarray(np.uint8(img))  # eg1
    return img

def image_to_tensor(image):
    img = image.resize((128,128),Image.ANTIALIAS)
    img = np.array(img).transpose(2, 0, 1)
    img = img.reshape((1,3,128,128))
    img = paddle.to_tensor(img/127.5-1.,'float32')

    return img

def predict_img(model, input_img):
    # inference
    model.eval()
    x = image_to_tensor(input_img)
    pred,_,_ = model(x)
    img = tensor_to_image(pred)
    return img

