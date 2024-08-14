import tkinter as tk
import tkinter.scrolledtext as tkst

import video_library as lib
import font_manager as fonts


def set_text(text_area, content):  # Function that adds content to the Text_area
    text_area.delete("1.0", tk.END)  # Delete existing content
    text_area.insert("1.0", content)  # Enter text

def video_exists(video_number):   # Define a function to check if a video exists in the library
    return video_number in lib.library  # Return True if the video number is in the library, False otherwise


class CheckVideos:  # A class to inspect video in the window of the program containing a list of clicked videos
    def __init__(self, window):
        window.geometry("770x500")  # Set the size of the window to accommodate new elements
        window.title("Check Videos")  # Set the window's title

        top_frame = tk.Frame(window)
        top_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")  # Set grid appearance

        list_videos_btn = tk.Button(top_frame, text="List All Videos", command=self.list_videos_clicked)  # Button to list all videos
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10, sticky="ew")  # Set grid appearance

        enter_id_lbl = tk.Label(top_frame, text="Enter Video Number")  # Make a label to instruct users on entering video number
        enter_id_lbl.grid(row=0, column=1, padx=10, pady=10)  # Set grid appearance

        self.input_id_txt = tk.Entry(top_frame, width=5)  # The area where users can input the video number
        self.input_id_txt.grid(row=0, column=2, padx=10, pady=10)  # Set grid appearance

        check_video_btn = tk.Button(top_frame, text="Check Video", command=self.check_video_clicked)  # Create a button labeled "Check Video", and upon clicking it, the check_video_clicked method is called
        check_video_btn.grid(row=0, column=3, padx=10, pady=10, sticky="ew")  # Set grid appearance
        
        middle_frame = tk.Frame(window)  # Create middle frame
        middle_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")  # Set grid appearance

        self.list_txt = tkst.ScrolledText(middle_frame, width=38, height=10, wrap="none")  # Make a text area which can be scrolled up and down
        self.list_txt.grid(row=0, column=0, columnspan=3, sticky="ew", padx=10, pady=10)  # Set grid appearance

        self.video_txt = tk.Text(middle_frame, width=30, height=10, wrap="none")  # Make a window that shows text in video format
        self.video_txt.grid(row=0, column=3, sticky="ew", padx=10, pady=10)  # Set grid appearance

        bottom_frame = tk.Frame(window)  # Create bottom frame
        bottom_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")  # Set grid appearance

        self.status_lbl = tk.Label(bottom_frame, text="", font=("Helvetica", 10))  # View the status of the video
        self.status_lbl.grid(row=0, column=0, columnspan=4, sticky="w", padx=10, pady=10)  # Set grid appearance
        
    def check_video_clicked(self):  # A procedure for handling checking videos
        key = self.input_id_txt.get()  # Obtain the entered video number from the input
        if not key:   # Check if the input field is empty
            set_text(self.video_txt, "Please enter a video number") # If empty, display an error message in the text area
            self.status_lbl.configure(text="Check Video button was clicked!") # Update the status label
            return # Exit the function early
        
        if not video_exists(key): # Check if the video exists in the library
            set_text(self.video_txt, f"Video {key} does not exist") # If the video does not exist, display an error message in the text area
            return # Exit the function early

        video_details = "" # Initialize an empty string to store video details
        try:  # Retrieve the video details from the library
            name = lib.get_name(key) # Get the video name
            director = lib.get_director(key) # Get the video director
            rating = lib.get_rating(key) # Get the video rating
            play_count = lib.get_play_count(key)  # Get the video play count
            comments = lib.get_comments (key) # Get the video comments

            video_details = f"Video name: {name}\nDirector name: {director}\nRating: {rating}\nPlay count: {play_count}\nComment:\n"  # Create a string to display the video details
            if comments is not None: # Check if there are any comments
                for comment in comments: # Iterate over each comment
                    video_details += f"- {comment}\n" # Add each comment to the video details string
            else:
                video_details += "No comments\n" # If there are no comments, add a message indicating that 
                
            set_text(self.video_txt, video_details) # Display the video details
        except Exception as e:
            set_text(self.video_txt, f"An error occurred: {str(e)}")  # If an error occurs, display an error message in the text area
        self.status_lbl.configure(text="Check Video button was clicked!") # Update the status label to indicate that the "Check Video" button was clicked

    def list_videos_clicked(self):  # A procedure for handling listing videos
        video_list = lib.list_all()  # Obtain a list of all videos from lib
        set_text(self.list_txt, video_list)  # Display the list of videos
        self.status_lbl.configure(text="List Videos button was clicked!")  # Update the status

if __name__ == "__main__":
    window = tk.Tk()  # Create a TK object
    fonts.configure()  # Configure the fonts
    CheckVideos(window)  # Open the CheckVideo GUI
    window.mainloop()  # Run the window main loop, reacting to button presses, etc