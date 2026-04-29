import os

def rename_assets(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if '?' in file or '%3F' in file:
                old_path = os.path.join(root, file)
                
                new_name = file
                if '?' in new_name:
                    new_name = new_name.split('?')[0]
                if '%3F' in new_name:
                    new_name = new_name.split('%3F')[0]
                
                new_path = os.path.join(root, new_name)
                
                if os.path.exists(new_path) and new_path != old_path:
                    os.remove(new_path)
                
                print(f"Renaming {old_path} -> {new_path}")
                os.rename(old_path, new_path)

if __name__ == '__main__':
    rename_assets('.')
