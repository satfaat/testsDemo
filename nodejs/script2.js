const puppeteer = require('puppeteer');

async function testYaRu(){
    console.log('Запуск браузера');
    // todo: создай константу browser и присвой ей результат асинхронного вызова метода launch объекта puppeteer
    const browser = await puppeteer.launch();

    console.log('Создание новой вкладки в браузере');
    // todo: создай константу page и присвоей ей результат асинхронного вызова метода newPage объекта browser
    const page = await browser.newPage();

    console.log('Переход на страницу ya.ru');
    // todo: напиши команду перехода на страницу 'https://ya.ru/'
    await page.goto('https://ya.ru/');

    console.log('Ввод текста "Автоматизация тестирования" в поисковую строку');
    // todo: создай константу searchField и присвоей ей результат поиска элемента текстового поля
    // todo: напиши команду ввода в поле текст 'Автоматизация тестирования'
    const searchField = await page.$('#text');
    await searchField.type('Автоматизация тестирования');

    console.log('Клик в кнопку "Найти"');
    // todo: создай константу searchButton и присвоей ей результат поиска элемента кнопки "Найти"
    // todo: напиши команду клика в кнопку поиска
    const searchButton = await page.$('.button[type=submit]');
    await searchButton.click();

    console.log('Закрытие браузера');
    // todo: напиши команду асинхронного закрытия браузера
    await browser.close();
}

testYaRu();