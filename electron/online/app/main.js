const electron = require('electron');
const app = electron.app;
const ipcMain = electron.ipcMain;
const BrowserWindow = electron.BrowserWindow;

let onlineStatusWindow;

app.on('ready', () => {
    onlineStatusWindow = new BrowserWindow({ width: 800, height: 600, show: false });
    onlineStatusWindow.loadURL(`file://${__dirname}/online-status.html`);
});

ipcMain.on('online-status-changed', (event, status) => {
    console.log(status);
});
