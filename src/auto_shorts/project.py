from src.auto_shorts.transcript import transcribe_audio
from src.auto_shorts.video_edit import combine_video
from src.auto_shorts.download import download_video
class Project:
    def __init__(self, project_name, link=None, path=None):
        import os
        os.chdir('projects')
        
        #if os.path.isdir(project_name):
         #   raise ValueError(f"Project {project_name} already exists, use another name!")
        
        
        self.project_path = os.path.join(os.getcwd(), project_name)
        self.result_path = os.path.join(self.project_path, "results")
        self.temp_path = os.path.join(self.project_path, "temp")
        self.sources_path = os.path.join(self.project_path, "sources")
        
        self.link = link
        self.video = path
        
        dirs = ["","results","temp","sources"]
        for dir in dirs:    
            os.makedirs(os.path.join(self.project_path, dir), exist_ok=True)
            
        print(f"Project '{project_name}' created at {self.project_path}")
        
    def get(self, proxy=None, cookies=None):
        self.video = download_video(self.link, self.sources_path, proxy, cookies)
        return self.video
    
    def transcribe(self):
        self.subtitles, self.transcription = transcribe_audio(self.video, self.project_path)
        return self.subtitles, self.transcription
        
    def h_to_v_with_subtitles(self):
        final_video = combine_video(self.project_path, self.subtitles, self.video)
        return final_video
        

