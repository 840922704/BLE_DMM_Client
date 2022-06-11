package com.yscoco.wyboem.myenum;

public enum DeviceType {
  AB_300, P_66, QB_5G, S_5G;
  
  static {
    AB_300 = new DeviceType("AB_300", 2);
    P_66 = new DeviceType("P_66", 3);
    $VALUES = new DeviceType[] { QB_5G, S_5G, AB_300, P_66 };
  }
}


/* Location:              C:\Users\xy790\Desktop\decode\dex-tools-2.1\output\!\com\yscoco\wyboem\myenum\DeviceType.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       1.1.3
 */