import tkinter as tk
from PIL import Image, ImageTk

class CheckImageVideos:
    def __init__(self, master):
        self.master = master
        self.master.title("Check Image Videos")
        self.master.geometry("500x500")
        
        self.image_label = tk.Label(self.master, text="No image selected")
        self.image_label.pack(padx=10, pady=10)
        
        self.tom_and_jerry_button = tk.Button(self.master, text="Tom and Jerry", command=self.display_tom_and_jerry)
        self.tom_and_jerry_button.pack(padx=5, pady=5)
        
        self.tom_and_jerry_button = tk.Button(self.master, text="Breakfast at Tiffany's", command=self.display_breakfast_at_tiffany)
        self.tom_and_jerry_button.pack(padx=5, pady=5)
        
        self.tom_and_jerry_button = tk.Button(self.master, text="Casablanca", command=self.display_casablanca)
        self.tom_and_jerry_button.pack(padx=5, pady=5)
        
        self.tom_and_jerry_button = tk.Button(self.master, text="The Sound of Music", command=self.display_the_sound_of_music)
        self.tom_and_jerry_button.pack(padx=5, pady=5)
        
        self.tom_and_jerry_button = tk.Button(self.master, text="Gone with the Wind", command=self.display_gone_with_the_wind)
        self.tom_and_jerry_button.pack(padx=5, pady=5)
            
    def display_image(self, image_path, width, height):
        pil_image = Image.open(image_path)
        pil_image = pil_image.resize((width, height))
        tk_image = ImageTk.PhotoImage(pil_image)
        self.image_label.config(image=tk_image)
        self.image_label.image = tk_image
        
    def display_tom_and_jerry(self):
        image_path = "tom_and_jerry.jpg" 
        width = 200
        height = 200
        self.display_image(image_path, width, height)
        
    def display_breakfast_at_tiffany(self):
        image_path = "breakfast_at_tiffany.jpg" 
        width = 200
        height = 200
        self.display_image(image_path, width, height)
        
    def display_casablanca(self):
        image_path = "casablanca.jpg" 
        width = 200
        height = 200
        self.display_image(image_path, width, height)
        
    def display_the_sound_of_music(self):
        image_path = "The_sound_of_music.jpg" 
        width = 200
        height = 200
        self.display_image(image_path, width, height)

    def display_gone_with_the_wind(self):
        image_path = "Gone_with_the_wind.jpg" 
        width = 200
        height = 200
        self.display_image(image_path, width, height)
        
if __name__ == "__main__":
    main_window = tk.Tk()
    application = CheckImageVideos(main_window)
    main_window.mainloop()  
