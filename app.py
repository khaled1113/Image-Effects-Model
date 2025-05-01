import gradio as gr
import numpy as np
import cv2

def apply_normal_blur(image):
    kernel_size = (7, 7)
    kernel = np.ones(kernel_size, np.float32) / (kernel_size[0] * kernel_size[1])
    blurred_image = cv2.filter2D(image, -1, kernel)
    return blurred_image

interface = gr.Interface(
    fn=apply_normal_blur,
    inputs=gr.Image(type="numpy"),
    outputs=gr.Image(type="numpy"),
    title="Apply 7x7 Blur Filter",
    description="Upload an image and apply a 7x7 averaging blur."
)

interface.launch()
