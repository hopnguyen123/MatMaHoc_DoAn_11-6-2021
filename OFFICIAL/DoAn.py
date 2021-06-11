import AES_ECB as aes_ecb
import SHA as sha
import RSA as rsa
import os
import time
import hashlib
import random


#Tạo key bằng tay
def Create_Key_by_Hand(data,tenfile_key):
    hash512 = hashlib.sha512(data.encode()).digest()
    b2 = hash512[32:48]
    KEY=b2
    file=open(tenfile_key,'wb').write(KEY)


#Tạo key _ Auto
def Create_Key_Auto(tenfile_key):
    key=os.urandom(16)              #Tạo key 16bytes
    file=open(tenfile_key,'wb').write(key)

#Mã hoá
def MaHoa(filename_Key,data,filesave,filePEM):
    KEY=open(filename_Key,'rb').read()
    # data=open(data).read()
    cipher=aes_ecb.Encrypt(data,KEY)

    out_sha=sha.SHA_256(cipher)

    digtl_sig = rsa.DigitalSignature()
    digtl_sig.GenerateKey(filePEM)
    chuki=digtl_sig.CreateSignature(out_sha)

    str_send=cipher+chuki
    file=open(filesave,'wb').write(str_send)

def MaHoa_1(filename_Key,file_INPUT,filesave,filePEM):
    KEY=open(filename_Key,'rb').read()
    data=open(file_INPUT).read()
    cipher=aes_ecb.Encrypt(data,KEY)

    out_sha=sha.SHA_256(cipher)

    digtl_sig = rsa.DigitalSignature()
    digtl_sig.GenerateKey(filePEM)
    chuki=digtl_sig.CreateSignature(out_sha)

    str_send=cipher+chuki
    file=open(filesave,'wb').write(str_send)

#Xác thực
def XacThuc(FileSave,FileRSA):
    str_input=open(FileSave,'rb').read()
    rsa_l=str_input[-256:]
    ct=str_input[:-256]

    hash_r=sha.SHA_256(ct)

    digtl_sig = rsa.DigitalSignature()
    out=digtl_sig.DecryptSignature(FileRSA,rsa_l)
    check=False
    if hash_r==out:
        check=True
    else:
        check=False
    return check

#Giải mã
def GiaiMa(fileName,filekey,file_out,fileRSA):
    str_input=open(fileName,'rb').read()
    ct=str_input[:-256]

    key=open(filekey,'rb').read()
    pt=aes_ecb.Decrypt(ct,key)
    file=open(file_out,'w').write(pt)

