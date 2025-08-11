import { app, BrowserWindow } from "electron/main";
import path from "node:path";
import { fileURLToPath } from "url";
const __dirname = path.dirname(fileURLToPath(import.meta.url));
import dotenv from "dotenv";

const createWindow = () => {
  dotenv.config();
  const win = new BrowserWindow({
    width: 1280,
    height: 720,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: true,
      contentSecurityPolicy: `
        default-src 'self';
        script-src 'self' 'unsafe-eval';
        style-src 'self' 'unsafe-inline';
        img-src 'self' data:;
        connect-src 'self' http://localhost:*;
      `,
    },
  });

  if (process.env.NODE_ENV === "development") {
    win.loadURL("http://localhost:5173");
  } else {
    win.loadFile(path.join(__dirname, "../dist/index.html"));
  }
};

app.whenReady().then(() => {
  createWindow();

  app.on("activate", () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  });
});

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") {
    app.quit;
  }
});
