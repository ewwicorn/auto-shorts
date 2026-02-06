if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    from src.auto_shorts.project import Project
    
    load_dotenv()
    
    proxy = os.getenv("HTTP_PROXY")
    
    project = Project("test2", path=r'C:\Users\eWwic0rn\Documents\projects\python\auto-shorts\sources\evelone.mp4')
    
    #project.get(proxy=proxy, cookies=r'C:\Users\eWwic0rn\Documents\projects\python\auto-shorts\cookies\www.youtube.com_cookies.txt')
    project.transcribe()
    #project.h_to_v_with_subtitles()
    
 