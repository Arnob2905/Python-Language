import uuid

def generate_uuid1():
   
    try:
        return uuid.uuid1()
    except Exception as e:
        return f"Error generating UUID1: {e}"

def generate_uuid4():
  
    return uuid.uuid4()