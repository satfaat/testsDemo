import http from 'k6/http';
import { sleep, check } from 'k6';


export const options = {
  vus: 1,
  duration: '1s',
};

export default function () {

  // given
  const url = 'URL/login';
  const params = {
    headers: {
      'Content-Type': 'application/xml',
    },
  };

  // when
  const res = http.post(url, params);

  // then
  check(res, { 'status was 200': (r) => r.status == 200 });
  console.log('Token is ' + res.json('body.token'));
  sleep(1);
}
