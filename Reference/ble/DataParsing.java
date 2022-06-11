package com.yscoco.wyboem.ble;

import com.yscoco.blue.utils.BleUtils;
import com.yscoco.blue.utils.FileWriteUtils;
import com.yscoco.wyboem.ble.Util.BleComputeUtil;
import com.yscoco.wyboem.ble.Util.DataListenterUtil;
import com.yscoco.wyboem.util.EncryptionUtil;
import com.yscoco.yscocomodule.log.LogUtils;
import java.util.Arrays;

public class DataParsing {
  public static int color;
  
  public static void dealData(String paramString, byte[] paramArrayOfbyte) {
    if (paramArrayOfbyte != null && paramArrayOfbyte.length > 9) {
      StringBuilder stringBuilder;
      if (paramArrayOfbyte[0] == -85) {
        stringBuilder = new StringBuilder();
        stringBuilder.append("接收回应数据数据");
        stringBuilder.append(BleUtils.toHexString(paramArrayOfbyte));
        LogUtils.e(stringBuilder.toString());
      } else if ((paramArrayOfbyte[0] & 0xFF) == 90 && (paramArrayOfbyte[1] & 0xFF) == 165) {
        byte b = paramArrayOfbyte[2];
        if (b != 2) {
          if (b != 3) {
            if (b != 4) {
              boolean[] arrayOfBoolean1 = BleComputeUtil.getAllResult(new BleByteBean[] { new BleByteBean(paramArrayOfbyte[3], false), new BleByteBean(paramArrayOfbyte[9], true), new BleByteBean(paramArrayOfbyte[7], true), new BleByteBean(paramArrayOfbyte[8], false), new BleByteBean(paramArrayOfbyte[8], true), new BleByteBean(paramArrayOfbyte[9], false) });
              boolean[] arrayOfBoolean2 = BleComputeUtil.getMoreResult(new BleByteBean[] { new BleByteBean(paramArrayOfbyte[9], true), new BleByteBean((byte)0, false) });
              DataListenterUtil.mainNum(BleComputeUtil.getDeviceType(paramArrayOfbyte[2]), (String)stringBuilder, BleComputeUtil.getCount(Arrays.copyOfRange(paramArrayOfbyte, 3, 8)), BleComputeUtil.getStringCount(Arrays.copyOfRange(paramArrayOfbyte, 3, 8)), arrayOfBoolean1, paramArrayOfbyte, arrayOfBoolean2);
            } else {
              if (paramArrayOfbyte.length < 19)
                return; 
              boolean[] arrayOfBoolean = BleComputeUtil.getAllResult(new BleByteBean[] { new BleByteBean(paramArrayOfbyte[3], false), new BleByteBean(paramArrayOfbyte[3], true), new BleByteBean(paramArrayOfbyte[4], false), new BleByteBean(paramArrayOfbyte[4], true), new BleByteBean(paramArrayOfbyte[13], false), new BleByteBean(paramArrayOfbyte[13], true), new BleByteBean(paramArrayOfbyte[16], true), new BleByteBean(paramArrayOfbyte[17], false), new BleByteBean(paramArrayOfbyte[18], true) });
              double d = BleComputeUtil.getCountForP66(Arrays.copyOfRange(paramArrayOfbyte, 9, 14));
              String str = BleComputeUtil.getStringCountP66(Arrays.copyOfRange(paramArrayOfbyte, 9, 14));
              StringBuilder stringBuilder1 = new StringBuilder();
              stringBuilder1.append("P66值:");
              stringBuilder1.append(d);
              LogUtils.e(stringBuilder1.toString());
              stringBuilder1 = new StringBuilder();
              stringBuilder1.append("P66值:");
              stringBuilder1.append(str);
              LogUtils.e(stringBuilder1.toString());
              DataListenterUtil.mainNum(BleComputeUtil.getDeviceType(paramArrayOfbyte[2]), (String)stringBuilder, d, str, arrayOfBoolean, paramArrayOfbyte, null);
            } 
          } else {
            if (paramArrayOfbyte.length < 11)
              return; 
            boolean[] arrayOfBoolean1 = BleComputeUtil.getRightOrderTable300(new BleByteBean[] { new BleByteBean(paramArrayOfbyte[3], false), new BleByteBean(paramArrayOfbyte[7], true), new BleByteBean(paramArrayOfbyte[8], false), new BleByteBean(paramArrayOfbyte[8], true), new BleByteBean(paramArrayOfbyte[9], false), new BleByteBean(paramArrayOfbyte[9], true), new BleByteBean(paramArrayOfbyte[10], false) });
            boolean[] arrayOfBoolean2 = BleComputeUtil.getMoreResult(new BleByteBean[] { new BleByteBean((byte)0, false), new BleByteBean(paramArrayOfbyte[10], false) });
            DataListenterUtil.mainNum(BleComputeUtil.getDeviceType(paramArrayOfbyte[2]), (String)stringBuilder, BleComputeUtil.getCount(Arrays.copyOfRange(paramArrayOfbyte, 3, 8)), BleComputeUtil.getStringCount(Arrays.copyOfRange(paramArrayOfbyte, 3, 8)), arrayOfBoolean1, paramArrayOfbyte, arrayOfBoolean2);
          } 
        } else {
          boolean[] arrayOfBoolean1 = BleComputeUtil.getAllResult(new BleByteBean[] { new BleByteBean(paramArrayOfbyte[3], false), new BleByteBean(paramArrayOfbyte[7], true), new BleByteBean(paramArrayOfbyte[8], false), new BleByteBean(paramArrayOfbyte[8], true), new BleByteBean(paramArrayOfbyte[9], false), new BleByteBean(paramArrayOfbyte[9], true) });
          boolean[] arrayOfBoolean2 = BleComputeUtil.getMoreResult(new BleByteBean[] { new BleByteBean((byte)0, false), new BleByteBean((byte)0, false) });
          DataListenterUtil.mainNum(BleComputeUtil.getDeviceType(paramArrayOfbyte[2]), (String)stringBuilder, BleComputeUtil.getCount(Arrays.copyOfRange(paramArrayOfbyte, 3, 8)), BleComputeUtil.getStringCount(Arrays.copyOfRange(paramArrayOfbyte, 3, 8)), arrayOfBoolean1, paramArrayOfbyte, arrayOfBoolean2);
        } 
      } 
    } 
  }
  
  public static void parsingData(String paramString, byte[] paramArrayOfbyte) {
    StringBuilder stringBuilder = new StringBuilder();
    stringBuilder.append("接收到的数据:");
    stringBuilder.append(BleUtils.toHexString(paramArrayOfbyte));
    FileWriteUtils.initWrite(stringBuilder.toString(), "wyb_debug");
    stringBuilder = new StringBuilder();
    stringBuilder.append("接收到的解密数据");
    stringBuilder.append(BleUtils.toHexString(EncryptionUtil.enc_code(paramArrayOfbyte)));
    FileWriteUtils.initWrite(stringBuilder.toString(), "wyb_debug");
    stringBuilder = new StringBuilder();
    stringBuilder.append("接收到的数据:");
    stringBuilder.append(BleUtils.toHexString(paramArrayOfbyte));
    LogUtils.e(stringBuilder.toString());
    stringBuilder = new StringBuilder();
    stringBuilder.append("接收到的解密数据");
    stringBuilder.append(BleUtils.toHexString(EncryptionUtil.enc_code(paramArrayOfbyte)));
    LogUtils.e(stringBuilder.toString());
    dealData(paramString, EncryptionUtil.enc_code(paramArrayOfbyte));
  }
}


/* Location:              C:\Users\xy790\Desktop\decode\dex-tools-2.1\output\!\com\yscoco\wyboem\ble\DataParsing.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       1.1.3
 */