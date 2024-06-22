import tkinter as tk
from tkinter import simpledialog, messagebox, IntVar
from tkinter.ttk import Label, Button, Radiobutton
from pytube import YouTube

def download_video():
    
    ROOT.withdraw()

    user_input = simpledialog.askstring(title="YouTube Downloader", prompt="Enter Link:")

    if not user_input:
        messagebox.showerror("Error", "No link provided!")
        return

    SAVE_PATH = "C:/YouTube Downloader"
    link = user_input

    try:
        yt = YouTube(link)
    except:
        messagebox.showerror("Error", "Connection Error")
        return

    try:
        if download_option.get() == 1:
            mp4_streams = yt.streams.filter(file_extension='mp4').all()
            d_video = mp4_streams[-1]
            d_video.download(output_path=SAVE_PATH)
            messagebox.showinfo("Success", "Video Downloaded successfully! File created in C: drive named 'YouTube Downloader'.")
        elif download_option.get() == 2:
            audio_stream = yt.streams.filter(only_audio=True).first()
            audio_stream.download(output_path=SAVE_PATH)
            messagebox.showinfo("Success", "Audio Downloaded successfully! File created in C: drive named 'YouTube Downloader'.")
        else:
            messagebox.showerror("Error", "Please select an option!")

        choice = messagebox.askyesno("Continue?", "Do you want to download another video?")
        if choice:
            ROOT.deiconify()
        else:
            ROOT.destroy()

    except Exception as e:
        messagebox.showerror("Error", f"Some error occurred: {e}")

ROOT = tk.Tk()
ROOT.title("YouTube Downloader")

label = Label(ROOT, text="Click the button to download a YouTube video or audio")
label.pack(pady=10)

download_option = IntVar()

video_radio = Radiobutton(ROOT, text="Download Video (MP4)", variable=download_option, value=1)
video_radio.pack(anchor=tk.W)

audio_radio = Radiobutton(ROOT, text="Download Audio (MP3)", variable=download_option, value=2)
audio_radio.pack(anchor=tk.W)

download_button = Button(ROOT, text="Download", command=download_video)
download_button.pack(pady=10)

ROOT.mainloop()
