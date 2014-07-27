#include <windowsx.h>
#include <mmsystem.h>
#include "resource.h"
//º¯ÊýÉùÃ÷
BOOL CALLBACK Main_DlgProc(HWND hWnd,UINT uMsg,WPARAM wParam,LPARAM lParam);
BOOL Main_OnInitDialog(HWND hWnd,HWND hWndFocus,LPARAM lParam);
void Main_OnCommand(HWND hWnd,int id,HWND hWndCtl,UINT codeNotify);
void Main_OnClose(HWND hWndDlg);
