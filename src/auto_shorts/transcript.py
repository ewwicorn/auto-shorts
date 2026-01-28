import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logging.getLogger("faster_whisper").setLevel(logging.DEBUG)

def format_timestamp(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    milliseconds = int((seconds - int(seconds)) * 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{milliseconds:03d}"

def transcribe_audio(video_path, project_path):
    import os
    import pysubs2
    
    os.chdir(project_path+'/temp')
    
    subtitles_file=os.path.join(os.path.basename(project_path))+".ass"
    transcription_file=os.path.join(os.path.basename(project_path))+".txt"

    if os.path.exists(transcription_file) and os.path.exists(subtitles_file):
        print("Video is already transcripted.")
        return subtitles_file, transcription_file
    
    from faster_whisper import WhisperModel 
    from auto_shorts.video_edit import extract_audio

    model = WhisperModel("small", device="cpu", compute_type="int8", cpu_threads=16)
    segments, info = model.transcribe(extract_audio(video_path, project_path), beam_size=5, language="ru", word_timestamps=True)
    
    with open(transcription_file, "w", encoding='utf-8') as f:
        pass
    
    list_for_subs = []
    
    for segment in segments:
        for word in segment.words:
            dict_for_subs = {'start': word.start, 'end': word.end, 'text': word.word}
            list_for_subs.append(dict_for_subs)
            with open(transcription_file, "a", encoding='utf-8') as f:
                f.write("%s %s" % (format_timestamp(word.start), format_timestamp(word.end))+" "+word.word[1:]+"\n")
    
    subs = pysubs2.load_from_whisper(list_for_subs)
    subs.save(subtitles_file)
    
    return subtitles_file, transcription_file
