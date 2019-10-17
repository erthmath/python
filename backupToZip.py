#!/usr/bin/env python3

import zipfile, os

def backupToZip(folder):
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1
    print(f'Creating {zipFilename}')
    backupZip = zipfile.ZipFile(zipFilename, 'w')
        #Percorre toda a arvore de diretorio e compacta os arquivos de cada pasta
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        backupZip.write(foldername)
            #Acrescenta todos os arquivos dessa pasta ao arquivo ZIP
        for filename in filenames:
            if filename.startswith(os.path.basename(folder) + '_') and filename.endswith('.zip'):
                continue  #no faz backup dos arquivos ZIP de backup
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done')

backupToZip('/home/ma/PY')
