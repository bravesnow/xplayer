#include <windows.h>
#include <commdlg.h>
#include "DlgHeader.h"

int APIENTRY WinMain(HINSTANCE hInstance,
                     HINSTANCE hPrevInstance,
                     LPSTR     lpCmdLine,
                     int       nCmdShow)
{
	DialogBox(hInstance,MAKEINTRESOURCE(IDD_MAIN),NULL,Main_DlgProc);
	return 0;
}
BOOL CALLBACK Main_DlgProc(HWND hWnd,UINT uMsg,WPARAM wParam,LPARAM lParam)
{
	switch(uMsg)
	{
		HANDLE_MSG(hWnd,WM_INITDIALOG,Main_OnInitDialog);
		HANDLE_MSG(hWnd,WM_COMMAND,Main_OnCommand);
		HANDLE_MSG(hWnd,WM_CLOSE,Main_OnClose);
	}
	
	return 0;
}
BOOL Main_OnInitDialog(HWND hWnd,HWND hWndFocus,LPARAM lParam)
{
	//SetDlgItemText(hWnd,IDC_EDITNAME,TEXT(""));
	return 1;
}
void Main_OnCommand(HWND hWnd,int id,HWND hWndCtl,UINT codeNotify)
{
	switch(id)
	{
	case IDC_LIST:
		{
			if(LBN_DBLCLK==codeNotify){
				mciSendString("close movie","",0,NULL);
				int index=SendDlgItemMessage(hWnd,IDC_LIST,LB_GETCURSEL,0,0);
				TCHAR strFile[MAX_PATH];
				SendDlgItemMessage(hWnd,IDC_LIST,LB_GETTEXT,index,(LPARAM)strFile);		
				TCHAR strShortPath[MAX_PATH];
				GetShortPathName(strFile,strShortPath,sizeof(strShortPath));
				HWND hEditvideo=GetDlgItem(hWnd,IDC_EDITVIDEO);
				TCHAR mciCtrlOpen[256];
				ZeroMemory(mciCtrlOpen,sizeof(mciCtrlOpen));
				wsprintf(mciCtrlOpen,"open %s type MPEGVideo Alias movie parent %u Style %u notify",strShortPath,hEditvideo,WS_CHILD);	
				mciSendString(mciCtrlOpen,"",0,NULL);
				mciSendString("play movie","",0,NULL);		
			}
			else if(LBN_SELCHANGE){//have a bug!
				TCHAR strFile[MAX_PATH];
				int index = SendDlgItemMessage(hWnd,IDC_LIST,LB_GETCURSEL,0,0);
				SendDlgItemMessage(hWnd,IDC_LIST,LB_GETTEXT,0,(LPARAM)strFile);
				TCHAR strShortPath[MAX_PATH];
				GetShortPathName(strFile,strShortPath,sizeof(strShortPath));
				HWND hEditvideo=GetDlgItem(hWnd,IDC_EDITVIDEO);
				TCHAR mciCtrlOpen[256];
				ZeroMemory(mciCtrlOpen,sizeof(mciCtrlOpen));
				wsprintf(mciCtrlOpen,"open %s type MPEGVideo Alias movie parent %u Style %u notify",strShortPath,hEditvideo,WS_CHILD);	
				mciSendString(mciCtrlOpen,"",0,NULL);
			}				
		}break;
	/*case IDC_BUTTONFULL:
		{//全屏
				mciSendString("play movie fullscreen","",0,NULL);
		}*/
	case IDC_BUTTONPLAYER:
		{//播放
			mciSendString("play movie","",0,NULL);
		}break;
	case IDC_BUTTONSTOP:
		{//停止
			mciSendString("close movie","",0,NULL);
		}break;
	case IDC_BUTTONPAUSE:
		{//暂停
			mciSendString("pause movie","",0,NULL);
		}break;
	case IDC_BUTTONADD:
		{//添加
			//打开文件对话框代码
			OPENFILENAME ofn; 
			TCHAR szFile[MAX_PATH]; 
			ZeroMemory(&ofn,sizeof(ofn)); 
			ofn.lStructSize = sizeof(ofn); 
			ofn.lpstrFile = szFile; 
			ofn.lpstrFile[0] = TEXT('\0'); 
			ofn.nMaxFile = sizeof(szFile); 
			ofn.lpstrFilter = TEXT("ALL\0*.*\0mp3\0*.mp3\0AVI\0*.avi\0");//设置过滤器
			ofn.nFilterIndex = 2;//默认过滤器的选择项
			ofn.lpstrFileTitle = NULL; 
			ofn.nMaxFileTitle = 0; 
			ofn.lpstrInitialDir = NULL; 
			ofn.hwndOwner = hWnd;//
			ofn.Flags = OFN_EXPLORER |OFN_PATHMUSTEXIST | OFN_FILEMUSTEXIST|OFN_ALLOWMULTISELECT;//打开多个文件的选项
			GetOpenFileName(&ofn);
			SendDlgItemMessage(hWnd,IDC_LIST,LB_INSERTSTRING,-1,(LPARAM)szFile);		
		}break;
	
	default:
		break;
	}
}
void Main_OnClose(HWND hWndDlg)
{
	EndDialog(hWndDlg,0);
}

