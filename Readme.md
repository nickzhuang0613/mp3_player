//======================//
�ļ�������API˵����
���ߣ�NICKZHUANG
ʱ�䣺2019/5/24
//======================//
SetCursorPosition(unsigned int x,unsigned int y)   -->   ���¶�λ��꣬x��ʾ���ˮƽ���꣬y��ʾ��괹ֱ����

void HideCursor()          -->   ���ع��

ClearRec(unsigned int start_x,unsigned int end_x, unsigned int start_y,unsigned int end_y)
  ^                                ^                      ^                             ^                           ^
  ^                              ˮƽ��ʼ            ˮƽ����                   ��ֱ��ʼ                ��ֱ����
  ^ 
   |________���ѡ����Ļ���������

CLearALL()  -->  �����Ļ��������

SetWindowsSize(unsigned int x,unsigned int y)  --> ���ô��ڴ�С

MusicShow() -->  ��ʾ�����б�

MusicLoad()  -->  �������֣�ֻ֧�ּ���һ�Σ����ֿ��и�����Ҫ����

StopMusic()  -->  ֹͣ��������

PlayMusic()   -->  ��������

PauseMusic()  -->  ��ͣ����

NextMusic()  --> ��һ��

PrevMusic()  -->  ��һ��

unsigned char DelayMs(unsigned int *dly) --> ms����ʱ����ʱ�������1

DelayMsBlockage��unsigned int dly�� -->  ���뼶��ʱ�����������

ע������������ֲ�����ʵ��ʱ��Ҫ�ڹ���Ŀ¼�½���music�ļ��У����ִ���ڴ�


                    
                   