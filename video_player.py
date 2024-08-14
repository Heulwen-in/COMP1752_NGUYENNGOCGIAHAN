import tkinter as tk
import time
import random
 
import font_manager as fonts
from check_videos import CheckVideos
from create_video_list import CreateVideoList
from update_videos import UpdateVideos
from check_image_videos import CheckImageVideos
from comment_videos import CommentVideos
 
def check_videos():
    status_label.configure(text="Check Videos button was clicked!")
    CheckVideos(tk.Toplevel(main_window))
 
def create_video_list():
    status_label.configure(text="Create Video List button was clicked!")
    CreateVideoList(tk.Toplevel(main_window))
 
def update_videos():
    status_label.configure(text="Update Videos button was clicked!")
    UpdateVideos(tk.Toplevel(main_window))

def check_image_videos():
    status_label.configure(text="Check Image Video button was clicked!")
    CheckImageVideos(tk.Toplevel(main_window))
    
def comment_videos():
    status_label.configure(text="Comment on Video button was clicked!")
    CommentVideos(tk.Toplevel(main_window))
    
def submit_customer_name():
    customer_name = customer_name_entry.get()
    if customer_name == "":
        status_label.configure(text="You need to write your name!")
    else:
        status_label.configure(text=f"Welcome {customer_name}!")
        check_videos_button.config(state="normal")
        create_video_list_button.config(state="normal")
        update_videos_button.config(state="normal")
        check_image_videos_button.config(state="normal")
        comment_videos_button.config(state="normal")
        
def update_time():
    current_time = time.strftime("%H:%M:%S")
    time_label.config(text=current_time)
    main_window.after(1000, update_time)
    
def change_theme():
    color = '#{:06x}'.format(random.randint(0, 0xFFFFFF))
    main_window.configure(bg=color)
    header_label.config(bg=color)
    customer_name_label.config(bg=color)
    status_label.config(bg=color)
    time_label.config(bg=color)

main_window = tk.Tk()
main_window.geometry("700x300")
main_window.title("Video Player")
 
fonts.configure()
 
header_label = tk.Label(main_window, text="Hello, you need to write your name before clicking one of the buttons below")
header_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
 
check_videos_button = tk.Button(main_window, text="Check Videos", command=check_videos, state="disabled")
check_videos_button.grid(row=1, column=0, padx=10, pady=10)
 
create_video_list_button = tk.Button(main_window, text="Create Video List", command=create_video_list, state="disabled")
create_video_list_button.grid(row=1, column=1, padx=10, pady=10)
 
update_videos_button = tk.Button(main_window, text="Update Videos", command=update_videos, state="disabled")
update_videos_button.grid(row=1, column=2, padx=10, pady=10)

check_image_videos_button = tk.Button(main_window, text="Check Image Video", command=check_image_videos, state="disabled")
check_image_videos_button.grid(row=2, column=0, padx=10, pady=10)

comment_videos_button = tk.Button(main_window, text="Comment on Video", command=comment_videos, state="disabled")
comment_videos_button.grid(row=2, column=1, padx=10, pady=10)

customer_name_label = tk.Label(main_window, text="Your Name:")
customer_name_label.grid(row=3, column=0, padx=5, pady=5)

customer_name_entry = tk.Entry(main_window, width=15)
customer_name_entry.grid(row=3, column=1, padx=10, pady=10)

enter_button = tk.Button(main_window, text="Enter", command=submit_customer_name)
enter_button.grid(row=3, column=2, padx=5, pady=5)

theme_button = tk.Button(main_window, text="Change Theme", command=change_theme)
theme_button.grid(row=4, column=2, padx=5, pady=5)

status_label = tk.Label(main_window, text="", font=("Helvetica", 10))
status_label.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

time_label = tk.Label(main_window, text="", font=("Helvetica", 10))
time_label.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

update_time()
 
main_window.mainloop()
