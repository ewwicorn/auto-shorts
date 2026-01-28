def create_new_project(project_name):
    import os
    os.chdir('projects')
    if not os.path.exists(project_name):
        project_path = os.path.join(os.getcwd(), project_name)
        result_path = os.path.join(project_path, "results")
        temp_path = os.path.join(project_path, "temp")
        try:
            os.makedirs(project_path)
            os.makedirs(result_path)
            os.makedirs(temp_path)

            print(f"Project '{project_name}' created at {project_path}")
        except FileExistsError:
            print(f"Project '{project_name}' already exists at {project_path}")
        
        return project_path
    else:
        print(f"Project '{project_name}' already exists.")
        return os.path.join(os.getcwd(), project_name)


if __name__ == "__main__":
    from src.auto_shorts.transcript import transcribe_audio
    from src.auto_shorts.video_edit import combine_video
    project = create_new_project(input("Enter project name: "))
    video_path=r'C:\Users\eWwic0rn\Documents\projects\python\auto-shorts\sources\evelone.mp4'
    transcription = transcribe_audio(video_path, project)
    video = combine_video(project, transcription, video_path)
 