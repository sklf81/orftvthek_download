# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'orftvthek_downloader.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from main import downloadAsMP4

icon_base64 = b"iVBORw0KGgoAAAANSUhEUgAAAPoAAAD6CAYAAACI7Fo9AAABhGlDQ1BJQ0MgcHJvZmlsZQAAKJF9kT1Iw0AcxV9Ti0VaHOwg4pChOlkQFXHUKhShQqgVWnUwufQLmjQkKS6OgmvBwY/FqoOLs64OroIg+AHi7OCk6CIl/i8ptIjx4Lgf7+497t4BQrPKNKtnHNB028ykkmIuvyr2viKEKCJIICwzy5iTpDR8x9c9Any9S/As/3N/jqhasBgQEIlnmWHaxBvE05u2wXmfOMbKskp8Tjxm0gWJH7muePzGueSywDNjZjYzTxwjFktdrHQxK5sa8RRxXNV0yhdyHquctzhr1Tpr35O/MFLQV5a5TnMYKSxiCRJEKKijgips6qsCnRQLGdpP+viHXL9ELoVcFTByLKAGDbLrB/+D391axckJLymSBEIvjvMxAvTuAq2G43wfO07rBAg+A1d6x19rAjOfpDc6WvwI6N8GLq47mrIHXO4Ag0+GbMquFKQpFIvA+xl9Ux4YuAX61rze2vs4fQCy1FX6Bjg4BEZLlL3u8+5wd2//nmn39wNDwnKUJ5x7lwAAAAZiS0dEAP8A/wD/oL2nkwAAAAlwSFlzAAAuIwAALiMBeKU/dgAAAAd0SU1FB+gFDQ0SO81ubkYAAAAZdEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIEdJTVBXgQ4XAAAPMElEQVR42u3deWyU1R7G8WdKK5sjilgRkYu44xZMMAbF68IiKAgaFRHiFpEbTERDDLjiH3rjgokgiIAoCggCKqiIyGUHwYpgoUSrFoWi2DQITtlK6dw/DlyFS8tMO/PrO+f9fpLGm6udM3Pe+fV93nPe95xIXPq3pOslnSYpRwB8sV/Sb5L+ky0pKqmZpFxJx9E3gDfKDxZ7NEtSnP4AvBbPog8A/1HoQEgKPUI3AF6LcEYHiO4AKHQAFDoACh0AhQ4glYXOnXFACAqdeXSA6A6A6A4g6OJEd8B/3AILEN0BeBHds2v9Erm5UsuWUkVFeLsxO7vmnz+R363qv6nud/Pz3XFp2tT2c+bnh+OYX3aZ3Xc+O1sqLpZKSmr+ErV+E/feKw0ZIsUJBoGxe7fUurU0YIA0cKBdu5WVUt++0sKFfvfv4MHSE0/YfecjEWnoUOnNN2tV6LUbjGvcWGrWjOIKkl27pGhUWrxYGjbMnRGs9Ojhf6H372/7nd++vVZFLgbjPJeXJ23ZYttmnz7uj4zPzj3Xtr2lS2v9EgzG+SwWkyZMsL2sys2VOnXyt09ffFE6/njbNqdPr+0rsDik9+bNk8rL7drLypJuu83f/uzZ07a9n36Spk1LyRkdPvvmG/dj6cYb3Yi/b9q0cYOcllI03kGhh8GYMW5E3Eo0Kl17rX/9+MwzUv36du3t3y+NHUuhI0ErV0plZXbtRSLS3Xf714/Wf7zWrUtZGqPQw6CoSJo717bNK6+ULrnEnz685hqpRQvbNlN4zCj0sJg40fbuxfr1peuu86f/hgyR6tWza2/nTmn4cAodSVq1Stq2zTa+33OPP/3Xvr1te8uXp/TlKPSwiMWkSZNs27zwQqljx8zvu/79pVNOsW3zgw9S+meXQg+T2bNt59Szs6WuXTO/3wYOdAnFyubN7lKLMzpqJC9PKiiwbbNfv8zvt7ZtbdtL/bMCrDATOqNH294S27Klu4EmUw0dKp14ol17Bw6k4xKL6B46ixa5p9us1Ksn9eqVuf3Vt69te+vXu6cOU4xCD5uiIvvHSHv3dg+7ZJpoVDrrLNs2581Ly8tS6GE0ZoyLiFZOOikz59Sff15q1MiuvV27XJsUOlJi7VqptNSuvaws6c47M6+funWzbW/lSjcNSqEjJUpKpKlTbdvs1Ml+wYbaaNtWatXKts2PPkrf31qx8EQ4vf++7Zx6w4aZFd+fflrKybFr77ff3CVVeqRgFdjvvpM++yw4B6iyUurSxfYgFRa6BQKCYs+eY0fAVaukH3+0myOORNwdZil67DLtrO/oS/MAae0LfepU+xh4LLt32xZ6QYF0yy2Zd1Z//XVp5Ei7u77at3c/eXnBvzZv3tyuvXhcmjIlrU1wjR5m8+e7s7+VnBypc+fg98ujj7oBRCsbN6Y9FVPoYVZYKK1YYdtm//7B75d27Wzb+/zztDdBoYfdqFG2c+rnnBPss/qAAdLJJ9u1t3evuy2ZQkdarV4t7dhh1169elL37sHtjwcesO//oiIKHWlWUiLNmmXb5h13BHeTh/POs23v449NmqHQIb3zjltx1Mqpp7op0KB59lnbP0ClpdKIEWaFzmOqYZefL/3yi117WVnBnI68/Xbb9hYtsmqJx1Qhd3PNuHG2z6kHbZOH3Fz7zRlqv9VSUmd0boGF9OmnbgTYygknBGuPtueekxo0sGuvsNBybIS913DQxo3SmjV27UUi0l13BefzW0/5zZ9v2hyFjr+MHGm7ddNVVwVjk4f27aXTT7drr7xcGj/evNAZjIPz5Zdu4wArDRoEI74//rhbsdbK11+7AVDD/MQZHX8pLnbX6paCsEpshw627Vn3sRiMw5HGjbPduunii+t2k4dbb5WaNbNrb8eOtC0XVQ0G43CEdeukrVvt2svOtl+y6e8eftj2SbU0rPCaaHTnGh1/icWkt96ybbMu15O76CLb9lK71VJS0R043Icf2s6pt2ol9ehh/zkHD3Yr1FrZtEl69906K3Su0XG4/HxpwwbDb2GW1LOn/ee03u3VeO6ca3Qcm/Wceu/etg+URKPS2WfbtVdRUWdnc6I7qrZokVRWZtde06a2Wzc99ZTUuLFde2vX2q/mc0ShMxiH/1dcLC1YYNdeJGL7RJv103N1u1IyN8ygGqNG2c6pd+5ss8lDmza2T86VlUkvv1ynh5LBOFRtzRq3Ao2VRo1sbokdPlyqX9/ucy1ZkratlhLEYByqEYtJkyfbxneLbYqvv962H2fPrvNDSaGjetOnS/v22bV3+eXuabJ0ueYa2y2ct241f1KtqkJnMA5V++Ybt0iClZwc6YYb0vf6jz1m+6Ra3c2dH5aVOKPj2F57zXaZqXTeEpvOtHCkykrpvfcCcQgZjMOxLVgg7dpl195550ldu6b+dfv1s92cYf166YsvgnAEGYxDAoqKpGXLDE8/Wel5ou2hh+w2lJSkuXMDcwgpdCTm1Vdt59Rvuy21rxeNShdcYPf+9+yRJkwIVKEzGIdjW7tW2r7drr3TTkvtOuuDBrmVZ60sX26y1VKCGIxDgkpKpBkzDL+aEenmm1P3eta7uBpttZTMGZ3BOCRm0iS3gqmVVG3ykJsrnXmm7R/FUaOCdOTiRHckLi/PLZ5g5YQTUjMo99RTUsOGdu87GHPnRHfUwtixdnPqkUhqBuUsV6+Jx6WZMwN32IjuSM7cuW5E2UrHjrXb5OGSS6QWLeze73ffBeLe9qNFdyBxhYXSV1/ZtdegQe1unnnySXdbreUfwgCi0JG8V16RDhywa69Pn5r/7tVX273PffvcXvMUOrywerXt1k2XXlqzTR66dbPdnGHVKuutlih0pFFJiTRnjl179epJ3bsn/3tDhrjftVIHWy0lU+hMryF5b7xhO6ee7F1y0ajUrp3d+9u+XXrppaAeLabXUEMFBbZbN7VundydcnfeKZ14ot37s1xIs4ZndKbXkLxYzPahjaws6aabEv/vH3zQ9km1Dz8M8tFieg21MHOm7Zx6r16JbfKQm2uzmuwhP/0kTZsW+DM6UDOFhbajzCefnNh67IMGSccfb/e+Ajp3TqEjdV55xW7rpkgksd1cLHdnraiQpk6l0OG5lSulP/+0a69zZ7cBQ1VatpTOOMPu/eTluflzCh1eKy62XRetcePqB+WeecbdNmvlk08y4jBR6EhNfN+/36696ubU07HWXFX+/DNoz51T6EijggLp99/t2qtqk4crrpBOPdXufSxcWNdbLVHoMBSL2T7MkZNz9Ftihw2z3ZwheI+jUuhIsylTbOfUj4zv0ajUoYNd+5s3S2+/TaEjZDZulL7/3q69888//Dn1Ll2kpk3t2s+AuXMKHenx6qt2c+pZWW7xyEMeecT9fxYOHHCbT1LoCKUFC6SyMrv2Dt0lF41KF11k1+6330qLF1PoCKniYmnpUrv2WrRwq8/cf7/UpIlduwFbs51Ch70RI+y2bopE3Aqv991n9/l27w7UVkuJyuabiZRas0YqLZWaN7dp78YbbRd/XLzYJRfO6Ai1WMx2oKpJE6lRI2I7hQ5zEydKe/f697m2bXMbWFDogNwz6sHZSTR1Mmzu/MhCZ3FIpN7o0XZbN1kI6FZLCWJxSKTJnDnSrl3+fJ4NG6TPPsvoMzqLQyL1iovdRg++yNBBuEN5hDM60uell+zm1NNp71730E4Go9CRPmvXSn/8kfmfY/ly99AOhQ4cRUlJRj2z7Wlsp9BhYNQot8topiotlUaO9KLQmV5D+uTnS1u2ZO77nzfPh6PA9BoMjB+fuXPqH33kxSFgeg3pN3Ome+or03z/vTRrlg9HIE50R/oVFUnr1mXe+7bcA57oDi+MGOGWYMoU+/dLM2Z40/1Ed9hYsULauTNz3u+qVW67JT9wZxyMlJRIn3+eOe/Xh/n/I87oXKPDxssvS+XlwX+fO3ZI48b51PNco8PQDz9Iv/4a/Pc5f37GbLWUzBkdsGG9dROx/bBCZzAOdiZNCvac+qZN0tSpvvU68+gwVlQU7CfBPHiAhWt0BIPl1k3JqKjI5OWiiO4ImPnzgzmnvmaNtGyZjz3OPDrqQEmJtGRJ8N6XJw+wVHVG5xod9l54wd1mGhRlZdLkyb72NtfoqCMFBe7MHhQLFmTkVkvJnNEBe7GYNG1acN6Pn6Pt/+PnJosLF0oNGvy12EEkUvOFDyIHr2yO9vuH/t2331K4NTFmjNvXPDvb9e/fj9PR/ndtjmN1ysvdNlIei8Sl1yR1l3S6pOP49gHeKJe0VdJcojsQAsyjA/7jFlggBJheA8IS3QFQ6AAodAAZUeiMugN+4+k1gOgOgEIHkBGYRwc4owPwAYNxANEdgDfRnYdaAK7RAVDoAAIvW1JMUqmknIM/APyw/2Btx+gKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKge+64lIS41FLvbBEVlRNpDN1DoqS7ybEljJPWlNwLhPUn/ikgVdAWFnupibyVpqaR/0Bt16hdJ/4y4fyIBxNDkbJE0VFI5XVFnyiU9LmkzXUGhpyv+xCV9IGmGO8HDPlRppqSZEfqf6E6EJ7KDMzoRnshOoYMIT2QnuoMIT2TnjE6EB5GdQifCg8hOdCfCg8jOGZ0IT2QHhU6EJ7KD6E6EJ7JzRgcRnshOoYMIT2QnuoMIT2TnjE6EB5GdQifCg8hOdCfCE9nBGZ0IT2QHgnBWPy4uTY5LlXEpzs9hP5VxaUpcOo5vCtGdCE9kB9GdCE9kB4jwRHYQ3YnwRHaiO4jwRHaACE9kB6qJ8HHp5xAW+s9xLluI7kR4IjtAhCeyA0R4IjsQzEKPxKU+cWmfx0W+Ly71jTOVCyK8txGeyA6EIMIT2QHPIzyRHfA8whPZgRBEeCI74HmEJ7IDnkd4IjsQgghPZAc8j/BEdsDzCE9kB0IQ4YnsgOcRnsgOeB7hiexACCI8kR3wPMIT2QHPIzyRHQhBhCeyA55HeCI74HmEJ7IDIYjwRHbA8whPZAc8j/BEdiAEEZ7IDnge4YnsgOcRnsgOhCDCE9kBzyM8kR3wPMIT2YEQRHgiO+B5hCeyA55HeCI7EIIIT2QHPI/wRHbA8whPZAdCEOGJ7IDnEZ7IDnge4YnsQAgiPJEd8DzCE9kBzyM8kR3wPMJvOvhDZA8RYlvIIryk2w8e9+kRKU6vhMN/ASIYAZHwtLNlAAAAAElFTkSuQmCC"

def iconFromBase64(base64):
    pixmap = QtGui.QPixmap()
    pixmap.loadFromData(QtCore.QByteArray.fromBase64(base64))
    icon = QtGui.QIcon(pixmap)
    return icon

class Ui_Form(object):
    def setupUi(self, Form, Dialog):
        Form.setObjectName("Form")
        #Form.resize(400, 192)
        Form.setFixedSize(400, 200)
        
        #Form.setWindowIcon(QtGui.QIcon("icons/icon.png"))
        Form.setWindowIcon(iconFromBase64(icon_base64))
        
        self.downloadButton = QtWidgets.QPushButton(Form)
        self.downloadButton.setGeometry(QtCore.QRect(10, 160, 371, 26))
        self.downloadButton.setObjectName("downloadButton")
        self.label_url = QtWidgets.QLabel(Form)
        self.label_url.setGeometry(QtCore.QRect(20, 20, 141, 18))
        self.label_url.setObjectName("label_url")
        self.textEdit_url = QtWidgets.QTextEdit(Form)
        self.textEdit_url.setGeometry(QtCore.QRect(10, 50, 371, 31))
        self.textEdit_url.setObjectName("textEdit_url")
        self.pushButton_info = QtWidgets.QPushButton(Form)
        self.pushButton_info.setGeometry(QtCore.QRect(339, 10, 41, 26))
        self.pushButton_info.setObjectName("pushButton_info")
        self.label_filename = QtWidgets.QLabel(Form)
        self.label_filename.setGeometry(QtCore.QRect(20, 90, 141, 18))
        self.label_filename.setObjectName("label_filename")
        self.textEdit_filename = QtWidgets.QTextEdit(Form)
        self.textEdit_filename.setGeometry(QtCore.QRect(10, 110, 371, 31))
        self.textEdit_filename.setObjectName("textEdit_filename")
        
        self.infoDialog = Dialog
        self.pushButton_info.clicked.connect(self.openInfoDialog)
        self.downloadButton.clicked.connect(self.downloadVideo)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ORF-TVthek-Greifer"))
        self.downloadButton.setText(_translate("Form", "Download"))
        self.label_url.setText(_translate("Form", "Hyperlink zum Stream:"))
        self.pushButton_info.setText(_translate("Form", "Info"))
        self.label_filename.setText(_translate("Form", "Dateiname:"))
        
    def openInfoDialog(self):
        self.infoDialog.show()
        
    def downloadVideo(self):
        url = self.textEdit_url.toPlainText()
        filename = self.textEdit_filename.toPlainText()
        
        if "." in filename:
            index = filename.index(".")
            filename = filename[index:]
        
        if url=="" or filename=="":
            print("ERROR: Bitte geben Sie die URL und den Dateinamen an!")
            return
        
        #Print Input to console
        print("--------")
        print("Eingabe:")
        print("  URL: " + url)
        print("  Dateiname: " + filename)
        print("--------")
        
        #Do the download
        stream_url = downloadAsMP4(url, filename)
        
        print("--------")
        print("Download beendet von " + stream_url)
        print("Bitte überprüfen Sie, ob der download erfolgreich war")
        print("Das Video sollte unter /downloads/"+filename+".mp4 zu finden sein")
        print("--------")
        
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        #Dialog.resize(400, 435)
        Dialog.setFixedSize(400, 435)
        Dialog.setWindowIcon(QtGui.QIcon("icons/icon.png"))
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 390, 351, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.label_info_title = QtWidgets.QLabel(Dialog)
        self.label_info_title.setGeometry(QtCore.QRect(90, 10, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_info_title.setFont(font)
        self.label_info_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_info_title.setObjectName("label_info_title")
        self.label_info_text = QtWidgets.QLabel(Dialog)
        self.label_info_text.setGeometry(QtCore.QRect(30, 40, 331, 261))
        self.label_info_text.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_info_text.setWordWrap(True)
        self.label_info_text.setObjectName("label_info_text")
        self.label_docs = QtWidgets.QLabel(Dialog)
        self.label_docs.setGeometry(QtCore.QRect(110, 360, 161, 18))
        self.label_docs.setObjectName("label_docs")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Informationen"))
        self.label_info_title.setText(_translate("Dialog", "Informationen"))
        self.label_info_text.setText(_translate("Dialog", "Der ORF-TVthek-Greifer ist ein einfaches Programm für den Download von ORF-TVthek Inhalten. \n"
"\n"
"Um einen Inhalt herunterzuladen muss man die entsprechende Adresse im oberen Textfeld eingeben, dann den gewünschten Dateinamen eingeben (bitte ohne Dateiendung) und dann auf \"Download\" klicken.\n"
"\n"
"Da die ORF-Tvthek stetig im Wandel ist, kann es vorkommen, dass das Programm rekonfiguguriert werden muss. Dafür steht Ihnen der Quellcode dieses Programms in den unten angegebenen Dokumentationen zur Verfügung."))
        self.label_docs.setText(_translate("Dialog", "<a href=\"https://github.com/sklf81/orftvthek_download/blob/main/README.md/\">Zu den Dokumentationen</a>"))
        self.label_docs.setOpenExternalLinks(True)

def createUI():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    Dialog = QtWidgets.QDialog()
    dialog_ui = Ui_Dialog()
    dialog_ui.setupUi(Dialog)
    ui = Ui_Form()
    ui.setupUi(Form, Dialog)
    #app.setWindowIcon(QtGui.QIcon('/icons/icon.ico'))
    #Form.setWindowIcon(app.windowIcon())
    Form.show()
    sys.exit(app.exec_())
    
    
    """
    Anmerkung: Titel: ORF-TVthek Herunterladen
    """

#createUI()