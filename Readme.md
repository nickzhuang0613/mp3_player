//======================//
文件：常用API说明：
作者：NICKZHUANG
时间：2019/5/24
//======================//
SetCursorPosition(unsigned int x,unsigned int y)   -->   重新定位光标，x表示光标水平坐标，y表示光标垂直坐标

void HideCursor()          -->   隐藏光标

ClearRec(unsigned int start_x,unsigned int end_x, unsigned int start_y,unsigned int end_y)
  ^                                ^                      ^                             ^                           ^
  ^                              水平起始            水平结束                   垂直开始                垂直结束
  ^ 
   |________清楚选的屏幕区域的内容

CLearALL()  -->  清除屏幕所有区域

SetWindowsSize(unsigned int x,unsigned int y)  --> 设置窗口大小

MusicShow() -->  显示音乐列表

MusicLoad()  -->  加载音乐，只支持加载一次，音乐库有更新需要重启

StopMusic()  -->  停止播放音乐

PlayMusic()   -->  播放音乐

PauseMusic()  -->  暂停播放

NextMusic()  --> 下一首

PrevMusic()  -->  上一首

unsigned char DelayMs(unsigned int *dly) --> ms级延时，延时结束输出1

DelayMsBlockage（unsigned int dly） -->  毫秒级延时，会堵塞进程

注意事项：用于音乐播放器实现时需要在工作目录下建立music文件夹，音乐存放于此


                    
                   