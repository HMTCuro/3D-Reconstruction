import torch
import encoding
import cv2 as cv

# Get the model
# model = encoding.models.get_model('Encnet_ResNet50s_PContext', pretrained=True).cuda()
# model = encoding.models.get_model('FCN_ResNeSt50_PContext', pretrained=True).cuda()
model = encoding.models.get_model('DeepLab_ResNeSt269_PContext', pretrained=True).cuda()
model.eval()

def process_name(index):
    if index <10:
        res="0000000"+str(index)
    elif index>=10 and index <100:
        res="000000"+str(index)
    elif index>=100 and index <1000:
        res="00000"+str(index)
    return res

# Prepare the image
#url = 'https://github.com/zhanghang1989/image-data/blob/master/encoding/segmentation/pcontext/2010_001829_org.jpg?raw=true'
# filename = '../../example.jpg'
# filename = 'img/IMG_0594.JPG'

for i in range(434):
    print(process_name(i))
#     img_dir="resized_images/"+process_name(i)+".jpg"
    img_dir="resized_images_dongbeiya/"+process_name(i)+".jpg"
    #img = encoding.utils.load_image(encoding.utils.download(url, filename)).cuda().unsqueeze(0)
    img = encoding.utils.load_image(img_dir).cuda().unsqueeze(0)
        # Make prediction
    output = model.evaluate(img)
    predict = torch.max(output, 1)[1].cpu().numpy() + 1
    
    # Get color pallete for visualization
    mask = encoding.utils.get_mask_pallete(predict, 'pascal_voc')
    mask.save('resized_images/seg_out/out_' + process_name(i) + '.png')
#     print(output.shape)
#     print(predict.shape)
#     print(mask.shape)
    del img, mask, predict, output
