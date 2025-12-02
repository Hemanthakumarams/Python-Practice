def read_file(file_path):
    file_handle = None
    try:
        file_handle = open(file_path)
        content = file_handle.read()
        print(content)
    
    except FileNotFoundError:
        print("Error: The file doesnot exist")

    except PermissionError:
        print("Error: Yoy doen't have permission to access this file")

    finally:
        print("Clean-Up in Progress")
        try:
            if file_handle is not None:
                file_handle.close()
                print("File is closed")
        except Exception:
            pass

read_file("my_notes.txt")


def check_age(age):
    if (age<18):
        raise ValueError("Age is less than allowed limit")
    
    print("Eligible for voting")

def chech_eligibility_for_voting():
    try:
        check_age(15)
        # check_address(address)
        # check_citizenship(document)
        
    except ValueError as e:
        print("Error:",e)

chech_eligibility_for_voting()