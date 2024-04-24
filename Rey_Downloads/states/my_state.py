import reflex as rx
from os.path import join, basename
from yt_dlp import YoutubeDL

class FormState(rx.State):
    form_data: dict = {}
    
    ver_card:str = "hidden"
    ver_bar:str = "hidden"
    btn_disabled:bool = False
    
    file:str
    thumb:str
    title:str
    url:str
    
    ydl_opts:dict = {
        'format': 'best',
        'outtmpl': join(rx.get_upload_dir(), '%(title)s.%(ext)s'),
    }

    def handle_submit(self, form_data: dict):
        self.btn_disabled = True
        self.form_data = form_data
        self.url = form_data["url"]
        
        with YoutubeDL(self.ydl_opts) as ydl:
            info_dict = ydl.extract_info(self.url, download=False)   
            self.file = ydl.prepare_filename(info_dict)
            self.thumb = info_dict['thumbnail'] 
            self.title = info_dict['title']
            self.ver_card = "visible"
            self.btn_disabled = False
        
        
    def download_video(self):
        print("descargando...", self.file)
        self.ver_bar = "visible"
        with YoutubeDL(self.ydl_opts) as ydl:
            ydl.download(self.url)
            
        return rx.download(rx.get_upload_url( basename(self.file) ))
        