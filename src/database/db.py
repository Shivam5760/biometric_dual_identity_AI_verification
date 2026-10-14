from src.database.config import supabase 
import bcrypt 

def hash_pass(pwd): 
    return bcrypt.hashpw(pwd.encode(),bcrypt.gensalt()).decode()   # encoee converts text to byte(binary stream) and decode convert that byte to aginathatn thing 

def check_pass(pwd,hashed): 
    return bcrypt.checkpw(pwd.encode(),hashed.encode())

def check_teacher_exists(username): 
    '''check for unique username and returns flasewhen username is already taken '''
    response = supabase.table('teachers').select('username').eq('username',username).execute()
    # goes to teacher table and checks for alll rsername columns and compare with given one if found similar there wil be response 
    return len(response.data) > 0   

def create_teacher(username,name,password):
    data = {"username":username,"name":name,"password":hash_pass(password)} 
    supabase.table("teachers").insert(data).execute() 
    #hasing so that even i cannot see users private data like password 



def teacher_login(username,password): 
    response = supabase.table("teachers").select("*").eq("username",username).execute()

    if response.data : 
        teacher = response.data[0]
        if check_pass(password,teacher["password"]):
            return teacher
    return None

def get_all_students(): 
    response = supabase.table("student").select("*").execute()   # geting whole sutduent table in form of array and returning that 
    return response.data 


def create_student(new_name, face_embedding = None, voice_embedding = None): 
    data = {'name':new_name, 'face_embeddings': face_embedding, 'voice_embeddings': voice_embedding} 

    response = supabase.table('student').insert(data).execute()

    return response.data 

def create_subject(subject_code, name, section, teacher_id):
    data = {"subject_code": subject_code, "name":name, "section":section, "teacher_id": teacher_id}
    response = supabase.table("subjects").insert(data).execute()
    return response.data

def get_teacher_subjects(teacher_id):
    response = supabase.table('subjects').select("*,subjects_students(count), attendance_logs(timestamp)").eq("teacher_id", teacher_id).execute()
    subjects = response.data

    for sub in subjects: 
        sub['total_students'] = sub.get("subjects_student", [{}])[0].get('count', 0) if sub.get('subjects_students') else 0 
        attendance = sub.get('attendance_logs',[])
        unique_sessions = len(set(log['timestamp'] for log in attendance)) 
        sub['total_classes'] = unique_sessions

        sub.pop ('subjects_student', None) 
        sub.pop('attendance_logs', None) 

    return subjects
