const puppeteer = require("puppeteer");
const fs = require('fs');
const args = process.argv.slice(2);
puppeteer
    .launch({
        defaultViewport: {
            width: 1920,
            height: 1080,
        },
    })
    .then(async (browser) => {
        const page = await browser.newPage();
        await page.goto("https://www.tradingview.com/chart/?symbol="+args[0]);
        await page.screenshot({ path: "photo/entire-page.png" });

        const element = await page.waitForSelector('div > .chart-container');
        await element.screenshot({path: "photo/"+args[1]+".png"});
/*
        const inner_html = await page.$eval('.priceWrapper-qqt8UV2f', element => element.innerHTML);

        console.log(inner_html);

        const price = inner_html.innerText;
        console.log(price)*/
        console.log("pham hong dang")
        await browser.close();
    });