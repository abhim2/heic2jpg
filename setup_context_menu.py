import os
import sys
import winreg
import subprocess

def register_context_menu():
    try:
        # Get the current script's directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        python_exe = sys.executable
        converter_script = os.path.join(script_dir, 'heic2jpg.py')
        
        # Create the command
        command = f'"{python_exe}" "{converter_script}" "%1"'
        
        # Register the context menu
        key_path = r'*\\shell\\ConvertToJPG'
        command_key_path = r'*\\shell\\ConvertToJPG\\command'
        
        # Create the main key
        winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, key_path)
        key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, key_path, 0, winreg.KEY_WRITE)
        winreg.SetValue(key, '', winreg.REG_SZ, 'Convert to JPG')
        key.Close()
        
        # Create the command key
        winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, command_key_path)
        key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, command_key_path, 0, winreg.KEY_WRITE)
        winreg.SetValue(key, '', winreg.REG_SZ, command)
        key.Close()
        
        print("Context menu successfully registered!")
        return True
    except Exception as e:
        print(f"Error registering context menu: {str(e)}")
        return False

if __name__ == '__main__':
    if os.name != 'nt':
        print("This script only works on Windows")
        sys.exit(1)
        
    # Check if running as administrator
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        import ctypes
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    
    if not is_admin:
        print("Please run this script as administrator")
        sys.exit(1)
        
    register_context_menu() 