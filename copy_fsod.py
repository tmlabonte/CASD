import os
import shutil
import json

copy_dir = "/mnt/cvgroupsouthcentral/fsod/annotations/voc0/JPEGImages"
os.makedirs(copy_dir, exist_ok=True)

j = json.load(open("/mnt/cvgroupsouthcentral/fsod/annotations/fsod_test.json", "r"))

for img in j["images"][6500:]:
    shutil.copyfile(os.path.join("/mnt/cvgroupsouthcentral/fsod/images", img["file_name"]), os.path.join(copy_dir, f"{img['id']}.jpg"))
