from os import scandir, path

source_path = path.abspath(path.join(path.dirname(__file__), '..'))
dirs = [d for d in scandir(source_path) if d.is_dir()]

scriptify = False

for d in dirs:
    for f in scandir(path.join(source_path, d.name)):
        f_name, _ = path.splitext(f.name)
        new_file = path.join(source_path, f_name + '.bat')
        new_path = path.join(source_path, d.name, f.name)
        with open(new_file, 'a+') as file:
            file.seek(0)
            if not file.read(1):
                file.write(f'@echo off\n{d.name} {new_path}')
                print(f'\n{new_file}\n - > @echo off\n - > {d.name} {new_path}\n')
                scriptify = True

if not scriptify:
    print('\nNothing to Scriptify...\n')
