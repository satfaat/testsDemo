import groovy.util.logging.Slf4j
import io.github.cdimascio.dotenv.Dotenv
import spock.lang.Specification

@Slf4j
class SpockParametrizationDemo extends Specification {

    Dotenv dotenv = Dotenv.load();

    def "length of Spock's and his friends' names"() {
        expect:
        name.size() == length

        where:
        name     | length
        "Spock"  | 5
        "Kirk"   | 4
        "Scotty" | 6
    }

    def "dotenv demo"() {
        expect:
        log.info(dotenv.get("URL"))
        dotenv.get("URL") == 'https://example.com'
    }
}
