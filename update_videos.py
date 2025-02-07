import tkinter as tk
import video_library as lib


class UpdateVideos:
    def __init__(self, main_window):
        self.main_window = main_window
        main_window.geometry("300x250")
        main_window.title("Update Video Rating")
 
        input_label = tk.Label(main_window, text="Enter Video Number")
        input_label.grid(row=0, column=0, padx=10, pady=20)
 
        self.video_number_entry = tk.Entry(main_window, width=10,)
        self.video_number_entry.grid(row=0, column=1, padx=10, pady=20)
 
        input_rating_label = tk.Label(main_window, text="Enter New Rating")
        input_rating_label.grid(row=1, column=0, padx=10, pady=20)
 
        self.new_rating_entry = tk.Entry(main_window, width=10)
        self.new_rating_entry.grid(row=1, column=1, padx=10, pady=10)
        
        update_button = tk.Button(main_window, text="Update Rating", command=self.modify_rating)
        update_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
 
        self.message_label = tk.Label(main_window, text=" ", font=("Helvetica", 10))
        self.message_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
 
    def modify_rating(self):
        video_number = self.video_number_entry.get()
        rating_value = self.new_rating_entry.get()
        try:
            rating_value = int(rating_value)
        except ValueError:
            self.message_label.configure(text="The rating number must be interger!")
            return
        
        if rating_value > 5:
            self.message_label.configure(text="The rating number must be between 1 and 5!")
            return
 
        if lib.update_rating(video_number, rating_value):
            video_name = lib.get_name(video_number)
            views_count = lib.get_play_count(video_number)
            self.message_label.configure(text=f"'{video_name}' rating is now: {rating_value}, Play count: {views_count}")
        else:
            self.message_label.configure(text="Video number is wrong or does not exist. Please Try Again!")

if __name__ == "__main__":
    main_window = tk.Tk()
    application = UpdateVideos(main_window)
    main_window.mainloop()