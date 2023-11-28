import numpy as np
import pandas as pd

objects = {
            0: 'person', 1: 'bicycle', 2: 'car', 3: 'motorcycle', 4: 'airplane', 5: 'bus', 6: 'train', 7: 'truck', 8: 'boat',
            9: 'traffic light', 10: 'fire hydrant', 11: 'stop sign', 12: 'parking meter', 13: 'bench', 14: 'bird', 15: 'cat',
            16: 'dog', 17: 'horse', 18: 'sheep', 19: 'cow', 20: 'elephant', 21: 'bear', 22: 'zebra', 23: 'giraffe', 24: 'backpack',
            25: 'umbrella', 26: 'handbag', 27: 'tie', 28: 'suitcase', 29: 'frisbee', 30: 'skis', 31: 'snowboard', 32: 'sports ball', 
            33: 'kite', 34: 'baseball bat', 35: 'baseball glove', 36: 'skateboard', 37: 'surfboard', 38: 'tennis racket', 39: 'bottle', 
            40: 'wine glass', 41: 'cup', 42: 'fork', 43: 'knife', 44: 'spoon', 45: 'bowl', 46: 'banana', 47: 'apple', 48: 'sandwich', 
            49: 'orange', 50: 'broccoli', 51: 'carrot', 52: 'hot dog', 53: 'pizza', 54: 'donut', 55: 'cake', 56: 'chair', 57: 'couch', 
            58: 'potted plant', 59: 'bed', 60: 'dining table', 61: 'toilet', 62: 'tv', 63: 'laptop', 64: 'mouse', 65: 'remote', 66: 'keyboard', 
            67: 'cell phone', 68: 'microwave', 69: 'oven', 70: 'toaster', 71: 'sink', 72: 'refrigerator', 73: 'book', 74: 'clock', 75: 'vase', 
            76: 'scissors', 77: 'teddy bear', 78: 'hair drier', 79: 'toothbrush'
        }

object_sortkey = ['bottle','cup','mouse','cell phone','book','scissors']

def convert_to_df(results)->pd.DataFrame:
    """
    A helper function for extracting confidence and bounding box information
    from detected objects.

    Args:
        results (list): output from running YOLO model on a video frame
    
    Returns:
        df (pd.Dataframe): object name, bbox coords, and confidence level organized into a dataframe format
    """

    bounding_box = results[0].boxes
    box_xyxy = bounding_box.xyxy.cpu().numpy()
    box_conf = bounding_box.conf.cpu().numpy()
    obj_ids = bounding_box.cls.cpu().numpy()
    box_name = []
    for id in obj_ids:
        box_name.append(objects[id])
    box_name = sorted(box_name, key = lambda x: object_sortkey.index(x))
    
    print(type(box_name))
    print(type(box_xyxy))
    print(type(box_conf))
    df = pd.DataFrame({
        'name': box_name,
        'bbox':box_xyxy.tolist(),
        'conf':box_conf.tolist()
        })
    df_filtered  = df[df['conf'] > 0.5]
    return df_filtered

def get_obj_from_df(data: pd.DataFrame, name: str):
    bboxes = []
    confs = []
    objs = data[data['name'] == name]

    for _,rows in objs.iterrows():
        bboxes.append(rows.bbox)
        confs.append(rows.conf)

    conf_box = np.array([[int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3]),confs[i]] for i,bbox in enumerate(bboxes)])

    return conf_box

def sort_obj(data: pd.DataFrame):
    pass



# TODO object retrieval
def find_obj(name: str):
    """
    Given the object's name, return the location of the closest object of that type.

    Args:
        name (str): name of object
    
    Returns:
        xy (tuple): x and y coordinates of the center of object's bounding box
    """
    pass



# TODO using april tags to identify & move towards loading area
def loading_bay():
    pass