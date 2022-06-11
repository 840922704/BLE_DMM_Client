package com.yscoco.wyboem.ble.Util;

import com.yscoco.blue.utils.FileWriteUtils;
import com.yscoco.wyboem.myenum.DeviceType;
import com.yscoco.yscocomodule.log.LogUtils;
import java.util.HashSet;
import java.util.Set;

public class DataListenterUtil {
  public static Set<DataListenter> listentersSet = new HashSet<DataListenter>();
  
  public static void addListenters(DataListenter paramDataListenter) {
    listentersSet.add(paramDataListenter);
  }
  
  public static void mainNum(DeviceType paramDeviceType, String paramString1, double paramDouble, String paramString2, boolean[] paramArrayOfboolean1, byte[] paramArrayOfbyte, boolean[] paramArrayOfboolean2) {
    StringBuilder stringBuilder = new StringBuilder();
    stringBuilder.append("解析出来数据:设备类型：");
    stringBuilder.append(paramDeviceType);
    stringBuilder.append("数据：");
    stringBuilder.append(paramDouble);
    stringBuilder.append("值:");
    stringBuilder.append(paramString2);
    stringBuilder.append("单位：");
    stringBuilder.append(BleComputeUtil.getUnit(paramDeviceType, paramArrayOfboolean1));
    FileWriteUtils.initWrite(stringBuilder.toString(), "wyb_debug");
    for (DataListenter dataListenter : listentersSet) {
      StringBuilder stringBuilder1 = new StringBuilder();
      stringBuilder1.append("listenter::::");
      stringBuilder1.append(dataListenter);
      LogUtils.e(stringBuilder1.toString());
      dataListenter.mainNum(paramDeviceType, paramString1, paramDouble, paramString2, paramArrayOfboolean1, paramArrayOfbyte, paramArrayOfboolean2);
    } 
  }
  
  public static void removelisteners(DataListenter paramDataListenter) {
    listentersSet.remove(paramDataListenter);
  }
}


/* Location:              C:\Users\xy790\Desktop\decode\dex-tools-2.1\output\!\com\yscoco\wyboem\ble\Util\DataListenterUtil.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       1.1.3
 */