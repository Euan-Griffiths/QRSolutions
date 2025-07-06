# my_module.py
from pathlib import Path
import os

def save_file(content, filename="output.txt"):
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
    
# my_module.py
from pathlib import Path
import os

def save_file_to_location(content, filepath=None):
    """
    Save content to a specific location chosen by the user.
    
    Args:
        content: Content to save
        filepath: Desired full path (optional)
    
    Returns:
        Path: Full path where the file was saved
    """
    if filepath is None:
        # Default to current working directory
        filepath = Path.cwd() / "output.txt"
    else:
        # Ensure parent directory exists
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
    
    try:
        with open(filepath, 'w') as f:
            f.write(content)
        return filepath
    except PermissionError:
        raise PermissionError("Insufficient permissions to save file")
    except Exception as e:
        raise IOError(f"Failed to save file: {str(e)}")