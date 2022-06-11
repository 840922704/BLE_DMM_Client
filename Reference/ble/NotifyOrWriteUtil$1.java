package com.yscoco.wyboem.ble;

import com.yscoco.yscocomodule.log.LogUtils;

final class null implements Runnable {
  public void run() {
    NotifyOrWriteUtil.clearState();
    LogUtils.e("NotifyOrWriteUtils:超时清除状态");
  }
}


/* Location:              C:\Users\xy790\Desktop\decode\dex-tools-2.1\output\!\com\yscoco\wyboem\ble\NotifyOrWriteUtil$1.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       1.1.3
 */