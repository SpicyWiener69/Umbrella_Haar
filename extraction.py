from pycocotools.coco import COCO
import os

ann_file = 'instances_val2017.json'
img_dir = 'val2017'
output_list = 'neg_filtered.txt'
limit = 300

coco = COCO(ann_file)

# IDs
umbrella_cat_id = coco.getCatIds(catNms=['umbrella'])[0]
floor_proxy_cat_ids = coco.getCatIds(catNms=['toilet', 'dining table', 'chair'])  # expand as needed

# Get image IDs with umbrellas (to exclude)
umbrella_img_ids = set(coco.getImgIds(catIds=[umbrella_cat_id]))

# Get image IDs with floor-related proxies (to include)
floor_proxy_img_ids = set()
for cid in floor_proxy_cat_ids:
    floor_proxy_img_ids.update(coco.getImgIds(catIds=[cid]))

# Final set = has "floor-like" + does NOT have umbrella
neg_img_ids = sorted(floor_proxy_img_ids - umbrella_img_ids)

# Write result
with open(output_list, 'w') as f:
    for count, img_id in enumerate(neg_img_ids):
        if count >= limit:
            break
        img_info = coco.loadImgs(img_id)[0]
        img_path = os.path.join(img_dir, img_info['file_name'])
        f.write(img_path + '\n')