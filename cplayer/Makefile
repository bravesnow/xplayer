#=======================================
#变量定义
Main = CMusicPlayer #最终可执行文件名
OBJs = DialogBased.o resource.o #目标文件
CC = gcc #主编译命令
CFlags = -lcomdlg32 -lwinmm -mwindows #编译参数 
#=======================================
ALL : $(Main) clean
$(Main) : $(OBJs)
	$(CC) -o $(Main) $(OBJs) $(CFlags)
$(OBJs) : resource.h DlgHeader.h
	$(CC) -c DialogBased.c
	windres resource.rc resource.o
#=======================================
#清理中间文件
.PHONY : clean
clean :
	del $(OBJs)
