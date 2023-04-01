from pyrogram import filters

filters_used = ~ filters.command("enviar") & ~ filters.command("cat") & ~ filters.command("start")