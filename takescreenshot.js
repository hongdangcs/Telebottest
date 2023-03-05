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
        await page.goto("https://www.tradingview.com/chart/?symbol=" + args[0]);
        await page.screenshot({path: "photo/entire-page.png"});
        await delay(1000);
        await page.mouse.click(228, 21)
        await delay(1000);

        await page.mouse.click(310, 387)
        await delay(1000);


        //  await page.click('isFirst-Jc9IXW74');

        const element = await page.waitForSelector('div > .chart-container');
        await element.screenshot({path: "photo/" + args[1] + ".png"});

        const inner_currency = await page.$eval('.currency-qqt8UV2f', element => element.innerHTML);

        await delay(1000);

        const inner_price_html = await page.$eval('.buttonText-_W8EGxGy', element => element.innerHTML);

        await delay(1000);
        let inner_price = inner_price_html.replace('<span class=\"highlight-vZ7uMuW4 growing-vZ7uMuW4\">', '');
        inner_price = inner_price.replace('</span>', '');

        let price = inner_price + inner_currency;

        fs.writeFileSync(args[1] + 'price.txt', price);
        console.log(price);
        await browser.close();
    });

function delay(time) {
    return new Promise(resolve => setTimeout(resolve, time));
}