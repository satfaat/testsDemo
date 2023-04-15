package restAssureDemo

import api.params.Post
import io.restassured.response.Response
import spock.lang.Shared
import spock.lang.Specification
import io.github.cdimascio.dotenv.Dotenv
import spock.lang.Stepwise

import static io.restassured.RestAssured.given
import static org.assertj.core.api.Assertions.assertThat
import static org.hamcrest.Matchers.equalTo

@Stepwise
class RestAssuredSpec extends Specification {

    @Shared
    Dotenv dotenv = Dotenv.load()

    @Shared
    String postId

    def "data demo"() {
        given:
        Map postParams = new HashMap()
        postParams.put("userId", 1)

        Post postPrm1 = new Post(1)

        expect:
        println postParams
        println postParams.getClass()
        println postParams.toString().getClass()
        println postParams.toMapString()
        println postParams.toMapString().getClass()
    }

    def "assertj demo"() {
        expect:
        assertThat("The lord of the rings").isNotNull()
                .startsWith("The")
                .contains("lord")
                .endsWith("rings")
    }

    def "get demo"() {
        given:
        String URL_BASE = "https://jsonplaceholder.typicode.com/"
        String ENDPOINT = "posts"
        Map postParams = new HashMap()
        postParams.put("userId", 1)

        when:
        Response res = given()
                .queryParams(postParams)
                .log().all()
                .request("GET", URL_BASE + ENDPOINT)

        Response res2 = RestAPI.res(postParams, "GET", URL_BASE + ENDPOINT)
        postId = res2
                .then()
                .extract().jsonPath().getString("[0].userId")

        then:
        res2.then()
                .log().ifError()
                .statusCode(200)
                .body("[0].userId", equalTo(1))

        println postId
    }

    def "get post by id"() {
        given:
        String URL_BASE = "https://jsonplaceholder.typicode.com/"
        String ENDPOINT = "posts/"

        when:
        Response res = RestAPI.res(new HashMap<String, String>(), "GET", URL_BASE + ENDPOINT + postId)

        then:
        res.then()
                .log().ifError()
                .statusCode(200)
                .body("userId", equalTo(1))
    }
}
