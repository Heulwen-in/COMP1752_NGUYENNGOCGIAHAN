import tkinter as tk
import video_library as lib

class CommentVideos:
    def __init__(self, main_window):
        self.main_window = main_window
        main_window.title("Comment on Video")
        
        video_number_label = tk.Label(main_window, text ="Enter Video Number")
        video_number_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.video_number_entry = tk.Entry(main_window, width=10)
        self.video_number_entry.grid(row=0, column= 1, padx=10, pady=10)
        
        self.video_title_label = tk.Label(main_window, text="")
        self.video_title_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        
        comment_label = tk.Label(main_window, text="Enter Comment")
        comment_label.grid(row=2, column=1, padx=10, pady=10)
        
        self.comment_entry = tk.Entry(main_window, width=40)
        self.comment_entry.grid(row=2, column=1, padx=10, pady=10)
        
        post_button = tk.Button(main_window, text="Post Comment", command=self.post_comment)
        post_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        
        self.status_label = tk.Label(main_window, text="", font=("Helvetica", 10))
        self.status_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        
    def post_comment(self):
        video_number = self.video_number_entry.get()
        comment = self.comment_entry.get()
        
        if lib.video_exists(video_number):
            video_title = lib.get_name(video_number)
            self.video_title_label.configure(text=f"Video Title: {video_title}")
            try:
                if lib.add_comment(video_number, comment):
                    self.status_label.configure(text="Comment posted successfully!")
                else:
                    self.status_label.configure(text="Failed to post comment. Please try again!")
            except Exception as e:
                self.status_label.configure(text=f"An error occurred: {str(e)}")
        else:
            self.status_label.configure(text="Video number is wrong or doesn't exist. Please try again!")

if __name__ == "__main__":
    main_window = tk.Tk()
    application = CommentVideos(main_window)
    main_window.mainloop()     