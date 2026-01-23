"use client";

import { useEffect } from "react";
import { registerServiceWorker } from "@/app/register-sw";

export default function PWAInstaller() {
  useEffect(() => {
    // Register service worker
    registerServiceWorker();
  }, []);

  return null;
}
