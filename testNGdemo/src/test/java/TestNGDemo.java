import org.testng.Assert;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;

public class TestNGDemo {

    @BeforeTest
    public void setup() {
        //todo
    }

    @Test
    public void testOther() {
        Assert.assertEquals("ActualTitle", "ActualTitle");
        System.out.println("First TestNG test");
    }

    @AfterTest
    public void tearDownTest() {
        //todo
    }
}
