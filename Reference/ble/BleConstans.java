package com.yscoco.wyboem.ble;

import com.yscoco.wyboem.myenum.DeviceType;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class BleConstans {
  public static final String CHA_BATTERY_NOTIFY = "00002A19-0000-1000-8000-00805F9B34FB";
  
  public static final String CHA_FIRMWARE_VISION_READ = "00002A26-0000-1000-8000-00805F9B34FB";
  
  public static final String CHA_NOTIFY = "0000FFF4-0000-1000-8000-00805F9B34FB";
  
  public static final String CHA_OTA_WRITE = "6E40FF02-B5A3-F393-E0A9-E50E24DCCA9E";
  
  public static final String CHA_VISION_READ = "00002A27-0000-1000-8000-00805F9B34FB";
  
  public static final String CHA_WRITE = "0000FFF4-0000-1000-8000-00805F9B34FB";
  
  public static final String RECONNECT_SCANNER_STATE_CHANGLE = "com.yscoco.ble.RECONNECT_SCANNER_STATE_CHANGLE";
  
  public static final String SERVICE_BATTERY_UUID = "0000180F-0000-1000-8000-00805F9B34FB";
  
  public static final String SERVICE_OTA_UUID = "6E40FF01-B5A3-F393-E0A9-E50E24DCCA9E";
  
  public static final String SERVICE_UUID1 = "0000FFF0-0000-1000-8000-00805F9B34FB";
  
  public static final String SERVICE_VESION_UUID = "0000180A-0000-1000-8000-00805F9B34FB";
  
  public static int battery = 100;
  
  public static Map<String, DeviceType> deviceTypeMap;
  
  public static boolean isOpenReconnectScanner = true;
  
  public static List<Float> listFour;
  
  public static List<Float> listOne = new ArrayList<Float>();
  
  public static List<Float> listThree;
  
  public static List<Float> listTwo = new ArrayList<Float>();
  
  public static List<Float>[] lists;
  
  public static String name;
  
  public static float[] times;
  
  static {
    listThree = new ArrayList<Float>();
    listFour = new ArrayList<Float>();
    lists = (List<Float>[])new List[] { listOne, listTwo, listThree, listFour };
    times = new float[] { 1.0F, 1.0F, 1.0F, 1.0F };
    name = "";
    deviceTypeMap = new HashMap<String, DeviceType>();
  }
}


/* Location:              C:\Users\xy790\Desktop\decode\dex-tools-2.1\output\!\com\yscoco\wyboem\ble\BleConstans.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       1.1.3
 */