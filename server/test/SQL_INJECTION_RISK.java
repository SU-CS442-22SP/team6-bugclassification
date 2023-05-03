package server.test;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class SQL_INJECTION_RISK {

    public void getsql(Connection connection, String userId) {
        try {
            Statement stmt = connection.createStatement();
            String query = "SELECT * FROM users WHERE userId = '" + userId + "'";
            ResultSet rs = stmt.executeQuery(query);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

}
