
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class slf4jhelloworld {
  public static void main(String[] args) {
    Logger logger = LoggerFactory.getLogger(slf4jhelloworld.class);
    logger.info("Hello World");
  }
}
