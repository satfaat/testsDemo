package restAssureDemo

import io.restassured.response.Response

import static io.restassured.RestAssured.given

class RestAPI {
    static Response res(Map<String, ?> params, String method, String url) {
        Response res = given()
                .queryParams(params)
                .log().all()
                .request(method, url)
        return res
    }
}
