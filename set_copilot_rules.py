import os
home_dir = os.path.expanduser("~")
vs_code_extensions_folder = os.path.join(home_dir, '.vscode', 'extensions')
extensions = os.listdir(vs_code_extensions_folder)
copilot_chat_extension = [extension for extension in extensions if 'github.copilot-chat' in extension]
copilot_chat_extension_path = os.path.join(vs_code_extensions_folder, copilot_chat_extension[0])
copilot_chat_extension_script_path = os.path.join(copilot_chat_extension_path, 'dist', 'extension.js')

print("extension_path:", copilot_chat_extension_script_path)
print('ctrl + f "you are a" to find example default prompts')

with open(copilot_chat_extension_script_path, 'r') as file:
    data = file.read()
