package com.yscoco.wyboem.ble;

import android.os.Handler;
import android.os.Looper;
import android.util.Log;
import com.yscoco.blue.utils.BleUtils;
import com.yscoco.wyboem.MultimeterApp;
import com.yscoco.yscocomodule.log.LogUtils;
import java.util.ArrayList;
import java.util.List;

public class NotifyOrWriteUtil {
  public static int dataType;
  
  public static Handler handler = new Handler(Looper.getMainLooper());
  
  public static boolean isSend;
  
  public static Runnable mRunnable;
  
  public static byte[] sendByte;
  
  public static List<byte[]> sendBytes = (List)new ArrayList<byte>();
  
  static {
    sendByte = null;
    isSend = false;
    dataType = 1;
    mRunnable = new Runnable() {
        public void run() {
          NotifyOrWriteUtil.clearState();
          LogUtils.e("NotifyOrWriteUtils:超时清除状态");
        }
      };
  }
  
  public static void clearState() {
    handler.removeCallbacks(mRunnable);
    isSend = false;
    List<byte[]> list = sendBytes;
    if (list != null && list.size() > 0)
      sendBytes.remove(0); 
  }
  
  public static void notify(String paramString, byte[] paramArrayOfbyte) {
    DataParsing.parsingData(paramString, paramArrayOfbyte);
  }
  
  public static boolean writeData(String paramString, byte[] paramArrayOfbyte) {
    Log.e("发送数据", BleUtils.toHexString(paramArrayOfbyte));
    return MultimeterApp.getBleDriver().writeData(paramString, paramArrayOfbyte);
  }
}


/* Location:              C:\Users\xy790\Desktop\decode\dex-tools-2.1\output\!\com\yscoco\wyboem\ble\NotifyOrWriteUtil.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       1.1.3
 */