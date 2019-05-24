.LOG

//======================================================================//
文件：常用API说明：
作者：NICKZHUANG
时间：2019/5/24
备注：如果出现新的修补，在文末自动插入 的时间后面备注，一处修补一处说明，并用序号标明。
          备注完毕，用多个"="隔开
//=======================================================================//
SetCursorPosition(unsigned int x,unsigned int y)   -->   重新定位光标，x表示光标水平坐标，y表示光标垂直坐标

void HideCursor()          -->   隐藏光标

ClearRec(unsigned int start_x /*水平起始*/,unsigned int end_x/*水平结束*/, \
         unsigned int start_y/*垂直开始*/,unsigned int end_y/*垂直结束*/)  --> 清楚选定的屏幕矩形区域的内容


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


                    
                   
14:31 2019/5/24 ：
     1、修改ReadMe文件
==========================================================================

