import dlib   # to detect face 
import face_recognition_models
from sklearn.svm import SVC 
import streamlit as st
from PIL import Image 
import numpy as np 

from src.database.db import get_all_students    # getting all teh sutuednts from the db and trainin model on that 




photo_source = st.camera_input("position face in center") 
if photo_source: 
    np.array(Image.open(photo_source))   # using pillow library to deal with our photo image.open is there fucino of pilow 


# dlib provides 3 types of modules : 
# 1. to make bounding box overface 
# 2. shape predictor (sp) -- it detects landmark of face (face points) there are 68 landmarks 
# 3.face recognizer 



# Streamlit scripts re-run top-to-bottom on every user interaction (a button click, a slider move).
# Caching prevents reloading heavyweight model weights into RAM on every single run.
@st.cache_resource

def load_dlib_models(): # its heavy model hence chache resource ie. only one time load in system not everytime we rerurn 

    detector = dlib.get_frontal_face_detector()   # here dlib gives us facedetector which detects boxes ie how many faces there are in image
                                
    sp = dlib.shape_predictor(face_recognition_models.pose_predictor_model_location() ) # this model pose~~~ gives location of our landmark
    # What it does: Takes the full image AND the bounding box from Step 1, then outputs 68 specific 2D coordinates $(x, y)$ 
    # corresponding to facial landmarks (eyes, nose bridge, jawline, lips).


    facerec = dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location()
    )
                              
    return detector, sp, facerec 
# we hvae used face_reicniton_models.~~~  cuause they are advanced models dlib can do shit but to make it efficient we use htose modles 


# now we will make funtion usign which we can get embeddings of face using numpy array 
def get_face_embeddings(image_np): 
    detector, sp, facerec = load_dlib_models()   # loading this 3 made above 

    faces = detector(image_np, 1)   # detecting faces in image --- parameters 1. image_np (numpy array of image) 2.number of preporcessing on given image to be more accurate only 1 cuase fucks cpu and all 
                
    encodings = []    # will filll embeddings of each face one by one in this    

    for face in faces: 
        shape = sp(image_np, face) # taking landmark of specific face (of each face form faces)  form that image

        face_descriptor = facerec.compute_face_descriptor(image_np, shape, 1) # takes image and landmark of that specific face and preporcessing number and gives 128embedding per face 

        encodings.append(np.array(face_descriptor))   # convering embdding into np.array and then appending to encoidngs 
    return encodings 



@st.cache_resource 
def get_trained_model() : 
    X = []  # embeddings of students in it 
    Y = []  # ids of those students    here 

    student_db = get_all_students() 

    if not student_db: 
        return None 

    for student in student_db: 
        embeddings = student.get("face_embeddings") 
        if embeddings: 
            X.append(np.array(embeddings))
            Y.append(student.get("student_id")) 

    if len(X) == 0 : 
        return 0 
    clf = SVC(kernel = "linear", probability=True, class_weight= "balanced") 

    try: 
        clf.fit(X,Y) 
    except ValueError: 
        pass 
    return {"clf":clf, "X":X, "Y": Y} 


def train_classifier(): 
    st.cache_resource.clear() 
    model_data = get_trained_model() 
    return bool(model_data) 


def predict_attendance(class_image_np): 
    encodings = get_face_embeddings(class_image_np)

    detect_student = {} 

    model_data = get_trained_model() 

    if not model_data: 
        return detect_student, [] , len(encodings) 

    clf = model_data['clf'] 
    x_train = model_data['X'] 
    y_train = model_data['Y'] 

    all_students = sorted(list(set(y_train))) 

    for encoding in encodings: 
        if len(all_students) >= 2: 
            predicted_id = int(clf.predict([encoding][0]))
        else: 
            predicted_id = int(all_students[0]) 

        student_embeddings  = x_train[y_train.index(predicted_id)]  

        best_match_score = np.linalg.norm(student_embeddings - encodings)

        resembelence_threshold = 0.6 

        if best_match_score <= resembelence_threshold: 
            detect_student[predicted_id] = True

    return detect_student, all_students, len(encodings)  
