import http from 'k6/http';
import { sleep, check } from 'k6';


let date_current = new Date();

export const options = {
    // vus: 1,
    // duration: '10s',

    stages: [
        { duration: '2m', target: 8 }, // simulate ramp-up of traffic from 1 to 100 users over 5 minutes.
        { duration: '5m', target: 10 }, // stay at 100 users for 10 minutes
        { duration: '2m', target: 0 }, // ramp-down to 0 users
    ],
};

export default function () {

    // given
    const url = 'put your URL';
    const token = 'put your token';
    const params = {
        headers: {
            'jd-token': token,
            'Content-Type': 'application/xml',
            'Accept-Language': 'ru-RU',
        },
    };
    let depDate = "28.03.2023";
    const payload = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><do_order_req><backward>false</backward><ordersRequest>" +
        "<request><car><number>08</number><type>Сидячий</type></car><depDate>" + depDate + "</depDate><requirements>" +
        "<seatsRange>14-14</seatsRange></requirements><stationFrom>2900700</stationFrom>" +
        "<stationTo>2900930</stationTo><train><number>770Ф</number></train></request>" +
        "</ordersRequest><passengers><passengers><children>" +
        "<valid>true</valid><birthDay>02.05.2018</birthDay><citizenship>UZB</citizenship>" +
        "<doc>AA99</doc><docType>TYPE</docType><firstname>NM</firstname><lastname>LNM</lastname>" +
        "<midname>MNM</midname><regionId>03</regionId><sex>М</sex></children><valid>true</valid>" +
        "<child5From10>false</child5From10><birthDay>01.01.2015</birthDay><citizenship>UZB</citizenship>" +
        "<doc>AA99</doc><docType>TYPE</docType><firstname>FNM</firstname><lastname>LNM</lastname>" +
        "<midname>MNM</midname><regionId>03</regionId><pinfl></pinfl><sex>М</sex></passengers>" +
        "</passengers><withInsurance>true</withInsurance><withSmsNotification>true</withSmsNotification></do_order_req>";

    // when
    const res = http.post(url, payload, params);

    // then
    check(res, {
        'Booked with 200': (r) => r.status == 200,
        'Body is not empty': (r) => r.json('body') != null,
        'status is 200': (r) => r.json('status') == 200,
        'status is 404': (r) => r.json('status') == 404,
        'status is 504': (r) => r.json('status') == 504
    });
    console.info(date_current.toString());
    console.log(res.status);
    console.log('Inner status is ' + res.json('status') + " type: " + typeof (res.json('status')));
    console.log('Order id is ' + res.json('body.orderId'));
    sleep(1);
}
