def extract_audio(video_path, project_path):
    import os
    import ffmpeg
    os.chdir(project_path+'/temp')
    audio_file=os.path.join(os.path.basename(project_path))+".mp3"
    ffmpeg.input(video_path).output(audio_file, format='mp3', acodec='libmp3lame').run()
    return audio_file

    
def subtitles_style(subtitles_path):
    import pysubs2
    
    subs = pysubs2.load(subtitles_path)
    subs_style = subs.styles["Default"]
    subs_style.alignment = 2
    subs_style.fontsize = 100
    subs_style.bold = True
    subs_style.borderstyle = 1
    subs_style.fontname = "Tovari Sans"
    subs_style.marginv = "400"
    subs_style.outline = 3
    subs_style.outlinecolor = pysubs2.Color(r=0,g=0,b=0,a=0)
    subs_style.primarycolor = pysubs2.Color(r=255,g=255,b=0,a=0)
    subs.info["PlayResX"] = 1080
    subs.info["PlayResY"] = 1920
    subs.styles["Default"] = subs_style
    subs.save(subtitles_path)
    
    
def combine_video(project_path, subtitles_path, video_path):
    import os
    subtitles_style(subtitles_path)
    os.chdir(project_path+'/temp')
    video_file=os.path.join(os.path.basename(project_path))+".mp4"
    
    if os.path.exists(video_file):
        print("Video is already combined.")
        return video_file
    
    import ffmpeg
    input_stream = ffmpeg.input(video_path)
    v = input_stream.video
    a = input_stream.audio
    (
        v
        .filter("scale", w=1080, h=1920, force_original_aspect_ratio="decrease")
        .filter("pad", w=1080, h=1920, x="(ow-iw)/2", y="(oh-ih)/2")
        .filter("setsar", 1)
        .filter('subtitles', filename=subtitles_path)
        .output(
            a,
            video_file, 
            vcodec="h264_amf", 
            acodec="aac", 
            pix_fmt="yuv420p",
            **{
            "quality": "speed",
            "rc": "cqp",
            "qp_i": 24,
            "qp_p": 24,
            "qp_b": 24,
            "usage": "transcoding",
            "profile": "high"
            }
        )
        .run(overwrite_output=True)
    )

    return video_file
    
    