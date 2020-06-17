
import win32serviceutil
import win32service
import win32event
import servicemanager
import repeater
import os
import os.path


class RepeatService(win32serviceutil.ServiceFramework):
    _svc_name_ = "RepeatService"
    _svc_display_name_ = "UDP Repeat Service"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        servicemanager.LogMsg(
            servicemanager.EVENTLOG_INFORMATION_TYPE,
            servicemanager.PYS_SERVICE_STARTED,
            (self._svc_name_, '')
        )
        os.chdir(os.path.dirname(
            win32serviceutil.LocateSpecificServiceExe(self._svc_name_)
        ))
        repeater.main()


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(RepeatService)
