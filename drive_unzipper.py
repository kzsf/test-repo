import os
import tarfile
import urllib.request


#url = 'https://drive.google.com/uc?export=download&id=1pgBMwfzPc8h1SFbtvK3myGHZavCva-I4'
cwd = os.getcwd()
dest = os.path.join(cwd, "spm12.tar.gz")
 
url = 'https://drive.usercontent.google.com/download?id=1pgBMwfzPc8h1SFbtvK3myGHZavCva-I4&export=download&confirm=t&uuid=295c6fa9-9a67-4b26-8733-a3633c3f5940'


def download_spm():
    try:
        #download from google drive link
        urllib.request.urlretrieve(url, dest)
        print(f'File downloaded successfully: {os.path.abspath(dest)}')

        #open tarfile
        with tarfile.open(dest, 'r:gz') as tar_ref:
            #ensure destination directory exists
            os.makedirs(cwd, exist_ok=True)
            #extract to directory
            tar_ref.extractall(path=cwd)
        print(f'File extracted to: {os.path.abspath(cwd)},spm12')

    except Exception as e:
        print(f'Failed to download and extract file: {e}')
    
    return os.path.join(os.path.abspath(cwd),'spm12')

spm_path = download_spm()

print(spm_path)
