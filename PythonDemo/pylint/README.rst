http://www.pylint.org/
http://docs.pylint.org/

pip install pylint


1. �������ģ�����ڵ��ļ��У����� pylint [options] module.py
���ֵ��÷�ʽ��һֱ���Թ����ģ���Ϊ��ǰ�Ĺ���Ŀ¼�ᱻ�Զ����� Python ��·���С�
2. ������ģ�����ڵ��ļ��У����� pylint [options] directory/module.py
���ֵ��÷�ʽ���������������ʱ���ǿ��Թ����ģ�directory �Ǹ� Python �� ( �������һ�� __init__.py �ļ� )������ directory �������� Python ��·���С�
ʹ�� Pylint ��һ���� pakage ���д����飺

1. ��������������ļ��У����� pylint [options] pakage��
���ֵ��÷�ʽ��һֱ���Թ����ģ���Ϊ��ǰ�Ĺ���Ŀ¼�ᱻ�Զ����� Python ��·���С�
2. ����������ڵ��ļ��У����� pylint [options] directory/ pakage��
��������µ��������������ʱ���ǿ��Թ����ģ�directory �������� Python ��·���С������� Linux �ϣ�export PYTHONPATH=$PYTHONPATH: directory��
���⣬���ڰ�װ�� tkinter ���Ļ���������ʹ������ pylint-gui��һ���򵥵� GUI ���棬����������ģ����߰������� ( ����ͬ������ ), ��� Run��Pylint ��������� GUI ����ʾ��