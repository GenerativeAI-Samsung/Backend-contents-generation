import replicate
import os
os.environ['REPLICATE_API_TOKEN'] = 'r8_UQIrfPj3KuUBklcProhoTkVzlQmKggD0itmUp'
# REPLICATE_API_TOKEN=r"r8_UQIrfPj3KuUBklcProhoTkVzlQmKggD0itmUp"
output = replicate.run(
r"methexis-inc/img2prompt:50adaf2d3ad20a6f911a8a9e3ccf777b263b8596fbd2c8fc26e8888f8a0edbb5",
input={"image": open(r"output/horse-png-27.png", "rb")}
)
print(output)