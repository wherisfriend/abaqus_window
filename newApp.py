# -*- coding: UTF-8-*-
# -*- coding: mbcs -*-  

import sys
# ������pyc�ļ�
sys.dont_write_bytecode = True

# ����abaqusGuiģ�飬����ʹ��Abaqus GUI Toolkit
from abaqusGui import *
# �����������ļ�
from mainWindow import MainWindow

# ����Ӧ�ó���
app = AFXApp('Abaqus/CAE', '���ʵ����', '���������Զ���ģϵͳ', 1, 1, 1)

# ��ʼ���մ�����Ӧ�ó���
app.init(sys.argv)

# ����������
mw = MainWindow(app)

# ����Ӧ�ó���
app.create()

# �Զ�����ģ��
# switchMoudle('Load')
# ����Ӧ�ó���
app.run()
