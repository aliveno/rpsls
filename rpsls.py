#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�ֲ������������Ԭ����
���ڣ�2020.04.14
"""

import random
# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����
def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if name=="ʯͷ":
        return 0
    elif name=="ʷ����":
        return 1
    elif name=="ֽ":
        return 2
    elif name=="����":
        return 3
    elif name=="����":
        return 4
    else:
        return 5.5
        # ~ print("Error: No Correct Name")
    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������


def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    if number == 0:
        return "ʯͷ"
    elif number == 1:
        return "ʷ����"
    elif number == 2:
	    return "ֽ"
    elif number == 3:
	    return "����"
    elif number == 4:
	    return "����"
    else:
        return 5.5
        # ~ print("Error: No Correct Name")


def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
    print()
    print("����ѡ��Ϊ��",player_choice)
    player_choice_number=name_to_number(player_choice)
    compu_number=random.randrange(0,5)
    compu_choice=number_to_name(compu_number)
    print("������ѡ��Ϊ��",compu_choice)
    difference=(player_choice_number-compu_number)%5
    if difference==1 or difference==2:
        print("��Ӯ��")
    elif difference==3 or difference==4:
        print("�����Ӯ��")
    elif difference ==0:
        print("���ͼ��������һ����")
    else:
        print("Error: No Correct Name")
    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)


