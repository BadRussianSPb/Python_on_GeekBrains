import os

proj_dir = 'Pavlov_Egor_dz_7_3/my_project'
sett_dir = 'settings'
main_dir = 'mainapp'
adm_dir = 'adminapp'
auth_dir = 'authapp'

dict_of_dirs = {proj_dir: (sett_dir, main_dir, adm_dir, auth_dir)}
for dir in dict_of_dirs:
    for el in dict_of_dirs[dir]:
        dir_path = os.path.join(dir, el)
        os.makedirs(dir_path, exist_ok=True)
