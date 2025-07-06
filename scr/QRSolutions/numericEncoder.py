import tqdm
import PIL
from pathlib import Path
import os

class Main:
    def __init__(self):
        self.mode = "0001"
        self.charCount = 0
        self.bits = 10
        self.verison = 1
        

    def charCounter(self,Data): # Formats the char count section of the QR code with the correct length and data
        a = len(str(Data))
        self.charCount = str(bin(a))[2:].rjust(self.bits,'0')
        print(self.charCount)
        
    def main(self,Data,Error="L"):
        self.charCounter(Data)
    
    def save_file(self,content, filename="output.txt"): # Saves a image of the QR code to the users device in the CWD as a image file
        """
        Save content to a file in the current working directory.
    
        Args:
            content: Content to save
            filename: Desired filename
    
        Returns:
            Path: Full path where the file was saved
        """
        working_dir = Path.cwd()
        file_path = working_dir / filename
    
        try:
            with open(file_path, 'w') as f:
                f.write(content)
            return file_path
        except Exception as e:
            raise IOError(f"Failed to save file: {str(e)}")

def Numeric(Data,Error):
    Main.main(Data,Error)
    
if __name__ == "__main__":
    m = Main()
    m.main(100)