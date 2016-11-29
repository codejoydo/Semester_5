from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
import json
import sys
sys.path.insert(0, '/home/joycode/sem5/tmp_proj/coco-text-master')
import coco_text

data_dir_c = '/home/joycode/sem5/tmp_proj/'
data_type_c = 'train2014'

coco_txt = coco_text.COCO_Text('/home/joycode/sem5/tmp_proj/COCO_Text.json')

annFile='%s/annotations/captions_%s.json'%(data_dir_c,data_type_c)
coco_ms = COCO(annFile)
G_TEXT_CAP = {}
#############################################################################
#############################################################################

# Get all validation Ids from COCO-Text dataset.
im_ids_txt = coco_txt.getImgIds(imgIds=coco_txt.val)

counter_image = 0
counter_word_instances = 0
counter_caption_instances = 0
images_without_text = 0
for i in im_ids_txt:
    counter_image += 1
    words_present = []
    ann_ids_txt = coco_txt.getAnnIds(imgIds = i)
    ann_txt = coco_txt.loadAnns(ann_ids_txt)
    for j in ann_txt:
        try:
            if j['utf8_string'] != '':
                counter_word_instances += 1
                words_present.append(j['utf8_string'])
        except KeyError:
            pass
    captions = []
    ann_ids_coco = coco_ms.getAnnIds(imgIds = i)
    ann_coco = coco_ms.loadAnns(ann_ids_coco)
    for j in ann_coco:
        try:
            if j['caption'] != '':
                counter_caption_instances += 1
                captions.append(str(j['caption']))
        except KeyError:
            pass
    if not words_present:
        images_without_text += 1
    im = coco_ms.loadImgs(i)
    temp_dict = {}
    temp_dict['captions'] = captions
    temp_dict['text'] = words_present
    temp_dict['file_name'] = im[0]['file_name']
    G_TEXT_CAP[i] = temp_dict

with open('data1.json', 'w') as fp:
    json.dump(G_TEXT_CAP, fp)
print "Total number of images : " + str(counter_image)
print "Total number of words : " + str(counter_word_instances)
print "Total number of captions : " + str(counter_caption_instances)
print "Total number of Images without Text : " + str(images_without_text)
