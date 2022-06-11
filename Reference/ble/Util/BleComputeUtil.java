package com.yscoco.wyboem.ble.Util;

import android.util.Log;
import com.yscoco.wyboem.ble.BleByteBean;
import com.yscoco.wyboem.myenum.DeviceType;
import com.yscoco.yscocomodule.log.LogUtils;

public class BleComputeUtil {
  public static final String TAG = BleComputeUtil.class.getSimpleName();
  
  public static boolean[] getAllResult(BleByteBean[] paramArrayOfBleByteBean) {
    boolean[] arrayOfBoolean = new boolean[paramArrayOfBleByteBean.length * 4];
    for (byte b = 0; b < paramArrayOfBleByteBean.length; b++) {
      for (byte b1 = 0; b1 < (getIsResult(paramArrayOfBleByteBean[b].getB(), paramArrayOfBleByteBean[b].isHigh())).length; b1++)
        arrayOfBoolean[b * 4 + b1] = getIsResult(paramArrayOfBleByteBean[b].getB(), paramArrayOfBleByteBean[b].isHigh())[b1]; 
    } 
    return arrayOfBoolean;
  }
  
  public static double getCount(byte[] paramArrayOfbyte) {
    if (paramArrayOfbyte.length != 5) {
      Log.e(TAG, "数组大小不满足条件");
      return 0.0D;
    } 
    byte b = 0;
    int i = getEveryNum((paramArrayOfbyte[0] & 0xFF & 0xF0) / 16, paramArrayOfbyte[1] & 0xFF & 0xF);
    int j = getEveryNum((paramArrayOfbyte[1] & 0xFF & 0xF0) / 16, paramArrayOfbyte[2] & 0xFF & 0xF);
    int k = getEveryNum((paramArrayOfbyte[2] & 0xFF & 0xF0) / 16, paramArrayOfbyte[3] & 0xFF & 0xF);
    int m = getEveryNum((paramArrayOfbyte[3] & 0xFF & 0xF0) / 16, paramArrayOfbyte[4] & 0xFF & 0xF);
    boolean bool = hasPoint((paramArrayOfbyte[0] & 0xFF & 0xF0) / 16);
    if (hasPoint((paramArrayOfbyte[1] & 0xFF & 0xF0) / 16)) {
      b = 1;
    } else if (hasPoint((paramArrayOfbyte[2] & 0xFF & 0xF0) / 16)) {
      b = 2;
    } else if (hasPoint((paramArrayOfbyte[3] & 0xFF & 0xF0) / 16)) {
      b = 3;
    } 
    double d1 = 0.01D;
    if (b != 1) {
      if (b != 2) {
        if (b != 3) {
          d2 = (i * 1000 + j * 100 + k * 10 + m);
        } else {
          d2 = (i * 100 + j * 10 + k) + m * 0.1D;
        } 
      } else {
        d2 = (i * 10 + j) + k * 0.1D;
        d2 += m * d1;
      } 
    } else {
      d2 = i + j * 0.1D + k * 0.01D;
      d1 = 0.001D;
      d2 += m * d1;
    } 
    d1 = d2;
    if (bool)
      d1 = -d2; 
    double d2 = d1;
    if (k == 999)
      d2 = 999.999D; 
    if (i == 998)
      d2 = 999.998D; 
    if (j == 997)
      d2 = 999.997D; 
    if (j == 996 && i == 996 && k == 996 && m == 996) {
      d2 = 999.996D;
    } else if (j == 996 && i == 996 && k == 996) {
      d2 = 999.995D;
    } else if (j == 996 && i == 996) {
      d2 = 999.994D;
    } else if (i == 996) {
      d2 = 999.993D;
    } 
    return d2;
  }
  
  public static double getCountForP66(byte[] paramArrayOfbyte) {
    // Byte code:
    //   0: new java/lang/StringBuilder
    //   3: dup
    //   4: invokespecial <init> : ()V
    //   7: astore_1
    //   8: aload_1
    //   9: ldc 'P66:解析的数据为：'
    //   11: invokevirtual append : (Ljava/lang/String;)Ljava/lang/StringBuilder;
    //   14: pop
    //   15: aload_1
    //   16: aload_0
    //   17: invokestatic toHexString : ([B)Ljava/lang/String;
    //   20: invokevirtual append : (Ljava/lang/String;)Ljava/lang/StringBuilder;
    //   23: pop
    //   24: aload_1
    //   25: invokevirtual toString : ()Ljava/lang/String;
    //   28: invokestatic e : (Ljava/lang/String;)V
    //   31: aload_0
    //   32: arraylength
    //   33: istore_2
    //   34: dconst_0
    //   35: dstore_3
    //   36: iload_2
    //   37: iconst_5
    //   38: if_icmpeq -> 52
    //   41: getstatic com/yscoco/wyboem/ble/Util/BleComputeUtil.TAG : Ljava/lang/String;
    //   44: ldc '数组大小不满足条件'
    //   46: invokestatic e : (Ljava/lang/String;Ljava/lang/String;)I
    //   49: pop
    //   50: dconst_0
    //   51: dreturn
    //   52: iconst_0
    //   53: istore_2
    //   54: aload_0
    //   55: iconst_0
    //   56: baload
    //   57: sipush #239
    //   60: iand
    //   61: iconst_0
    //   62: invokestatic getEveryNumP66 : (IZ)I
    //   65: istore #5
    //   67: aload_0
    //   68: iconst_1
    //   69: baload
    //   70: sipush #239
    //   73: iand
    //   74: iconst_0
    //   75: invokestatic getEveryNumP66 : (IZ)I
    //   78: istore #6
    //   80: aload_0
    //   81: iconst_2
    //   82: baload
    //   83: sipush #239
    //   86: iand
    //   87: iconst_0
    //   88: invokestatic getEveryNumP66 : (IZ)I
    //   91: istore #7
    //   93: aload_0
    //   94: iconst_3
    //   95: baload
    //   96: sipush #239
    //   99: iand
    //   100: iconst_0
    //   101: invokestatic getEveryNumP66 : (IZ)I
    //   104: istore #8
    //   106: aload_0
    //   107: iconst_4
    //   108: baload
    //   109: sipush #239
    //   112: iand
    //   113: iconst_1
    //   114: invokestatic getEveryNumP66 : (IZ)I
    //   117: istore #9
    //   119: aload_0
    //   120: iconst_4
    //   121: baload
    //   122: sipush #128
    //   125: iand
    //   126: sipush #128
    //   129: if_icmpne -> 138
    //   132: iconst_1
    //   133: istore #10
    //   135: goto -> 141
    //   138: iconst_0
    //   139: istore #10
    //   141: aload_0
    //   142: iconst_0
    //   143: baload
    //   144: bipush #16
    //   146: iand
    //   147: ifeq -> 155
    //   150: iconst_1
    //   151: istore_2
    //   152: goto -> 208
    //   155: aload_0
    //   156: iconst_1
    //   157: baload
    //   158: bipush #16
    //   160: iand
    //   161: ifeq -> 169
    //   164: iconst_2
    //   165: istore_2
    //   166: goto -> 208
    //   169: aload_0
    //   170: iconst_2
    //   171: baload
    //   172: bipush #16
    //   174: iand
    //   175: ifeq -> 183
    //   178: iconst_4
    //   179: istore_2
    //   180: goto -> 208
    //   183: aload_0
    //   184: iconst_3
    //   185: baload
    //   186: bipush #16
    //   188: iand
    //   189: ifeq -> 197
    //   192: iconst_5
    //   193: istore_2
    //   194: goto -> 208
    //   197: aload_0
    //   198: iconst_4
    //   199: baload
    //   200: bipush #16
    //   202: iand
    //   203: ifeq -> 208
    //   206: dconst_0
    //   207: dreturn
    //   208: iload_2
    //   209: iconst_1
    //   210: if_icmpeq -> 344
    //   213: iload_2
    //   214: iconst_2
    //   215: if_icmpeq -> 308
    //   218: iload_2
    //   219: iconst_4
    //   220: if_icmpeq -> 271
    //   223: iload_2
    //   224: iconst_5
    //   225: if_icmpeq -> 231
    //   228: goto -> 386
    //   231: iload #5
    //   233: i2d
    //   234: ldc2_w 1.0E-4
    //   237: dmul
    //   238: iload #6
    //   240: i2d
    //   241: ldc2_w 0.001
    //   244: dmul
    //   245: dadd
    //   246: iload #7
    //   248: i2d
    //   249: ldc2_w 0.01
    //   252: dmul
    //   253: dadd
    //   254: iload #8
    //   256: i2d
    //   257: ldc2_w 0.1
    //   260: dmul
    //   261: dadd
    //   262: dstore_3
    //   263: iload #9
    //   265: i2d
    //   266: dstore #11
    //   268: goto -> 381
    //   271: iload #5
    //   273: i2d
    //   274: ldc2_w 0.001
    //   277: dmul
    //   278: iload #6
    //   280: i2d
    //   281: ldc2_w 0.01
    //   284: dmul
    //   285: dadd
    //   286: iload #7
    //   288: i2d
    //   289: ldc2_w 0.1
    //   292: dmul
    //   293: dadd
    //   294: iload #8
    //   296: i2d
    //   297: dadd
    //   298: dstore_3
    //   299: iload #9
    //   301: bipush #10
    //   303: imul
    //   304: istore_2
    //   305: goto -> 377
    //   308: iload #5
    //   310: i2d
    //   311: ldc2_w 0.01
    //   314: dmul
    //   315: iload #6
    //   317: i2d
    //   318: ldc2_w 0.1
    //   321: dmul
    //   322: dadd
    //   323: iload #7
    //   325: i2d
    //   326: dadd
    //   327: iload #8
    //   329: bipush #10
    //   331: imul
    //   332: i2d
    //   333: dadd
    //   334: dstore_3
    //   335: iload #9
    //   337: bipush #100
    //   339: imul
    //   340: istore_2
    //   341: goto -> 377
    //   344: iload #5
    //   346: i2d
    //   347: ldc2_w 0.1
    //   350: dmul
    //   351: iload #6
    //   353: i2d
    //   354: dadd
    //   355: iload #7
    //   357: bipush #10
    //   359: imul
    //   360: i2d
    //   361: dadd
    //   362: iload #8
    //   364: bipush #100
    //   366: imul
    //   367: i2d
    //   368: dadd
    //   369: dstore_3
    //   370: iload #9
    //   372: sipush #1000
    //   375: imul
    //   376: istore_2
    //   377: iload_2
    //   378: i2d
    //   379: dstore #11
    //   381: dload_3
    //   382: dload #11
    //   384: dadd
    //   385: dstore_3
    //   386: dload_3
    //   387: dstore #11
    //   389: iload #10
    //   391: ifeq -> 427
    //   394: new java/lang/StringBuilder
    //   397: dup
    //   398: invokespecial <init> : ()V
    //   401: astore_0
    //   402: aload_0
    //   403: ldc 'P66:isNegative：：'
    //   405: invokevirtual append : (Ljava/lang/String;)Ljava/lang/StringBuilder;
    //   408: pop
    //   409: aload_0
    //   410: iload #10
    //   412: invokevirtual append : (Z)Ljava/lang/StringBuilder;
    //   415: pop
    //   416: aload_0
    //   417: invokevirtual toString : ()Ljava/lang/String;
    //   420: invokestatic e : (Ljava/lang/String;)V
    //   423: dload_3
    //   424: dneg
    //   425: dstore #11
    //   427: iload #5
    //   429: iconst_m1
    //   430: if_icmpeq -> 466
    //   433: iload #6
    //   435: iconst_m1
    //   436: if_icmpeq -> 466
    //   439: iload #7
    //   441: iconst_m1
    //   442: if_icmpeq -> 466
    //   445: iload #8
    //   447: iconst_m1
    //   448: if_icmpeq -> 466
    //   451: iload #9
    //   453: iconst_m1
    //   454: if_icmpne -> 460
    //   457: goto -> 466
    //   460: dload #11
    //   462: dstore_3
    //   463: goto -> 468
    //   466: dconst_0
    //   467: dstore_3
    //   468: dload_3
    //   469: dreturn
  }
  
  public static DeviceType getDeviceType(byte paramByte) {
    DeviceType deviceType;
    if (paramByte != 1) {
      if (paramByte != 3) {
        if (paramByte != 4) {
          deviceType = DeviceType.S_5G;
        } else {
          deviceType = DeviceType.P_66;
        } 
      } else {
        deviceType = DeviceType.AB_300;
      } 
    } else {
      deviceType = DeviceType.QB_5G;
    } 
    return deviceType;
  }
  
  public static int getEndUnit(DeviceType paramDeviceType, boolean[] paramArrayOfboolean) {
    int i = null.$SwitchMap$com$yscoco$wyboem$myenum$DeviceType[paramDeviceType.ordinal()];
    byte b = 5;
    if (i != 1 && i != 2 && i != 3) {
      if (i == 4) {
        if (paramArrayOfboolean[15])
          return 1; 
        if (paramArrayOfboolean[35])
          return 2; 
        if (paramArrayOfboolean[31])
          return 3; 
        if (paramArrayOfboolean[25])
          return 4; 
        if (paramArrayOfboolean[24])
          return b; 
      } 
    } else {
      if (paramArrayOfboolean[10])
        return 1; 
      if (paramArrayOfboolean[13])
        return 2; 
      if (paramArrayOfboolean[15])
        return 3; 
      if (paramArrayOfboolean[19])
        return 4; 
      if (!paramArrayOfboolean[22])
        if (paramArrayOfboolean[21]) {
          b = 6;
        } else {
          if (paramArrayOfboolean[20])
            return 7; 
          b = 0;
        }  
      return b;
    } 
    b = 0;
  }
  
  public static String getEndUnitString(DeviceType paramDeviceType, boolean[] paramArrayOfboolean) {
    int i = null.$SwitchMap$com$yscoco$wyboem$myenum$DeviceType[paramDeviceType.ordinal()];
    String str = "Hz";
    if (i != 1 && i != 2 && i != 3) {
      if (i == 4) {
        if (paramArrayOfboolean[15])
          return "V"; 
        if (paramArrayOfboolean[35])
          return "A"; 
        if (paramArrayOfboolean[31])
          return "F"; 
        if (paramArrayOfboolean[25])
          return "Ω"; 
        if (paramArrayOfboolean[24])
          return str; 
      } 
    } else {
      if (paramArrayOfboolean[10])
        return "V"; 
      if (paramArrayOfboolean[13])
        return "A"; 
      if (paramArrayOfboolean[15])
        return "F"; 
      if (paramArrayOfboolean[19])
        return "Ω"; 
      if (!paramArrayOfboolean[22])
        if (paramArrayOfboolean[21]) {
          str = "℉";
        } else {
          if (paramArrayOfboolean[20])
            return "℃"; 
          str = "";
        }  
      return str;
    } 
    str = "";
  }
  
  public static int getEveryNum(int paramInt1, int paramInt2) {
    byte b = 6;
    if ((paramInt1 == 0 || paramInt1 == 1) && paramInt2 == 10) {
      paramInt1 = 1;
    } else if ((paramInt1 == 10 || paramInt1 == 11) && paramInt2 == 13) {
      paramInt1 = 2;
    } else if ((paramInt1 == 8 || paramInt1 == 9) && paramInt2 == 15) {
      paramInt1 = 3;
    } else if ((paramInt1 == 4 || paramInt1 == 5) && paramInt2 == 14) {
      paramInt1 = 4;
    } else if ((paramInt1 == 13 || paramInt1 == 12) && paramInt2 == 7) {
      paramInt1 = 5;
    } else if ((paramInt1 == 14 || paramInt1 == 15) && paramInt2 == 7) {
      paramInt1 = b;
    } else if ((paramInt1 == 8 || paramInt1 == 9) && paramInt2 == 10) {
      paramInt1 = 7;
    } else if ((paramInt1 == 14 || paramInt1 == 15) && paramInt2 == 15) {
      paramInt1 = 8;
    } else if ((paramInt1 == 12 || paramInt1 == 13) && paramInt2 == 15) {
      paramInt1 = 9;
    } else if (paramInt1 == 6 && paramInt2 == 1) {
      paramInt1 = 999;
    } else if (paramInt1 == 14 && paramInt2 == 14) {
      paramInt1 = 998;
    } else if (paramInt1 == 14 && paramInt2 == 5) {
      paramInt1 = 997;
    } else if (paramInt1 == 0 && paramInt2 == 4) {
      paramInt1 = 996;
    } else {
      paramInt1 = 0;
    } 
    return paramInt1;
  }
  
  public static int getEveryNumP66(int paramInt, boolean paramBoolean) {
    byte b = 0;
    if (paramBoolean)
      return ((paramInt & 0xC) == 12) ? 1 : 0; 
    if (paramInt != 10) {
      if (paramInt != 78) {
        if (paramInt != 138) {
          if (paramInt != 143) {
            if (paramInt != 173) {
              if (paramInt != 199) {
                if (paramInt != 207) {
                  if (paramInt != 231) {
                    if (paramInt != 235)
                      if (paramInt != 239) {
                        b = -1;
                      } else {
                        b = 8;
                      }  
                  } else {
                    b = 6;
                  } 
                } else {
                  b = 9;
                } 
              } else {
                b = 5;
              } 
            } else {
              b = 2;
            } 
          } else {
            b = 3;
          } 
        } else {
          b = 7;
        } 
      } else {
        b = 4;
      } 
    } else {
      b = 1;
    } 
    StringBuilder stringBuilder = new StringBuilder();
    stringBuilder.append("P66:计算值为：");
    stringBuilder.append(paramInt);
    stringBuilder.append(":计算结果:");
    stringBuilder.append(b);
    LogUtils.e(stringBuilder.toString());
    return b;
  }
  
  public static String getEveryStringNum(int paramInt1, int paramInt2) {
    String str;
    if ((paramInt1 == 0 || paramInt1 == 1) && paramInt2 == 10) {
      str = "1";
    } else if ((paramInt1 == 10 || paramInt1 == 11) && paramInt2 == 13) {
      str = "2";
    } else if ((paramInt1 == 8 || paramInt1 == 9) && paramInt2 == 15) {
      str = "3";
    } else if ((paramInt1 == 4 || paramInt1 == 5) && paramInt2 == 14) {
      str = "4";
    } else if ((paramInt1 == 13 || paramInt1 == 12) && paramInt2 == 7) {
      str = "5";
    } else if ((paramInt1 == 14 || paramInt1 == 15) && paramInt2 == 7) {
      str = "6";
    } else if ((paramInt1 == 8 || paramInt1 == 9) && paramInt2 == 10) {
      str = "7";
    } else if ((paramInt1 == 14 || paramInt1 == 15) && paramInt2 == 15) {
      str = "8";
    } else if ((paramInt1 == 12 || paramInt1 == 13) && paramInt2 == 15) {
      str = "9";
    } else if ((paramInt1 == 6 || paramInt1 == 7) && paramInt2 == 1) {
      str = "L";
    } else if ((paramInt1 == 14 || paramInt1 == 15) && paramInt2 == 14) {
      str = "A";
    } else if ((paramInt1 == 14 || paramInt1 == 15) && paramInt2 == 5) {
      str = "E";
    } else if ((paramInt1 == 0 || paramInt1 == 1) && paramInt2 == 4) {
      str = "-";
    } else if ((paramInt1 == 14 || paramInt1 == 15) && paramInt2 == 11) {
      str = "0";
    } else if ((paramInt1 == 2 || paramInt1 == 3) && paramInt2 == 7) {
      str = "O";
    } else if ((paramInt1 == 2 || paramInt1 == 3) && paramInt2 == 3) {
      str = "U";
    } else if ((paramInt1 == 7 || paramInt1 == 6) && paramInt2 == 5) {
      str = "T";
    } else if ((paramInt1 == 14 || paramInt1 == 15) && paramInt2 == 4) {
      str = "F";
    } else {
      str = "";
    } 
    return str;
  }
  
  public static String getEveryStringNumForP66(int paramInt, boolean paramBoolean) {
    String str = "1";
    if (paramBoolean)
      return ((paramInt & 0xC) == 12) ? "1" : ""; 
    switch (paramInt) {
      default:
        str = "";
        break;
      case 239:
        str = "8";
        break;
      case 238:
        str = "A";
        break;
      case 235:
        str = "0";
        break;
      case 231:
        str = "6";
        break;
      case 229:
        str = "E";
        break;
      case 228:
        str = "F";
        break;
      case 207:
        str = "9";
        break;
      case 199:
        str = "5";
        break;
      case 173:
        str = "2";
        break;
      case 143:
        str = "3";
        break;
      case 138:
        str = "7";
        break;
      case 101:
        str = "T";
        break;
      case 97:
        str = "L";
        break;
      case 78:
        str = "4";
        break;
      case 39:
        str = "O";
        break;
      case 35:
        str = "U";
        break;
      case 4:
        str = "-";
        break;
      case 10:
        break;
    } 
    StringBuilder stringBuilder = new StringBuilder();
    stringBuilder.append("P66:计算结果:");
    stringBuilder.append(paramInt);
    stringBuilder.append("最终值：");
    stringBuilder.append(str);
    LogUtils.e(stringBuilder.toString());
    return str;
  }
  
  public static boolean[] getIsResult(byte paramByte, boolean paramBoolean) {
    String str;
    boolean bool1;
    boolean bool2;
    if (paramBoolean) {
      str = Integer.toBinaryString((paramByte & 0xFF & 0xF0) / 16);
    } else {
      str = Integer.toBinaryString(paramByte & 0xFF & 0xF);
    } 
    if (str.length() == 4) {
      paramBoolean = true;
    } else {
      paramBoolean = false;
    } 
    if (str.length() > 2 && str.substring(str.length() - 3, str.length() - 2).equals("1")) {
      bool1 = true;
    } else {
      bool1 = false;
    } 
    if (str.length() > 1 && str.substring(str.length() - 2, str.length() - 1).equals("1")) {
      bool2 = true;
    } else {
      bool2 = false;
    } 
    return new boolean[] { paramBoolean, bool1, bool2, str.substring(str.length() - 1).equals("1") };
  }
  
  public static boolean[] getIsResultF66(byte paramByte, boolean paramBoolean) {
    String str;
    boolean bool1;
    boolean bool2;
    if (paramBoolean) {
      str = Integer.toBinaryString((paramByte & 0xFF & 0xF0) / 16);
    } else {
      str = Integer.toBinaryString(paramByte & 0xFF & 0xF);
    } 
    if (str.length() == 4) {
      paramBoolean = true;
    } else {
      paramBoolean = false;
    } 
    if (str.length() > 2 && str.substring(str.length() - 3, str.length() - 2).equals("1")) {
      bool1 = true;
    } else {
      bool1 = false;
    } 
    if (str.length() > 1 && str.substring(str.length() - 2, str.length() - 1).equals("1")) {
      bool2 = true;
    } else {
      bool2 = false;
    } 
    return new boolean[] { paramBoolean, bool1, bool2, str.substring(str.length() - 1).equals("1") };
  }
  
  public static boolean[] getMoreResult(BleByteBean[] paramArrayOfBleByteBean) {
    boolean[] arrayOfBoolean = getAllResult(paramArrayOfBleByteBean);
    return new boolean[] { arrayOfBoolean[1], arrayOfBoolean[3], arrayOfBoolean[7] };
  }
  
  public static boolean[] getRightOrderTable300(BleByteBean[] paramArrayOfBleByteBean) {
    boolean bool10;
    boolean[] arrayOfBoolean = getAllResult(paramArrayOfBleByteBean);
    boolean bool1 = false;
    boolean bool2 = arrayOfBoolean[0];
    boolean bool3 = arrayOfBoolean[2];
    boolean bool4 = arrayOfBoolean[7];
    boolean bool5 = arrayOfBoolean[3];
    boolean bool6 = arrayOfBoolean[8];
    boolean bool7 = arrayOfBoolean[21];
    boolean bool8 = arrayOfBoolean[23];
    boolean bool9 = arrayOfBoolean[12];
    if (arrayOfBoolean[14] || arrayOfBoolean[25]) {
      bool10 = true;
    } else {
      bool10 = false;
    } 
    boolean bool11 = arrayOfBoolean[20];
    boolean bool12 = arrayOfBoolean[4];
    boolean bool13 = arrayOfBoolean[15];
    boolean bool14 = arrayOfBoolean[16];
    if (arrayOfBoolean[13] || arrayOfBoolean[22] || arrayOfBoolean[24])
      bool1 = true; 
    return new boolean[] { 
        bool2, bool3, bool4, bool5, false, false, false, false, bool6, bool7, 
        bool8, bool9, bool10, bool11, bool12, bool13, bool14, bool1, arrayOfBoolean[17], arrayOfBoolean[18], 
        arrayOfBoolean[5], arrayOfBoolean[6], arrayOfBoolean[19], arrayOfBoolean[9] };
  }
  
  public static int getStartUnit(DeviceType paramDeviceType, boolean[] paramArrayOfboolean) {
    int i = null.$SwitchMap$com$yscoco$wyboem$myenum$DeviceType[paramDeviceType.ordinal()];
    byte b = 0;
    if (i != 1 && i != 2 && i != 3) {
      if (i == 4) {
        if (paramArrayOfboolean[28])
          return 1; 
        if (paramArrayOfboolean[27])
          return 3; 
        if (paramArrayOfboolean[29])
          return 4; 
        if (paramArrayOfboolean[26])
          return 5; 
      } 
    } else {
      if (paramArrayOfboolean[11])
        return 1; 
      if (paramArrayOfboolean[12]) {
        b = 2;
      } else {
        if (paramArrayOfboolean[16])
          return 3; 
        if (paramArrayOfboolean[17])
          return 4; 
        if (paramArrayOfboolean[18])
          return 5; 
      } 
    } 
    return b;
  }
  
  public static String getStartUnitString(DeviceType paramDeviceType, boolean[] paramArrayOfboolean) {
    int i = null.$SwitchMap$com$yscoco$wyboem$myenum$DeviceType[paramDeviceType.ordinal()];
    String str = "k";
    if (i != 1 && i != 2 && i != 3) {
      if (i == 4) {
        if (paramArrayOfboolean[28])
          return "n"; 
        if (paramArrayOfboolean[27])
          return "M"; 
        if (paramArrayOfboolean[29])
          return "m"; 
        if (paramArrayOfboolean[26])
          return str; 
      } 
    } else {
      if (paramArrayOfboolean[11])
        return "n"; 
      if (paramArrayOfboolean[12]) {
        str = "u";
      } else {
        if (paramArrayOfboolean[16])
          return "M"; 
        if (paramArrayOfboolean[17])
          return "m"; 
        if (paramArrayOfboolean[18])
          return str; 
        str = "";
      } 
      return str;
    } 
    str = "";
  }
  
  public static String getStringCount(byte[] paramArrayOfbyte) {
    if (paramArrayOfbyte.length != 5) {
      Log.e(TAG, "数组大小不满足条件");
      return "";
    } 
    byte b = 0;
    String str1 = getEveryStringNum((paramArrayOfbyte[0] & 0xFF & 0xF0) / 16, paramArrayOfbyte[1] & 0xFF & 0xF);
    String str2 = getEveryStringNum((paramArrayOfbyte[1] & 0xFF & 0xF0) / 16, paramArrayOfbyte[2] & 0xFF & 0xF);
    String str3 = getEveryStringNum((paramArrayOfbyte[2] & 0xFF & 0xF0) / 16, paramArrayOfbyte[3] & 0xFF & 0xF);
    String str4 = getEveryStringNum((paramArrayOfbyte[3] & 0xFF & 0xF0) / 16, paramArrayOfbyte[4] & 0xFF & 0xF);
    boolean bool = hasPoint((paramArrayOfbyte[0] & 0xFF & 0xF0) / 16);
    if (hasPoint((paramArrayOfbyte[1] & 0xFF & 0xF0) / 16)) {
      b = 1;
    } else if (hasPoint((paramArrayOfbyte[2] & 0xFF & 0xF0) / 16)) {
      b = 2;
    } else if (hasPoint((paramArrayOfbyte[3] & 0xFF & 0xF0) / 16)) {
      b = 3;
    } 
    StringBuilder stringBuilder = new StringBuilder();
    if (bool)
      stringBuilder.append("-"); 
    stringBuilder.append(str1);
    if (b == 1)
      stringBuilder.append("."); 
    stringBuilder.append(str2);
    if (b == 2)
      stringBuilder.append("."); 
    stringBuilder.append(str3);
    if (b == 3)
      stringBuilder.append("."); 
    stringBuilder.append(str4);
    return stringBuilder.toString();
  }
  
  public static String getStringCountP66(byte[] paramArrayOfbyte) {
    boolean bool;
    if (paramArrayOfbyte.length != 5) {
      Log.e(TAG, "数组大小不满足条件");
      return "";
    } 
    byte b = 0;
    String str1 = getEveryStringNumForP66(paramArrayOfbyte[0] & 0xEF, false);
    String str2 = getEveryStringNumForP66(paramArrayOfbyte[1] & 0xEF, false);
    String str3 = getEveryStringNumForP66(paramArrayOfbyte[2] & 0xEF, false);
    String str4 = getEveryStringNumForP66(paramArrayOfbyte[3] & 0xEF, false);
    String str5 = getEveryStringNumForP66(paramArrayOfbyte[4] & 0xEF, true);
    if ((paramArrayOfbyte[4] & 0x80) == 128) {
      bool = true;
    } else {
      bool = false;
    } 
    if ((paramArrayOfbyte[0] & 0x10) != 0) {
      b = 1;
    } else if ((paramArrayOfbyte[1] & 0x10) != 0) {
      b = 2;
    } else if ((paramArrayOfbyte[2] & 0x10) != 0) {
      b = 4;
    } else if ((paramArrayOfbyte[3] & 0x10) != 0) {
      b = 5;
    } else if ((paramArrayOfbyte[4] & 0x10) != 0) {
      b = 3;
    } 
    StringBuilder stringBuilder = new StringBuilder();
    if (bool)
      stringBuilder.append("-"); 
    stringBuilder.append(str5);
    if (b == 5)
      stringBuilder.append("."); 
    stringBuilder.append(str4);
    if (b == 4)
      stringBuilder.append("."); 
    stringBuilder.append(str3);
    if (b == 3)
      stringBuilder.append(":"); 
    if (b == 2)
      stringBuilder.append("."); 
    stringBuilder.append(str2);
    if (b == 1)
      stringBuilder.append("."); 
    stringBuilder.append(str1);
    return stringBuilder.toString();
  }
  
  public static int getTag(DeviceType paramDeviceType, boolean[] paramArrayOfboolean) {
    int i = null.$SwitchMap$com$yscoco$wyboem$myenum$DeviceType[paramDeviceType.ordinal()];
    boolean bool = false;
    if (i != 1 && i != 2 && i != 3) {
      if (i != 4) {
        i = bool;
      } else {
        if (paramArrayOfboolean[21])
          return 1; 
        if (paramArrayOfboolean[18])
          return 2; 
        if (paramArrayOfboolean[6] && !paramArrayOfboolean[5])
          return 3; 
        if (!paramArrayOfboolean[6] && paramArrayOfboolean[5])
          return 4; 
        i = bool;
        if (paramArrayOfboolean[6]) {
          i = bool;
          if (paramArrayOfboolean[5])
            return 34; 
        } 
      } 
    } else {
      if (paramArrayOfboolean[8])
        return 1; 
      if (paramArrayOfboolean[9])
        return 2; 
      if (paramArrayOfboolean[0] && !paramArrayOfboolean[14])
        return 3; 
      if (!paramArrayOfboolean[0] && paramArrayOfboolean[14])
        return 4; 
      i = bool;
      if (paramArrayOfboolean[0]) {
        i = bool;
        if (paramArrayOfboolean[14])
          return 34; 
      } 
    } 
    return i;
  }
  
  public static String getUnit(DeviceType paramDeviceType, boolean[] paramArrayOfboolean) {
    StringBuilder stringBuilder1;
    String str2;
    int i = null.$SwitchMap$com$yscoco$wyboem$myenum$DeviceType[paramDeviceType.ordinal()];
    String str3 = "Hz";
    String str1 = "k";
    if (i != 1 && i != 2 && i != 3) {
      if (i != 4) {
        str2 = "";
        str1 = str2;
      } else {
        StringBuilder stringBuilder;
        if (str2[28] != null) {
          str1 = "n";
        } else if (str2[27] != null) {
          str1 = "M";
        } else if (str2[29] != null) {
          str1 = "m";
        } else if (str2[26] == null) {
          str1 = "";
        } 
        if (str2[15] != null) {
          str2 = "V";
          stringBuilder = new StringBuilder();
          stringBuilder.append(str1);
          stringBuilder.append(str2);
          return stringBuilder.toString();
        } 
        if (str2[35] != null) {
          str2 = "A";
          stringBuilder = new StringBuilder();
          stringBuilder.append(str1);
          stringBuilder.append(str2);
          return stringBuilder.toString();
        } 
        if (str2[31] != null) {
          str2 = "F";
          stringBuilder = new StringBuilder();
          stringBuilder.append(str1);
          stringBuilder.append(str2);
          return stringBuilder.toString();
        } 
        if (str2[25] != null) {
          str2 = "Ω";
          stringBuilder = new StringBuilder();
          stringBuilder.append(str1);
          stringBuilder.append(str2);
          return stringBuilder.toString();
        } 
        String str = str1;
        if (str2[24] != null) {
          str2 = str3;
          stringBuilder = new StringBuilder();
          stringBuilder.append(str1);
          stringBuilder.append(str2);
          return stringBuilder.toString();
        } 
        str2 = "";
        stringBuilder1 = stringBuilder;
      } 
    } else {
      if (str2[11] != null) {
        str1 = "n";
      } else if (str2[12] != null) {
        str1 = "u";
      } else if (str2[16] != null) {
        str1 = "M";
      } else if (str2[17] != null) {
        str1 = "m";
      } else if (str2[18] == null) {
        str1 = "";
      } 
      if (str2[10] != null) {
        str2 = "V";
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append(str1);
        stringBuilder.append(str2);
        return stringBuilder.toString();
      } 
      if (str2[13] != null) {
        str2 = "A";
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append(str1);
        stringBuilder.append(str2);
        return stringBuilder.toString();
      } 
      if (str2[15] != null) {
        str2 = "F";
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append(str1);
        stringBuilder.append(str2);
        return stringBuilder.toString();
      } 
      if (str2[19] != null) {
        str2 = "Ω";
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append(str1);
        stringBuilder.append(str2);
        return stringBuilder.toString();
      } 
      if (str2[22] != null) {
        str2 = str3;
      } else if (str2[21] != null) {
        str2 = "℉";
      } else {
        StringBuilder stringBuilder;
        String str = str1;
        if (str2[20] != null) {
          str2 = "℃";
          stringBuilder = new StringBuilder();
          stringBuilder.append(str1);
          stringBuilder.append(str2);
          return stringBuilder.toString();
        } 
        str2 = "";
        stringBuilder1 = stringBuilder;
      } 
    } 
    StringBuilder stringBuilder2 = new StringBuilder();
    stringBuilder2.append((String)stringBuilder1);
    stringBuilder2.append(str2);
    return stringBuilder2.toString();
  }
  
  public static boolean hasPoint(int paramInt) {
    boolean bool = true;
    if (paramInt % 2 != 1)
      bool = false; 
    return bool;
  }
}


/* Location:              C:\Users\xy790\Desktop\decode\dex-tools-2.1\output\!\com\yscoco\wyboem\ble\Util\BleComputeUtil.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       1.1.3
 */